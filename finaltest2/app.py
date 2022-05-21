#importing the necessary libraries
import streamlit as st
#setting page width for all pages
st.set_page_config(layout="wide")
#importing the other pages of the multipage apps
from multiapp import MultiApp
from apps import home, financeDashboard, prediction # import your app modules here
app = MultiApp()

# Adding all application pages here
app.add_app("Home", home.app)
app.add_app("Finance Dashboard", financeDashboard.app)
app.add_app("Prediction",prediction.app)

# The main app
app.run()