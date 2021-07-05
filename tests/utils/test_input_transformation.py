from mlvizlib.utils.input_transformation import numpy_to_list, pandas_to_list
import numpy as np
import pandas as pd


def test_numpy_to_list():
    # test that numpy.ndarray of shape (n_samples,1) is converted into a list of shape (n_samples,)
    assert numpy_to_list(np.array([[0], [1], [2], [3]])) == [0, 1, 2, 3]


def test_pandas_to_list():
    # test that pd.DataFrame of shape (n_samples,1) is converted into a list of shape (n_samples,)
    assert pandas_to_list(pd.DataFrame([8, 2, 3, 5])) == [8, 2, 3, 5]
    # test that pd.Series of shape (n_samples,) is converted into a list of shape (n_samples,)
    assert pandas_to_list(pd.Series([8, 2, 3, 5])) == [8, 2, 3, 5]
    # test that numpy.ndarray doesn't return anything
    assert pandas_to_list(np.array([8, 2, 3, 5])) is None
