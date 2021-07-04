"""
The :mod:`mlvizlib.classification` module implements a variety of classification visualizations.
"""

__all__ = [
    "confusion_matrix"
    ]

# import relevant function (for package users) from the modules (.py) into the subpackages
from .viz_confusion_matrix import confusion_matrix
