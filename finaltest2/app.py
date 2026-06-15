"""
Stock Market Dashboard - Main Entry Point
Multi-page Streamlit application for real-time stock analysis
"""

import streamlit as st
from multiapp import MultiApp
from apps import home, financeDashboard, prediction

# Configure page layout
st.set_page_config(
    page_title="Stock Market Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize the multi-app framework
app = MultiApp()

# Register all application pages
app.add_app("Home", home.app)
app.add_app("Finance Dashboard", financeDashboard.app)
app.add_app("Prediction", prediction.app)

# Run the application
if __name__ == "__main__":
    app.run()
