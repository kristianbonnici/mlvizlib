"""Utilities for input validation"""

# Authors: Kristian Bonnici

import numpy as np


def check_consistent_length(*lists):
    """Check that all lists have consistent lengths.

    Parameters
    ----------
    *lists : list of input objects.
        Objects that will be checked for consistent length.
    """

    lengths = [len(l) for l in lists]  # noqa: E741
    unique_lengths = np.unique(lengths)

    print(unique_lengths)
    print("pit", len(unique_lengths))

    if len(unique_lengths) != 1:
        raise ValueError(
            "Found input variables with inconsistent numbers of"
            " samples: %r" % [int(l) for l in lengths]  # noqa: E741
        )
