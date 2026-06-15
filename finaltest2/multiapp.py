"""
Multi-Page Framework for Streamlit Applications
"""

import streamlit as st
from typing import List, Callable, Dict
import logging

logger = logging.getLogger(__name__)


class MultiApp:
    """Framework for combining multiple Streamlit applications into a single app."""
    
    def __init__(self):
        """Initialize the MultiApp framework"""
        self.apps: List[Dict[str, str | Callable]] = []
    
    def add_app(self, title: str, func: Callable) -> None:
        """
        Add a new application page
        
        Args:
            title (str): Title of the app page
            func (Callable): The Python function to render this app
        """
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string")
        
        if not callable(func):
            raise ValueError(f"Function for '{title}' must be callable")
        
        self.apps.append({"title": title, "function": func})
        logger.info(f"Added app: {title}")
    
    def run(self) -> None:
        """Run the multi-app framework with sidebar navigation"""
        st.set_page_config(page_title="Stock Market Dashboard", page_icon="📈", layout="wide")
        
        st.sidebar.markdown("# Dashboard Navigation")
        
        try:
            st.sidebar.image("data/LOGO.png", use_column_width=True)
        except FileNotFoundError:
            logger.warning("Logo file not found at data/LOGO.png")
        except Exception as e:
            logger.warning(f"Could not load logo: {str(e)}")
        
        st.sidebar.markdown("---")
        
        if not self.apps:
            st.error("❌ No apps registered. Please add apps using add_app().")
            return
        
        selected_app = st.sidebar.selectbox("Navigate to", self.apps, format_func=lambda app: app['title'], help="Select a page to view")
        
        try:
            selected_app['function']()
        except Exception as e:
            logger.error(f"Error running app '{selected_app['title']}': {str(e)}")
            st.error(f"❌ An error occurred: {str(e)}")
        
        st.sidebar.markdown("---")
        st.sidebar.markdown("📊 **Stock Market Dashboard** v2.0  \nBuilt with Streamlit & Prophet")
