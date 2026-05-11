import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from finaltest2.apps.home import parse_Website

@patch('finaltest2.apps.home.requests.get')
def test_parse_Website(mock_get):
    # Mock the HTTP response from requests.get
    mock_response = MagicMock()

    # To avoid pandas FileNotFoundError when reading html strings with read_html without a local file,
    # it is robust to mock the return value of pd.read_html directly.
    mock_response.text = "<html><body><table>...</table></body></html>"
    mock_get.return_value = mock_response

    # We create a dummy dataframe matching the expected HTML table output to simulate what read_html returns.
    # This dummy dataframe includes spaces in columns and the specific columns that should be dropped.
    # Actually read_html returns a list of dataframes. So we return [dummy_df].
    dummy_df = pd.DataFrame({
        'Symbol': ['AAPL', 'MSFT'],
        'Name': ['Apple Inc.', 'Microsoft Corp.'],
        'Price (Intraday)': ['150.00', '280.00'],
        'Change': ['+1.00', '-2.00'],
        '% Change': ['+0.67%', '-0.71%'],
        'Volume': ['50M', '30M'],
        'Avg Vol (3 month)': ['60M', '35M'],
        'Market Cap': ['2T', '2.1T'],
        'PE Ratio (TTM)': ['28.5', '30.2'],
        '52 Week Range': ['130.00 - 180.00', '240.00 - 305.00']
    })

    with patch('finaltest2.apps.home.pd.read_html') as mock_read_html:
        mock_read_html.return_value = [dummy_df]

        # Call the function
        link = "https://finance.yahoo.com/most-active"
        result_df = parse_Website(link)

    # Assert that requests.get was called correctly
    mock_get.assert_called_once_with(link, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)

    # Check the result type
    assert isinstance(result_df, pd.DataFrame)

    # Check that rows were parsed correctly (limited to top 5, but we only have 2 here)
    assert len(result_df) == 2

    # Check that columns were renamed (spaces replaced with underscores)
    assert 'Price_(Intraday)' in result_df.columns
    assert '%_Change' in result_df.columns

    # Check that the specific columns were dropped
    assert '52_Week_Range' not in result_df.columns
    assert 'PE_Ratio_(TTM)' not in result_df.columns

    # Verify a couple of data points
    assert result_df.iloc[0]['Symbol'] == 'AAPL'
    assert result_df.iloc[1]['Symbol'] == 'MSFT'
