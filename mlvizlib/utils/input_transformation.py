"""Utilities for input transformation"""

# Authors: Kristian Bonnici

import numpy as np
import pandas as pd


def numpy_to_list(array):
    """Converts NumPy array into a list of shape (n_samples,).

        Parameters
        ----------
        array : numpy.ndarray of shape (n_samples,) or (n_samples,1)
            NumPy array that will be converted into a list.

        Returns
        -------
        list
        """
    return list(array.reshape(-1, 1).reshape(1, -1)[0])


def pandas_to_list(array):
    """Converts Pandas Series or DataFrame into a list of shape (n_samples,).

        Parameters
        ----------
        array : pandas.core.frame.DataFrame of shape (n_samples,1), or pandas.core.series.Series of shape (n_samples,)
            Pandas Series or DataFrame that will be converted into a list.

        Returns
        -------
        list
        """
    if isinstance(array, type(pd.DataFrame())):
        return list(array.values.reshape(-1, 1).reshape(1, -1)[0])
    elif isinstance(array, type(pd.Series(dtype=float))):
        return list(array)
