import pandas as pd
import numpy as np
import pytest
from finaltest2.apps.financeDashboard import getMACD

def test_getMACD_creates_columns():
    """Test that getMACD creates the correct columns in the dataframe."""
    # Create a simple dataframe with 50 rows
    df = pd.DataFrame({'Adj Close': np.linspace(10, 100, 50)})

    result_df = getMACD(df)

    # Check if all expected columns are present
    expected_columns = ['Adj Close', 'EMA12', 'EMA26', 'MACD', 'Signal', 'Histogram']
    for col in expected_columns:
        assert col in result_df.columns

def test_getMACD_custom_column():
    """Test that getMACD works with a custom column name."""
    df = pd.DataFrame({'Custom Price': np.linspace(10, 100, 50)})

    result_df = getMACD(df, column='Custom Price')

    # Check if all expected columns are present
    expected_columns = ['Custom Price', 'EMA12', 'EMA26', 'MACD', 'Signal', 'Histogram']
    for col in expected_columns:
        assert col in result_df.columns

def test_getMACD_calculation_values():
    """Test the correctness of the MACD calculations for deterministic inputs."""
    # Constant value array
    df = pd.DataFrame({'Adj Close': np.full(50, 100.0)})

    result_df = getMACD(df)

    # If the price is constant, EMA12 and EMA26 should be the same constant value
    # Therefore, MACD should be 0, Signal should be 0, Histogram should be 0
    assert np.allclose(result_df['EMA12'], 100.0)
    assert np.allclose(result_df['EMA26'], 100.0)
    assert np.allclose(result_df['MACD'], 0.0)
    assert np.allclose(result_df['Signal'], 0.0)
    assert np.allclose(result_df['Histogram'], 0.0)

def test_getMACD_calculation_increasing_values():
    """Test MACD calculations with an increasing sequence."""
    # Linearly increasing values
    df = pd.DataFrame({'Adj Close': np.linspace(10, 60, 50)})

    # Calculate expected EMA values manually for the first few rows
    # EMA = Price(t) * k + EMA(y) * (1-k), where k = 2/(span+1)
    # EMA12: k = 2/13
    # EMA26: k = 2/27

    result_df = getMACD(df)

    # With linearly increasing values, a shorter span EMA (EMA12)
    # reacts faster and should be greater than a longer span EMA (EMA26)
    # So MACD = EMA12 - EMA26 should be positive after the initial value
    assert all(result_df['MACD'].iloc[1:] > 0)

    # Signal is EMA of MACD, so it should lag behind MACD during a steady trend
    # Therefore Histogram = MACD - Signal should also be positive
    assert all(result_df['Histogram'].iloc[1:] > 0)
import pytest
import pandas as pd
import numpy as np

from finaltest2.apps.financeDashboard import getMACD

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
