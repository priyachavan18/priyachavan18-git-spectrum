from components.insights import show_insights
import streamlit as st
from components.filters import sidebar_filters
from utils.load_data import load_data
from components.kpi_cards import show_kpis
from components.charts import (
    prepare_data,
    monthly_revenue_chart,
    country_sales_chart,
    top_products_chart,
    quantity_chart,
    country_map,
    country_donut,
    sales_heatmap,
    daily_sales_chart,
)


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📊 Executive Dashboard")
st.caption("Real-Time E-Commerce Analytics")

st.divider()

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = load_data()
df = prepare_data(df)
df = sidebar_filters(df)

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

show_kpis(df)

st.divider()

# --------------------------------------------------
# ROW 1
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        monthly_revenue_chart(df),
        use_container_width=True,
    )

with col2:
    st.plotly_chart(
        country_sales_chart(df),
        use_container_width=True,
    )

# --------------------------------------------------
# ROW 2
# --------------------------------------------------

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(
        top_products_chart(df),
        use_container_width=True,
    )

with col4:
    st.plotly_chart(
        quantity_chart(df),
        use_container_width=True,
    )

# --------------------------------------------------
# ROW 3
# --------------------------------------------------

col5, col6 = st.columns(2)

with col5:
    st.plotly_chart(
        country_donut(df),
        use_container_width=True,
    )

with col6:
    st.plotly_chart(
        country_map(df),
        use_container_width=True,
    )

# --------------------------------------------------
# ROW 4
# --------------------------------------------------

st.plotly_chart(
    sales_heatmap(df),
    use_container_width=True,
)

st.plotly_chart(
    daily_sales_chart(df),
    use_container_width=True,
)
st.divider()

show_insights(df)