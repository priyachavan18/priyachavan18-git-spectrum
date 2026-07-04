import streamlit as st
import pandas as pd
from pathlib import Path

@st.cache_data
def load_data():

    BASE_DIR = Path(__file__).resolve().parent.parent
    csv_path = BASE_DIR / "data" / "online_retail.csv"

    df = pd.read_csv(csv_path, encoding="ISO-8859-1")

    df = df.dropna(subset=["CustomerID", "Description"])

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")

    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

    df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

    return df
