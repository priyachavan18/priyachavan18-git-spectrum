import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------


# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("ℹ️ About Spectrum Retail Intelligence Platform")

st.markdown("""
Welcome to the **Spectrum Retail Intelligence Platform**, an end-to-end business intelligence application developed to transform raw retail transaction data into meaningful business insights through interactive dashboards and advanced analytics.
""")

st.divider()

# ---------------------------------------------------
# PROJECT OVERVIEW
# ---------------------------------------------------

st.header("📌 Project Overview")

st.write("""
Spectrum Retail Intelligence Platform enables organizations to analyze sales performance, customer behavior, and product trends through interactive visualizations and analytics. It demonstrates the complete data analytics workflow, from data cleaning to executive reporting.
""")

# ---------------------------------------------------
# KEY FEATURES
# ---------------------------------------------------

st.header("🚀 Key Features")

col1, col2 = st.columns(2)

with col1:
    st.success("""
### 📊 Dashboard

- Executive KPI Dashboard
- Revenue Analysis
- Sales Trends
- Country-wise Performance
- Product Analysis
""")

    st.success("""
### 👥 Customer Analytics

- RFM Segmentation
- Customer Insights
- Customer Value Analysis
- Purchase Behaviour
""")

with col2:
    st.success("""
### 🛍 Product Analytics

- Best Selling Products
- Product Revenue
- Quantity Analysis
- Product Search
""")

    st.success("""
### 📈 Business Intelligence

- Executive Insights
- Business Recommendations
- Trend Analysis
- Interactive Reports
""")

st.divider()

# ---------------------------------------------------
# BUSINESS VALUE
# ---------------------------------------------------

st.header("💼 Business Value")

st.info("""
This application helps businesses to:

• Monitor business performance in real time

• Identify high-value customers

• Analyze customer purchasing behaviour

• Track product performance

• Discover sales opportunities

• Support strategic business decisions

• Improve customer retention

• Increase profitability through data-driven insights
""")

# ---------------------------------------------------
# TECHNOLOGY STACK
# ---------------------------------------------------

st.header("🛠 Technology Stack")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.markdown("""
### Programming

- Python
- SQL
""")

with tech2:
    st.markdown("""
### Analytics

- Pandas
- NumPy
- Plotly
- Scikit-learn
""")

with tech3:
    st.markdown("""
### Visualization

- Streamlit
- Plotly
- Git
- GitHub
""")

st.divider()

# ---------------------------------------------------
# DATASET
# ---------------------------------------------------

st.header("📂 Dataset")

st.write("""
The project uses the **Online Retail Dataset**, which contains transactional records of a UK-based online retailer. The dataset includes customer purchases, invoice details, products, quantities, prices, countries, and transaction dates.
""")

st.divider()

# ---------------------------------------------------
# PROJECT MODULES
# ---------------------------------------------------

st.header("📑 Project Modules")

modules = [
    "📊 Executive Dashboard",
    "👥 Customer Segmentation",
    "🛍 Product Analytics",
    "📈 Business Insights",
    "🌍 Geographic Sales Analysis",
    "📄 Executive Reporting"
]

for module in modules:
    st.markdown(f"✅ {module}")

st.divider()

# ---------------------------------------------------
# SKILLS DEMONSTRATED
# ---------------------------------------------------

st.header("🎯 Skills Demonstrated")

skills = [
    "Data Cleaning",
    "Exploratory Data Analysis",
    "Business Intelligence",
    "Data Visualization",
    "Customer Segmentation",
    "Interactive Dashboard Development",
    "KPI Design",
    "Business Analytics",
    "Python Programming",
    "SQL Analysis"
]

cols = st.columns(2)

for i, skill in enumerate(skills):
    cols[i % 2].markdown(f"✔ {skill}")

st.divider()

# ---------------------------------------------------
# DEVELOPER
# ---------------------------------------------------

st.header("👨‍💻 Developer")

st.markdown("""
### Priya Chavan

**Aspiring Data Analyst**

**Skills**

- Python
- Excel
- Streamlit
- Pandas
- NumPy
- Plotly

Passionate about transforming data into actionable business insights through analytics, dashboards, and machine learning.
""")

st.divider()

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.caption(
    "Spectrum Retail Intelligence Platform | Developed using Python, Streamlit and Data Analytics"
)