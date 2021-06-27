"""
The :mod:`mlvizlib.classification` module implements a variety of classification visualizations.
"""

#  from mlvizlib import classification
#  from mlvizlib.classification import _confusion_matrix  # required
#  from mlvizlib.classification._confusion_matrix import confusion_matrix  # used to make this function importable
#  from ._confusion_matrix import confusion_matrix_kalastaja  # used to make this function importable


#__all__ = [
#    "confusion_matrix"
#    ]

# import relevant function (for package users) from the modules (.py) into the subpackages
from .viz_confusion_matrix import confusion_matrix
