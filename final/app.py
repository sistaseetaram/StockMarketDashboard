import streamlit as st
st.set_page_config(layout="wide")
from multiapp import MultiApp
from apps import home, financeDashboard, prediction # import your app modules here
app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Finance Dashboard", financeDashboard.app)
app.add_app("Prediction",prediction.app)

# The main app
app.run()