import pytest
import pandas as pd
import numpy as np

from finaltest2.apps.financeDashboard import getMACD, getRSI

def test_getMACD_default_column():
    """Test getMACD with default 'Adj Close' column."""
    # Create a dummy dataframe with 'Adj Close'
    # We use enough rows to allow EWMA calculations to settle, although even 10 is fine
    data = {
        'Adj Close': [100, 102, 104, 103, 101, 99, 98, 97, 100, 105, 110, 115, 120, 118, 115, 112, 110, 108, 105, 102, 100, 98, 95, 90, 85, 80]
    }
    df = pd.DataFrame(data)

    # Apply getMACD
    result_df = getMACD(df.copy())

    # Check if new columns were added
    assert 'EMA12' in result_df.columns
    assert 'EMA26' in result_df.columns
    assert 'MACD' in result_df.columns
    assert 'Signal' in result_df.columns
    assert 'Histogram' in result_df.columns

    # Verify MACD calculation: MACD = EMA12 - EMA26
    np.testing.assert_allclose(
        result_df['MACD'],
        result_df['EMA12'] - result_df['EMA26'],
        rtol=1e-5
    )

    # Verify Histogram calculation: Histogram = MACD - Signal
    np.testing.assert_allclose(
        result_df['Histogram'],
        result_df['MACD'] - result_df['Signal'],
        rtol=1e-5
    )

    # Verify the initial values based on pandas EWMA adjust=False
    # EMA for t=0 is just the value itself
    assert result_df['EMA12'].iloc[0] == 100
    assert result_df['EMA26'].iloc[0] == 100
    assert result_df['MACD'].iloc[0] == 0
    assert result_df['Signal'].iloc[0] == 0
    assert result_df['Histogram'].iloc[0] == 0

def test_getMACD_custom_column():
    """Test getMACD with a custom column name."""
    data = {
        'Close': [50, 52, 54, 53, 51, 49, 48, 47, 50, 55, 60, 65, 70, 68, 65, 62, 60, 58, 55, 52, 50, 48, 45, 40, 35, 30]
    }
    df = pd.DataFrame(data)

    # Apply getMACD using 'Close' column
    result_df = getMACD(df.copy(), column='Close')

    # Check if new columns were added
    assert 'EMA12' in result_df.columns
    assert 'EMA26' in result_df.columns
    assert 'MACD' in result_df.columns
    assert 'Signal' in result_df.columns
    assert 'Histogram' in result_df.columns

    # Verify calculation logic is sound
    np.testing.assert_allclose(
        result_df['MACD'],
        result_df['EMA12'] - result_df['EMA26'],
        rtol=1e-5
    )
    np.testing.assert_allclose(
        result_df['Histogram'],
        result_df['MACD'] - result_df['Signal'],
        rtol=1e-5
    )

def test_getMACD_empty_dataframe():
    """Test getMACD with an empty dataframe."""
    df = pd.DataFrame({'Adj Close': []})
    result_df = getMACD(df.copy())

    assert len(result_df) == 0
    assert 'EMA12' in result_df.columns
    assert 'EMA26' in result_df.columns
    assert 'MACD' in result_df.columns
    assert 'Signal' in result_df.columns
    assert 'Histogram' in result_df.columns


def test_getRSI_default_column():
    """Test getRSI with default 'Adj Close' column and default time."""
    data = {
        'Adj Close': [100, 102, 104, 103, 101, 99, 98, 97, 100, 105, 110, 115, 120, 118, 115, 112, 110, 108, 105, 102, 100, 98, 95, 90, 85, 80]
    }
    df = pd.DataFrame(data)

    # Apply getRSI
    result_df = getRSI(df.copy())

    # Check if 'RSI' column was added
    assert 'RSI' in result_df.columns
    assert len(result_df) == len(df)

    # RSI values should be between 0 and 100 or NaN
    valid_rsi = result_df['RSI'].dropna()
    assert all(valid_rsi >= 0)
    assert all(valid_rsi <= 100)
    assert len(valid_rsi) > 0


def test_getRSI_custom_params():
    """Test getRSI with custom column and time period."""
    data = {
        'Close': [10, 11, 12, 11, 10, 11, 12, 13, 14, 15]
    }
    df = pd.DataFrame(data)
    time_period = 5

    # Apply getRSI
    result_df = getRSI(df.copy(), column='Close', time=time_period)

    assert 'RSI' in result_df.columns
    # Check that we have some non-NaN values
    assert result_df['RSI'].notnull().any()


def test_getRSI_empty_dataframe():
    """Test getRSI with an empty dataframe."""
    df = pd.DataFrame({'Adj Close': []})
    result_df = getRSI(df.copy())

    assert len(result_df) == 0
    assert 'RSI' in result_df.columns


def test_getRSI_constant_values():
    """Test getRSI with constant price values."""
    df = pd.DataFrame({'Adj Close': [100] * 20})
    result_df = getRSI(df.copy())

    # Since there's no change, upChange and downChange are 0.
    # RSI should be NaN (because RS = 0/0 = NaN)
    assert result_df['RSI'].isna().all()


def test_getRSI_only_up():
    """Test getRSI with strictly increasing price values."""
    df = pd.DataFrame({'Adj Close': range(100, 130)})
    result_df = getRSI(df.copy())

    # After initial period, RSI should be 100
    valid_rsi = result_df['RSI'].dropna()
    np.testing.assert_allclose(valid_rsi, 100.0)


def test_getRSI_only_down():
    """Test getRSI with strictly decreasing price values."""
    df = pd.DataFrame({'Adj Close': range(130, 100, -1)})
    result_df = getRSI(df.copy())

    # After initial period, RSI should be 0
    valid_rsi = result_df['RSI'].dropna()
    np.testing.assert_allclose(valid_rsi, 0.0, atol=1e-7)
