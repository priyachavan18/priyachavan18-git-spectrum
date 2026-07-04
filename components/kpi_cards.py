import streamlit as st


def show_kpis(df):
    """
    Display KPI cards for the dashboard.
    """

    total_revenue = df["TotalAmount"].sum()
    total_orders = df["InvoiceNo"].nunique()
    total_customers = df["CustomerID"].nunique()
    total_products = df["Description"].nunique()
    avg_order_value = total_revenue / total_orders if total_orders > 0 else 0
    total_quantity = df["Quantity"].sum()

    st.subheader("📈 Business Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="💰 Total Revenue",
            value=f"£{total_revenue:,.2f}"
        )

    with col2:
        st.metric(
            label="🛒 Total Orders",
            value=f"{total_orders:,}"
        )

    with col3:
        st.metric(
            label="👥 Total Customers",
            value=f"{total_customers:,}"
        )

    st.markdown("")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric(
            label="📦 Products Sold",
            value=f"{total_quantity:,}"
        )

    with col5:
        st.metric(
            label="🛍 Unique Products",
            value=f"{total_products:,}"
        )

    with col6:
        st.metric(
            label="💳 Avg Order Value",
            value=f"£{avg_order_value:,.2f}"
        )