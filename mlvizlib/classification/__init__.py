"""
The :mod:`mlvizlib.classification` module implements a variety of classification visualizations.
"""

from ._confusion_matrix import confusion_matrix

from ..utils import input_validation

__all__ = [
    "confusion_matrix"
    ]
