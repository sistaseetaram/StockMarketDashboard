import pytest
from unittest.mock import patch, MagicMock

from finaltest2.multiapp import MultiApp

def test_multiapp_init():
    app = MultiApp()
    assert app.apps == []

def test_multiapp_add_app():
    app = MultiApp()

    mock_func = MagicMock()
    app.add_app("Test Title", mock_func)

    assert len(app.apps) == 1
    assert app.apps[0]["title"] == "Test Title"
    assert app.apps[0]["function"] == mock_func

@patch("finaltest2.multiapp.st.sidebar")
def test_multiapp_run(mock_sidebar):
    app = MultiApp()

    mock_func1 = MagicMock()
    mock_func2 = MagicMock()

    app.add_app("App 1", mock_func1)
    app.add_app("App 2", mock_func2)

    # Mock the selectbox to return the dictionary for "App 2"
    mock_sidebar.selectbox.return_value = app.apps[1]

    app.run()

    # Check that the sidebar components were called correctly
    mock_sidebar.image.assert_called_once_with("data/LOGO.png", use_column_width=True)
    mock_sidebar.write.assert_called_once_with("\n# Dashboard\n ")

    # Check selectbox call
    # The format_func is passed as a kwarg, we can extract it to verify if needed,
    # but asserting it was called with the right general arguments is sufficient.
    mock_sidebar.selectbox.assert_called_once()
    args, kwargs = mock_sidebar.selectbox.call_args
    assert args[0] == "Go To"
    assert args[1] == app.apps
    assert "format_func" in kwargs

    # Verify the selected app's function was called
    mock_func1.assert_not_called()
    mock_func2.assert_called_once()
