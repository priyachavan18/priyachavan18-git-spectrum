import streamlit as st
import pandas as pd
import plotly.express as px

from utils.load_data import load_data



st.title("🛍️ Product Analytics")
st.caption("Product Performance Dashboard")

# ----------------------------------------------------
# LOAD DATA
# ----------------------------------------------------

df = load_data()

# ----------------------------------------------------
# PRODUCT SUMMARY
# ----------------------------------------------------

product = (
    df.groupby("Description")
    .agg(
        Revenue=("TotalAmount", "sum"),
        Quantity=("Quantity", "sum"),
        Orders=("InvoiceNo", "nunique"),
        Customers=("CustomerID", "nunique"),
    )
    .reset_index()
)

product = product.sort_values("Revenue", ascending=False)

# ----------------------------------------------------
# KPI
# ----------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric("Products", len(product))
c2.metric("Revenue", f"£{product['Revenue'].sum():,.0f}")
c3.metric("Units Sold", f"{product['Quantity'].sum():,.0f}")
c4.metric("Top Product", product.iloc[0]["Description"])

st.divider()

# ----------------------------------------------------
# TOP PRODUCTS
# ----------------------------------------------------

fig = px.bar(
    product.head(15),
    x="Revenue",
    y="Description",
    orientation="h",
    color="Revenue",
    template="plotly_dark",
    title="Top 15 Products by Revenue"
)

fig.update_layout(yaxis={"categoryorder": "total ascending"})

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------
# QUANTITY SOLD
# ----------------------------------------------------

fig2 = px.bar(
    product.head(15),
    x="Description",
    y="Quantity",
    color="Quantity",
    template="plotly_dark",
    title="Top Products by Quantity Sold"
)

fig2.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig2, use_container_width=True)

# ----------------------------------------------------
# REVENUE VS ORDERS
# ----------------------------------------------------

fig3 = px.scatter(
    product,
    x="Orders",
    y="Revenue",
    size="Quantity",
    color="Revenue",
    hover_name="Description",
    template="plotly_dark",
    title="Revenue vs Orders"
)

st.plotly_chart(fig3, use_container_width=True)

# ----------------------------------------------------
# PRODUCT SEARCH
# ----------------------------------------------------

st.subheader("🔍 Search Product")

search = st.text_input("Enter Product Name")

if search:

    result = product[
        product["Description"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

    st.dataframe(result, use_container_width=True)

else:

    st.dataframe(product.head(25), use_container_width=True)

# ----------------------------------------------------
# BEST PRODUCTS
# ----------------------------------------------------

st.subheader("🏆 Product Recommendations")

top5 = product.head(5)

for _, row in top5.iterrows():

    st.success(
        f"""
**{row['Description']}**

Revenue: £{row['Revenue']:,.2f}

Units Sold: {row['Quantity']:,.0f}

Orders: {row['Orders']}
"""
    )