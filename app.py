import streamlit as st
from components.sidebar import sidebar
# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Shopper Spectrum",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)
sidebar()
# -----------------------------
# HERO
# -----------------------------

st.markdown("""
<div style="
background: linear-gradient(135deg,#0F172A,#1E40AF,#2563EB);
padding:40px;
border-radius:20px;
box-shadow:0px 8px 25px rgba(0,0,0,0.25);
">

<h1 style="
color:white;
font-size:52px;
margin-bottom:8px;
">
🛒 Shopper Spectrum
</h1>

<h3 style="
color:#E2E8F0;
margin-top:0;
">
Retail Intelligence & Customer Analytics Platform
</h3>

<p style="
color:#CBD5E1;
font-size:18px;
line-height:1.8;
">
Transform retail transaction data into interactive dashboards,
customer intelligence, product analytics and executive business insights
using Python, SQL, Machine Learning and Streamlit.
</p>

</div>
""", unsafe_allow_html=True)
st.write("")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("💰 Revenue", "£8.89M")

with c2:
    st.metric("🧾 Orders", "18,532")

with c3:
    st.metric("👥 Customers", "4,372")

with c4:
    st.metric("🌍 Countries", "38")
    st.write("")
st.subheader("🚀 Platform Modules")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("""
### 📊 Dashboard

Executive KPIs

Revenue Analysis

Sales Trends

Geo Analytics
""")

with col2:
    st.info("""
### 👥 Customers

RFM Analysis

Segmentation

Customer Value

Behaviour
""")

with col3:
    st.info("""
### 🛍 Products

Revenue

Performance

Recommendations

Top Products
""")

with col4:
    st.info("""
### 📈 Insights

Executive Report

Recommendations

Growth

Forecast
""")
    st.write("")
st.subheader("⭐ Why Shopper Spectrum?")

left, right = st.columns(2)

with left:

    st.success("""
✅ Executive Dashboard

✅ Customer Segmentation

✅ Product Analytics

✅ Business Insights

✅ Interactive Visualizations
""")

with right:

    st.success("""
✅ Machine Learning Ready

✅ Retail Intelligence

✅ KPI Monitoring

✅ Business Reporting

✅ Portfolio Project
""")
    st.write("")
st.subheader("🛠 Technology Stack")

t1,t2,t3,t4,t5,t6 = st.columns(6)

t1.metric("🐍","Python")
t2.metric("🗄","SQL")
t3.metric("📊","Plotly")
t4.metric("⚡","Streamlit")
t5.metric("🤖","Scikit-learn")
t6.metric("🐼","Pandas")
st.write("")
st.subheader("⚙ Analytics Workflow")

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
Analytics Engine
      │
 ┌────┼────┐
 ▼    ▼    ▼
Dashboard
Customer Analytics
Product Analytics
      │
      ▼
Business Intelligence
""", language="text")
st.write("")
st.subheader("📂 Dataset Summary")

d1,d2,d3,d4 = st.columns(4)

d1.metric("Transactions","541,909")
d2.metric("Products","3,684")
d3.metric("Customers","4,372")
d4.metric("Countries","38")
st.divider()

st.markdown("""
<div style="text-align:center;color:gray;">

### Shopper Spectrum

Retail Intelligence & Customer Analytics Platform

Built with ❤️ using Python • Streamlit • SQL • Machine Learning

Developed by **Priya Chavan**

</div>
""", unsafe_allow_html=True)