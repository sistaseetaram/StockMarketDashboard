#framework we used to create multipages in a single stremlit web app
# https://github.com/upraneelnihar/streamlit-multiapps
#above is the link for the original framwork that we used
"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        app=st.sidebar.image("data/LOGO.png", use_column_width=True)
        app=st.sidebar.write("""
# Dashboard
 """)
        app = st.sidebar.selectbox(
    "Go To",
    self.apps,
    format_func=lambda app: app['title']
)
        app['function']()