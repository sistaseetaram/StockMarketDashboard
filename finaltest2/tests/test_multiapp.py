import sys
from unittest.mock import MagicMock, patch
from finaltest2.multiapp import MultiApp

def test_multiapp_init():
    app = MultiApp()
    assert app.apps == []

def test_multiapp_add_app():
    app = MultiApp()
    mock_func = MagicMock()
    app.add_app("Test App", mock_func)

    assert len(app.apps) == 1
    assert app.apps[0]["title"] == "Test App"
    assert app.apps[0]["function"] == mock_func

def test_multiapp_add_multiple_apps():
    app = MultiApp()
    mock_func1 = MagicMock()
    mock_func2 = MagicMock()

    app.add_app("App 1", mock_func1)
    app.add_app("App 2", mock_func2)

    assert len(app.apps) == 2
    assert app.apps[0]["title"] == "App 1"
    assert app.apps[1]["title"] == "App 2"
    assert app.apps[0]["function"] == mock_func1
    assert app.apps[1]["function"] == mock_func2

@patch("streamlit.sidebar.image")
@patch("streamlit.sidebar.write")
@patch("streamlit.sidebar.selectbox")
def test_multiapp_run(mock_selectbox, mock_write, mock_image):
    app = MultiApp()
    mock_func1 = MagicMock()
    mock_func2 = MagicMock()

    app.add_app("App 1", mock_func1)
    app.add_app("App 2", mock_func2)

    # Mock the selectbox to return the dictionary of "App 2"
    mock_selectbox.return_value = app.apps[1]

    app.run()

    # Check that streamlit methods were called
    mock_image.assert_called_once_with("data/LOGO.png", use_column_width=True)
    mock_write.assert_called_once_with("\n# Dashboard\n ")
    mock_selectbox.assert_called_once()

    # The format_func is passed to selectbox, let's verify it works
    _, kwargs = mock_selectbox.call_args
    assert "format_func" in kwargs
    assert kwargs["format_func"](app.apps[0]) == "App 1"

    # Check that the selected function was executed
    mock_func2.assert_called_once()
    mock_func1.assert_not_called()
