import streamlit as st

# ======================================================
# TITLE
# ======================================================

st.title("ℹ️ About Shopper Spectrum")
st.caption("Retail Intelligence & Customer Analytics Platform")

st.divider()

# ======================================================
# HERO
# ======================================================

st.markdown("""
## 🛒 Shopper Spectrum

An enterprise-style Retail Intelligence Platform designed to transform raw retail transactions into meaningful business insights using Business Intelligence, Customer Analytics, Interactive Dashboards and Machine Learning.
""")

st.divider()

# ======================================================
# PROJECT OVERVIEW
# ======================================================

st.header("📌 Project Overview")

st.info("""
This project demonstrates a complete Data Analytics workflow from data collection and cleaning to executive reporting.

It enables organizations to:

• Monitor business performance

• Understand customer behaviour

• Track product performance

• Support strategic business decisions

• Improve profitability using analytics
""")

# ======================================================
# PLATFORM MODULES
# ======================================================

st.header("🚀 Platform Modules")

c1, c2 = st.columns(2)

with c1:

    st.success("""
### 📊 Executive Dashboard

• KPI Monitoring

• Revenue Analysis

• Sales Trends

• Geographic Performance
""")

    st.success("""
### 👥 Customer Segmentation

• RFM Analysis

• Customer Value

• Behaviour Analysis

• Customer Insights
""")

with c2:

    st.success("""
### 🛍 Product Analytics

• Product Revenue

• Quantity Analysis

• Product Search

• Best Sellers
""")

    st.success("""
### 📈 Business Intelligence

• Executive Summary

• Business Recommendations

• Strategic Reporting

• Trend Analysis
""")

st.divider()

# ======================================================
# TECHNOLOGY STACK
# ======================================================

st.header("🛠 Technology Stack")

t1, t2, t3, t4 = st.columns(4)

with t1:
    st.metric("🐍", "Python")

with t2:
    st.metric("🗄", "SQL")

with t3:
    st.metric("📊", "Plotly")

with t4:
    st.metric("⚡", "Streamlit")

st.divider()

# ======================================================
# DATASET
# ======================================================

st.header("📂 Dataset")

st.success("""
Dataset : Online Retail

• 541,909 Transactions

• 4,372 Customers

• 3,684 Products

• 38 Countries
""")

st.divider()

# ======================================================
# SKILLS
# ======================================================

st.header("🎯 Skills Demonstrated")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
✅ Data Cleaning

✅ Exploratory Data Analysis

✅ Data Visualization

✅ KPI Development

✅ Business Intelligence
""")

with col2:

    st.markdown("""
✅ Customer Segmentation

✅ Python Programming

✅ SQL Analysis

✅ Dashboard Development

✅ Business Analytics
""")

st.divider()

# ======================================================
# PROJECT WORKFLOW
# ======================================================

st.header("⚙ Analytics Workflow")

st.code("""
Retail Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Analytics
      │
      ▼
Interactive Dashboard
      │
      ▼
Business Intelligence
""", language="text")

st.divider()

# ======================================================
# DEVELOPER
# ======================================================

st.header("👨‍💻 Developer")

st.info("""
### Rohit Chavan

Aspiring Data Analyst

Python • SQL • Excel • Power BI • Streamlit • Pandas • NumPy • Plotly

Passionate about building professional Business Intelligence solutions that transform raw data into actionable insights.
""")

st.divider()

# ======================================================
# FOOTER
# ======================================================

st.caption(
    "© 2026 Shopper Spectrum | Retail Intelligence & Customer Analytics Platform"
)
