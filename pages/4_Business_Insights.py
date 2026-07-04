import streamlit as st
import pandas as pd
import plotly.express as px

from utils.load_data import load_data


st.title("📈 Executive Business Insights")
st.caption("Strategic Overview of Business Performance")

# ----------------------------
# LOAD DATA
# ----------------------------

df = load_data()

df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

# ----------------------------
# KPIs
# ----------------------------

total_revenue = df["TotalAmount"].sum()
total_orders = df["InvoiceNo"].nunique()
customers = df["CustomerID"].nunique()
products = df["Description"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Revenue", f"£{total_revenue:,.0f}")
c2.metric("Orders", f"{total_orders:,}")
c3.metric("Customers", customers)
c4.metric("Products", products)

st.divider()

# ----------------------------
# Monthly Revenue
# ----------------------------

monthly = (
    df.groupby("Month")["TotalAmount"]
    .sum()
    .reset_index()
)

fig = px.line(
    monthly,
    x="Month",
    y="TotalAmount",
    markers=True,
    template="plotly_dark",
    title="Monthly Revenue Trend"
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# Top Countries
# ----------------------------

country = (
    df.groupby("Country")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig2 = px.bar(
    country,
    x="Country",
    y="TotalAmount",
    color="TotalAmount",
    template="plotly_dark",
    title="Top 10 Countries"
)

st.plotly_chart(fig2, use_container_width=True)

# ----------------------------
# Top Customers
# ----------------------------

customers_df = (
    df.groupby("CustomerID")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig3 = px.bar(
    customers_df,
    x="CustomerID",
    y="TotalAmount",
    color="TotalAmount",
    template="plotly_dark",
    title="Top 10 Customers"
)

st.plotly_chart(fig3, use_container_width=True)

# ----------------------------
# Top Products
# ----------------------------

products_df = (
    df.groupby("Description")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig4 = px.bar(
    products_df,
    x="TotalAmount",
    y="Description",
    orientation="h",
    color="TotalAmount",
    template="plotly_dark",
    title="Top 10 Products"
)

fig4.update_layout(
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(fig4, use_container_width=True)

# ----------------------------
# Executive Summary
# ----------------------------

st.subheader("📋 Executive Summary")

best_country = country.iloc[0]["Country"]
best_product = products_df.iloc[0]["Description"]
best_customer = customers_df.iloc[0]["CustomerID"]
best_month = monthly.loc[
    monthly["TotalAmount"].idxmax(), "Month"
]

st.success(f"""
### Key Findings

- 💰 Total Revenue: **£{total_revenue:,.2f}**
- 🌍 Highest Revenue Country: **{best_country}**
- 📦 Best Selling Product: **{best_product}**
- 👤 Highest Value Customer: **{best_customer}**
- 📈 Best Performing Month: **{best_month}**
""")

st.subheader("💡 Business Recommendations")

st.info("""
### Recommendations

1. Focus marketing campaigns on the highest-performing countries.

2. Increase inventory for top-selling products.

3. Reward loyal customers with exclusive offers.

4. Improve retention of low-frequency customers.

5. Monitor monthly sales to prepare inventory for seasonal demand.

6. Bundle low-selling products with high-selling products.

7. Launch personalized email campaigns using customer purchase history.

8. Expand successful products into additional markets.
""")

st.divider()

st.download_button(
    "⬇ Download Executive Summary",
    data=f"""
Total Revenue: £{total_revenue:,.2f}

Orders: {total_orders}

Customers: {customers}

Products: {products}

Top Country: {best_country}

Top Product: {best_product}

Top Customer: {best_customer}

Best Month: {best_month}
""",
    file_name="Executive_Business_Report.txt"
)