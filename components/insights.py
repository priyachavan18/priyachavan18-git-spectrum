import streamlit as st


def show_insights(df):

    st.subheader("🧠 Business Insights")

    # -----------------------------
    # Top Country
    # -----------------------------
    top_country = (
        df.groupby("Country")["TotalAmount"]
        .sum()
        .idxmax()
    )

    top_country_sales = (
        df.groupby("Country")["TotalAmount"]
        .sum()
        .max()
    )

    # -----------------------------
    # Top Product
    # -----------------------------
    top_product = (
        df.groupby("Description")["TotalAmount"]
        .sum()
        .idxmax()
    )

    top_product_sales = (
        df.groupby("Description")["TotalAmount"]
        .sum()
        .max()
    )

    # -----------------------------
    # Best Customer
    # -----------------------------
    best_customer = (
        df.groupby("CustomerID")["TotalAmount"]
        .sum()
        .idxmax()
    )

    customer_sales = (
        df.groupby("CustomerID")["TotalAmount"]
        .sum()
        .max()
    )

    # -----------------------------
    # Highest Revenue Month
    # -----------------------------
    monthly = (
        df.groupby("Month")["TotalAmount"]
        .sum()
    )

    best_month = monthly.idxmax()
    best_month_sales = monthly.max()

    # -----------------------------
    # Metrics
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:

        st.success(
            f"""
🌍 **Best Country:** {top_country}

Revenue: **£{top_country_sales:,.2f}**
"""
        )

        st.info(
            f"""
📦 **Top Product**

{top_product}

Revenue: **£{top_product_sales:,.2f}**
"""
        )

    with col2:

        st.warning(
            f"""
👤 **Top Customer**

Customer ID: **{best_customer}**

Revenue: **£{customer_sales:,.2f}**
"""
        )

        st.error(
            f"""
📈 **Highest Revenue Month**

{best_month}

Revenue: **£{best_month_sales:,.2f}**
"""
        )

    st.divider()

    st.subheader("📌 Executive Recommendations")

    st.markdown("""
- Focus marketing on the highest revenue countries.
- Increase stock for top-performing products.
- Reward high-value customers with loyalty offers.
- Monitor monthly revenue trends to identify seasonal demand.
- Promote underperforming products through targeted campaigns.
- Improve customer retention using personalized recommendations.
""")