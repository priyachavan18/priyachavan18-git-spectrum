import streamlit as st
import pandas as pd
import plotly.express as px

from utils.load_data import load_data

# ===================================================
# TITLE
# ===================================================

st.title("📈 Executive Business Insights")
st.caption("Strategic Business Intelligence Dashboard")

st.divider()

# ===================================================
# LOAD DATA
# ===================================================

df = load_data()

df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

# ===================================================
# KPIs
# ===================================================

total_revenue = df["TotalAmount"].sum()
total_orders = df["InvoiceNo"].nunique()
customers = df["CustomerID"].nunique()
products = df["Description"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Revenue", f"£{total_revenue:,.0f}")
c2.metric("🛒 Orders", f"{total_orders:,}")
c3.metric("👥 Customers", f"{customers:,}")
c4.metric("📦 Products", f"{products:,}")

st.divider()

# ===================================================
# DATASETS
# ===================================================

monthly = (
    df.groupby("Month")["TotalAmount"]
    .sum()
    .reset_index()
)

country = (
    df.groupby("Country")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

customers_df = (
    df.groupby("CustomerID")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

products_df = (
    df.groupby("Description")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

# ===================================================
# ROW 1
# ===================================================

left, right = st.columns(2)

with left:

    fig1 = px.line(
        monthly,
        x="Month",
        y="TotalAmount",
        markers=True,
        template="plotly_dark",
        title="Monthly Revenue Trend",
    )

    st.plotly_chart(fig1, use_container_width=True)

with right:

    fig2 = px.bar(
        country,
        x="Country",
        y="TotalAmount",
        color="TotalAmount",
        template="plotly_dark",
        title="Top 10 Countries by Revenue",
    )

    st.plotly_chart(fig2, use_container_width=True)

# ===================================================
# ROW 2
# ===================================================

left, right = st.columns(2)

with left:

    fig3 = px.bar(
        customers_df,
        x="CustomerID",
        y="TotalAmount",
        color="TotalAmount",
        template="plotly_dark",
        title="Top 10 Customers",
    )

    st.plotly_chart(fig3, use_container_width=True)

with right:

    fig4 = px.bar(
        products_df,
        x="TotalAmount",
        y="Description",
        orientation="h",
        color="TotalAmount",
        template="plotly_dark",
        title="Top 10 Products",
    )

    fig4.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    st.plotly_chart(fig4, use_container_width=True)

st.divider()

# ===================================================
# EXECUTIVE SUMMARY
# ===================================================

best_country = country.iloc[0]["Country"]
best_product = products_df.iloc[0]["Description"]
best_customer = customers_df.iloc[0]["CustomerID"]
best_month = monthly.loc[
    monthly["TotalAmount"].idxmax(),
    "Month",
]

st.subheader("📋 Executive Summary")

col1, col2 = st.columns(2)

with col1:

    st.success(f"""
### Business Highlights

• Revenue : **£{total_revenue:,.0f}**

• Best Country : **{best_country}**

• Best Month : **{best_month}**

• Orders : **{total_orders:,}**
""")

with col2:

    st.info(f"""
### Top Performers

• Product : **{best_product}**

• Customer : **{best_customer}**

• Customers : **{customers:,}**

• Products : **{products:,}**
""")

st.divider()

# ===================================================
# RECOMMENDATIONS
# ===================================================

st.subheader("💡 Strategic Recommendations")

st.warning("""
### Executive Recommendations

1. Increase inventory for top-performing products.

2. Expand marketing campaigns in high-revenue countries.

3. Reward loyal customers with exclusive offers.

4. Target at-risk customers through retention campaigns.

5. Bundle slow-moving products with best sellers.

6. Forecast monthly demand for inventory planning.

7. Personalize promotions using customer purchase history.

8. Monitor product performance continuously using KPIs.
""")

st.divider()

# ===================================================
# DOWNLOAD REPORT
# ===================================================

report = f"""
EXECUTIVE BUSINESS REPORT

Total Revenue : £{total_revenue:,.2f}

Orders : {total_orders}

Customers : {customers}

Products : {products}

Top Country : {best_country}

Top Product : {best_product}

Top Customer : {best_customer}

Best Month : {best_month}
"""

st.download_button(
    "⬇ Download Executive Report",
    data=report,
    file_name="Executive_Business_Report.txt",
)
