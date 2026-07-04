import streamlit as st
import pandas as pd
import plotly.express as px

from utils.load_data import load_data

# =====================================
# TITLE
# =====================================

st.title("👥 Customer Segmentation")
st.caption("RFM Analysis Dashboard")

st.divider()

# =====================================
# LOAD DATA
# =====================================

df = load_data()

snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

# =====================================
# CREATE RFM TABLE
# =====================================

rfm = (
    df.groupby("CustomerID")
    .agg(
        Recency=("InvoiceDate", lambda x: (snapshot_date - x.max()).days),
        Frequency=("InvoiceNo", "nunique"),
        Monetary=("TotalAmount", "sum"),
    )
    .reset_index()
)

# =====================================
# RFM SCORES
# =====================================

rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    q=5,
    labels=[5, 4, 3, 2, 1],
    duplicates="drop",
)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    q=5,
    labels=[1, 2, 3, 4, 5],
    duplicates="drop",
)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    q=5,
    labels=[1, 2, 3, 4, 5],
    duplicates="drop",
)

rfm["R_Score"] = rfm["R_Score"].astype(int)
rfm["F_Score"] = rfm["F_Score"].astype(int)
rfm["M_Score"] = rfm["M_Score"].astype(int)

rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str)
    + rfm["F_Score"].astype(str)
    + rfm["M_Score"].astype(str)
)

# =====================================
# SEGMENT LOGIC
# =====================================

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

# =====================================
# KPI CARDS
# =====================================

c1, c2, c3, c4 = st.columns(4)

c1.metric("👥 Customers", f"{len(rfm):,}")
c2.metric("💰 Revenue", f"£{rfm['Monetary'].sum():,.0f}")
c3.metric("🛒 Avg Customer Value", f"£{rfm['Monetary'].mean():,.0f}")
c4.metric("🏆 Largest Segment", rfm["Segment"].mode()[0])

st.divider()

# =====================================
# SEGMENT COUNTS
# =====================================

segment_count = (
    rfm["Segment"]
    .value_counts()
    .reset_index()
)

segment_count.columns = ["Segment", "Customers"]

# =====================================
# CHARTS
# =====================================

left, right = st.columns(2)

with left:

    fig1 = px.bar(
        segment_count,
        x="Segment",
        y="Customers",
        color="Customers",
        template="plotly_dark",
        title="Customer Segments",
    )

    st.plotly_chart(fig1, use_container_width=True)

with right:

    fig2 = px.pie(
        segment_count,
        names="Segment",
        values="Customers",
        hole=0.65,
        template="plotly_dark",
        title="Segment Distribution",
    )

    st.plotly_chart(fig2, use_container_width=True)

# =====================================
# SCATTER
# =====================================

fig3 = px.scatter(
    rfm,
    x="Frequency",
    y="Monetary",
    color="Segment",
    size="Monetary",
    hover_data=["CustomerID"],
    template="plotly_dark",
    title="Customer Distribution",
)

st.plotly_chart(fig3, use_container_width=True)

# =====================================
# TOP CUSTOMERS
# =====================================

st.subheader("🏆 Top 20 Customers by Revenue")

top_customers = (
    rfm.sort_values("Monetary", ascending=False)
    .head(20)
)

st.dataframe(
    top_customers,
    use_container_width=True,
    hide_index=True,
)
