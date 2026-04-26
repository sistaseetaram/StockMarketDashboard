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
