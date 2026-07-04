import streamlit as st
import pandas as pd
import plotly.express as px

from utils.load_data import load_data

# ==================================================
# TITLE
# ==================================================

st.title("🛍️ Product Analytics")
st.caption("Product Performance & Recommendation Dashboard")

st.divider()

# ==================================================
# LOAD DATA
# ==================================================

df = load_data()

# ==================================================
# PRODUCT SUMMARY
# ==================================================

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

# ==================================================
# KPI CARDS
# ==================================================

c1, c2, c3, c4 = st.columns(4)

c1.metric("🛍 Products", f"{len(product):,}")
c2.metric("💰 Revenue", f"£{product['Revenue'].sum():,.0f}")
c3.metric("📦 Units Sold", f"{product['Quantity'].sum():,.0f}")
c4.metric("🏆 Best Seller", product.iloc[0]["Description"][:20])

st.divider()

# ==================================================
# ROW 1
# ==================================================

left, right = st.columns(2)

with left:

    fig1 = px.bar(
        product.head(10),
        x="Revenue",
        y="Description",
        orientation="h",
        color="Revenue",
        template="plotly_dark",
        title="Top 10 Products by Revenue",
    )

    fig1.update_layout(yaxis={"categoryorder": "total ascending"})

    st.plotly_chart(fig1, use_container_width=True)

with right:

    fig2 = px.bar(
        product.head(10),
        x="Quantity",
        y="Description",
        orientation="h",
        color="Quantity",
        template="plotly_dark",
        title="Top 10 Products by Units Sold",
    )

    fig2.update_layout(yaxis={"categoryorder": "total ascending"})

    st.plotly_chart(fig2, use_container_width=True)

# ==================================================
# ROW 2
# ==================================================

left, right = st.columns(2)

with left:

    fig3 = px.scatter(
        product,
        x="Orders",
        y="Revenue",
        size="Quantity",
        color="Revenue",
        hover_name="Description",
        template="plotly_dark",
        title="Revenue vs Orders",
    )

    st.plotly_chart(fig3, use_container_width=True)

with right:

    fig4 = px.pie(
        product.head(10),
        names="Description",
        values="Revenue",
        hole=0.6,
        template="plotly_dark",
        title="Revenue Share (Top 10)",
    )

    st.plotly_chart(fig4, use_container_width=True)

st.divider()

# ==================================================
# PRODUCT SEARCH
# ==================================================

st.subheader("🔍 Product Search")

search = st.text_input("Search Product")

if search:

    result = product[
        product["Description"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

    st.dataframe(
        result,
        use_container_width=True,
        hide_index=True,
    )

else:

    st.dataframe(
        product.head(20),
        use_container_width=True,
        hide_index=True,
    )

st.divider()

# ==================================================
# EXECUTIVE INSIGHTS
# ==================================================

st.subheader("📈 Executive Insights")

best = product.iloc[0]
highest_quantity = product.sort_values("Quantity", ascending=False).iloc[0]
highest_orders = product.sort_values("Orders", ascending=False).iloc[0]

col1, col2, col3 = st.columns(3)

with col1:
    st.success(f"""
### 🏆 Highest Revenue

**{best['Description']}**

Revenue

**£{best['Revenue']:,.0f}**
""")

with col2:
    st.info(f"""
### 📦 Most Sold

**{highest_quantity['Description']}**

Units Sold

**{highest_quantity['Quantity']:,.0f}**
""")

with col3:
    st.warning(f"""
### 🛒 Most Ordered

**{highest_orders['Description']}**

Orders

**{highest_orders['Orders']:,.0f}**
""")
