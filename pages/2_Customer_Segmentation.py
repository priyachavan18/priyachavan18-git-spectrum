
import streamlit as st
import pandas as pd
import plotly.express as px

from utils.load_data import load_data


st.title("👥 Customer Segmentation")
st.caption("RFM Analysis Dashboard")

# ----------------------------------------------------
# LOAD DATA
# ----------------------------------------------------

df = load_data()

snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

# ----------------------------------------------------
# RFM TABLE
# ----------------------------------------------------

rfm = df.groupby("CustomerID").agg(
    Recency=("InvoiceDate", lambda x: (snapshot_date - x.max()).days),
    Frequency=("InvoiceNo", "nunique"),
    Monetary=("TotalAmount", "sum")
).reset_index()

# ----------------------------------------------------
# RFM SCORES
# ----------------------------------------------------

rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    5,
    labels=[5,4,3,2,1]
)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5,
    labels=[1,2,3,4,5]
)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"],
    5,
    labels=[1,2,3,4,5]
)

rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str) +
    rfm["F_Score"].astype(str) +
    rfm["M_Score"].astype(str)
)

# ----------------------------------------------------
# CUSTOMER SEGMENTS
# ----------------------------------------------------

def segment(row):

    if row["R_Score"] >= 4 and row["F_Score"] >= 4:
        return "Champions"

    elif row["F_Score"] >= 4:
        return "Loyal Customers"

    elif row["R_Score"] >= 4:
        return "Potential Loyalists"

    elif row["M_Score"] >= 4:
        return "Big Spenders"

    elif row["R_Score"] <= 2:
        return "At Risk"

    else:
        return "Others"

rfm["Segment"] = rfm.apply(segment, axis=1)

# ----------------------------------------------------
# KPI
# ----------------------------------------------------

c1,c2,c3,c4 = st.columns(4)

c1.metric("Customers", len(rfm))
c2.metric("Revenue", f"£{rfm['Monetary'].sum():,.0f}")
c3.metric("Avg Customer Value", f"£{rfm['Monetary'].mean():,.0f}")
c4.metric("Best Segment", rfm["Segment"].mode()[0])

st.divider()

# ----------------------------------------------------
# SEGMENT CHART
# ----------------------------------------------------

segment_count = (
    rfm["Segment"]
    .value_counts()
    .reset_index()
)

segment_count.columns=["Segment","Customers"]

fig = px.bar(
    segment_count,
    x="Segment",
    y="Customers",
    color="Customers",
    template="plotly_dark",
    title="Customer Segments"
)

st.plotly_chart(fig,use_container_width=True)

# ----------------------------------------------------
# SCATTER
# ----------------------------------------------------

fig2 = px.scatter(
    rfm,
    x="Frequency",
    y="Monetary",
    color="Segment",
    size="Monetary",
    hover_data=["CustomerID"],
    template="plotly_dark",
    title="Customer Distribution"
)

st.plotly_chart(fig2,use_container_width=True)

# ----------------------------------------------------
# PIE
# ----------------------------------------------------

fig3 = px.pie(
    segment_count,
    names="Segment",
    values="Customers",
    hole=0.6,
    template="plotly_dark",
    title="Segment Share"
)

st.plotly_chart(fig3,use_container_width=True)

# ----------------------------------------------------
# TABLE
# ----------------------------------------------------

st.subheader("Customer RFM Table")

st.dataframe(
    rfm.sort_values(
        "Monetary",
        ascending=False
    ),
    use_container_width=True
)