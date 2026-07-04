import streamlit as st


def sidebar_filters(df):
    """
    Sidebar filters for the dashboard.
    """

    st.sidebar.header("🔎 Dashboard Filters")

    # --------------------------
    # Country Filter
    # --------------------------

    countries = ["All"] + sorted(df["Country"].dropna().unique().tolist())

    selected_country = st.sidebar.selectbox(
        "🌍 Select Country",
        countries
    )

    if selected_country != "All":
        df = df[df["Country"] == selected_country]

    # --------------------------
    # Date Filter
    # --------------------------

    min_date = df["InvoiceDate"].min().date()
    max_date = df["InvoiceDate"].max().date()

    start_date, end_date = st.sidebar.date_input(
        "📅 Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    if start_date and end_date:
        df = df[
            (df["InvoiceDate"].dt.date >= start_date)
            & (df["InvoiceDate"].dt.date <= end_date)
        ]

    # --------------------------
    # Product Search
    # --------------------------

    product = st.sidebar.text_input(
        "📦 Search Product"
    )

    if product:
        df = df[
            df["Description"].str.contains(
                product,
                case=False,
                na=False
            )
        ]

    # --------------------------
    # Customer Filter
    # --------------------------

    customers = sorted(df["CustomerID"].unique())

    customer = st.sidebar.selectbox(
        "👤 Customer",
        ["All"] + customers
    )

    if customer != "All":
        df = df[df["CustomerID"] == customer]

    st.sidebar.markdown("---")
    st.sidebar.success(f"Rows Selected: {len(df):,}")

    return df