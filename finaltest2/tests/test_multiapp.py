import pytest
from unittest.mock import patch, MagicMock
from finaltest2.multiapp import MultiApp

def test_multiapp_init():
    app = MultiApp()
    assert app.apps == []

def test_multiapp_add_app():
    app = MultiApp()
    mock_func = MagicMock()
    app.add_app("Test App", mock_func)

    assert len(app.apps) == 1
    assert app.apps[0] == {
        "title": "Test App",
        "function": mock_func
    }

@patch("finaltest2.multiapp.st.sidebar")
def test_multiapp_run(mock_sidebar):
    app = MultiApp()
    mock_func = MagicMock()
    app.add_app("Test App", mock_func)

    # Configure selectbox mock to return our app dictionary
    mock_sidebar.selectbox.return_value = app.apps[0]

    app.run()

    # Assert sidebar interactions
    mock_sidebar.image.assert_called_once_with("data/LOGO.png", use_column_width=True)
    mock_sidebar.write.assert_called_once_with("\n# Dashboard\n ")
    mock_sidebar.selectbox.assert_called_once()

    # Verify selectbox call arguments
    args, kwargs = mock_sidebar.selectbox.call_args
    assert args[0] == "Go To"
    assert args[1] == app.apps

    # Test the format_func lambda
    format_func = kwargs['format_func']
    assert format_func(app.apps[0]) == "Test App"

    # Assert that the selected function was called
    mock_func.assert_called_once()
