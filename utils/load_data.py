import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    # Read CSV
    df = pd.read_csv("data/online_retail.csv", encoding="ISO-8859-1")

    # Remove missing values
    df = df.dropna(subset=["CustomerID", "Description"])

    # Convert date
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Correct data types
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")

    # Remove invalid transactions
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

    # Create TotalAmount column
    df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

    # Convert CustomerID to integer
    df["CustomerID"] = df["CustomerID"].astype(int)

    return df