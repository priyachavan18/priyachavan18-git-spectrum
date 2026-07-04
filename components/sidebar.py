import streamlit as st


def sidebar():

    with st.sidebar:

        # ----------------------------
        # LOGO
        # ----------------------------

        st.title("🛒 Shopper Spectrum")

        st.markdown("""
### Customer Intelligence Platform
""")

        st.divider()

        # ----------------------------
        # STATUS
        # ----------------------------

        st.success("✅ Machine Learning Enabled")

        st.info("📂 Dataset : Online Retail")

        st.divider()

        # ----------------------------
        # NAVIGATION
        # ----------------------------

        st.subheader("📌 Navigation")

        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("app.py")

        if st.button("📊 Dashboard", use_container_width=True):
            st.switch_page("pages/1_Dashboard.py")

        if st.button("👥 Customer Segmentation", use_container_width=True):
            st.switch_page("pages/2_Customer_Segmentation.py")

        if st.button("🛍️ Product Recommendation", use_container_width=True):
            st.switch_page("pages/3_Product_Recommendation.py")

        if st.button("📈 Business Insights", use_container_width=True):
            st.switch_page("pages/4_Business_Insights.py")

        if st.button("ℹ️ About", use_container_width=True):
            st.switch_page("pages/5_About.py")

        st.divider()

        # ----------------------------
        # PROJECT DETAILS
        # ----------------------------

        st.subheader("📊 Project Details")

        st.markdown("""
**Algorithm:** K-Means

**Recommendation:** Collaborative Filtering

**Framework:** Streamlit

**Dataset:** Online Retail
""")

        st.divider()

        st.caption("© 2026 Shopper Spectrum")