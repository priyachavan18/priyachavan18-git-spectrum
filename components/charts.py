# charts.py

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ----------------------------
# PREPARE DATA
# ----------------------------
def prepare_data(df):
    df = df.copy()

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)
    df["Date"] = df["InvoiceDate"].dt.date

    return df


# ----------------------------
# MONTHLY REVENUE
# ----------------------------
def monthly_revenue_chart(df):

    revenue = (
        df.groupby("Month")["TotalAmount"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        revenue,
        x="Month",
        y="TotalAmount",
        markers=True,
        template="plotly_dark"
    )

    fig.update_layout(
        title="Monthly Revenue",
        height=450,
        xaxis_title="Month",
        yaxis_title="Revenue"
    )

    return fig


# ----------------------------
# DAILY SALES
# ----------------------------
def daily_sales_chart(df):

    sales = (
        df.groupby("Date")["TotalAmount"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        sales,
        x="Date",
        y="TotalAmount",
        template="plotly_dark"
    )

    fig.update_layout(
        title="Daily Revenue",
        height=450
    )

    return fig


# ----------------------------
# TOP PRODUCTS
# ----------------------------
def top_products_chart(df):

    products = (
        df.groupby("Description")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        products,
        x="TotalAmount",
        y="Description",
        orientation="h",
        template="plotly_dark"
    )

    fig.update_layout(
        title="Top 10 Products",
        height=500,
        yaxis=dict(categoryorder="total ascending")
    )

    return fig


# ----------------------------
# COUNTRY SALES
# ----------------------------
def country_sales_chart(df):

    country = (
        df.groupby("Country")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        country,
        x="Country",
        y="TotalAmount",
        color="TotalAmount",
        template="plotly_dark"
    )

    fig.update_layout(
        title="Top Countries by Revenue",
        height=450,
        coloraxis_showscale=False
    )

    return fig


# ----------------------------
# COUNTRY MAP
# ----------------------------
def country_map(df):

    country = (
        df.groupby("Country")["TotalAmount"]
        .sum()
        .reset_index()
    )

    fig = px.choropleth(
        country,
        locations="Country",
        locationmode="country names",
        color="TotalAmount",
        color_continuous_scale="Viridis",
        template="plotly_dark"
    )

    fig.update_layout(
        title="Revenue by Country",
        height=500
    )

    return fig


# ----------------------------
# ORDER QUANTITY
# ----------------------------
def quantity_chart(df):

    qty = (
        df.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        qty,
        x="Description",
        y="Quantity",
        color="Quantity",
        template="plotly_dark"
    )

    fig.update_layout(
        title="Most Sold Products",
        height=450,
        xaxis_tickangle=-45,
        coloraxis_showscale=False
    )

    return fig


# ----------------------------
# REVENUE DONUT
# ----------------------------
def country_donut(df):

    country = (
        df.groupby("Country")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    fig = px.pie(
        country,
        names="Country",
        values="TotalAmount",
        hole=0.6,
        template="plotly_dark"
    )

    fig.update_layout(
        title="Revenue Share by Country",
        height=450
    )

    return fig


# ----------------------------
# HEATMAP
# ----------------------------
def sales_heatmap(df):

    df["Hour"] = df["InvoiceDate"].dt.hour
    df["Weekday"] = df["InvoiceDate"].dt.day_name()

    heat = (
        df.pivot_table(
            values="TotalAmount",
            index="Weekday",
            columns="Hour",
            aggfunc="sum",
            fill_value=0
        )
    )

    fig = go.Figure(
        data=go.Heatmap(
            z=heat.values,
            x=heat.columns,
            y=heat.index,
            colorscale="Viridis"
        )
    )

    fig.update_layout(
        title="Sales Heatmap",
        height=500,
        template="plotly_dark"
    )

    return fig
def prepare_data(df):
    import pandas as pd

    df = df.copy()
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)
    df["Date"] = df["InvoiceDate"].dt.date
    return df