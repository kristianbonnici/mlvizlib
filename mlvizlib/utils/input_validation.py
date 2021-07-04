"""Utilities for input validation"""

# Authors: Kristian Bonnici

import numpy as np
import pandas as pd


def check_consistent_length(*lists):
    """Check that all lists have consistent lengths.

    Parameters
    ----------
    *lists : list of input objects.
        Objects that will be checked for consistent length.
    """

    lengths = [len(l) for l in lists]  # noqa: E741
    unique_lengths = np.unique(lengths)

    if len(unique_lengths) != 1:
        raise ValueError(
            "Found input variables with inconsistent numbers of"
            " samples: %r" % [int(l) for l in lengths]  # noqa: E741
        )


def check_array_type_support(array):
    """Check that array-like dtype is one that is supported.

    Currently list, numpy.ndarray, pandas.core.frame.DataFrame, and pandas.core.series.Series are supported.

    Parameters
    ----------
    array : array-like of input objects.
        Objects that will be checked for supported dtype.

    Returns
    -------
    type
    """
    supported_types = [type(list()), type(np.array([])), type(pd.DataFrame()),
                       type(pd.Series(dtype=float)), type(())]

    if array is None:
        raise ValueError(
            "No input array provided for function check_array_type_support."
        )

    elif type(array) in supported_types:
        return type(array)

    else:
        raise TypeError(
            """The provided dtype {} for arrays is not supported. The input array should be in one of the following
            dtypes: {}""".format(
                type(array), supported_types)
        )
