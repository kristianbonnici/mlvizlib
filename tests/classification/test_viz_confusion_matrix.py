from mlvizlib.classification.viz_confusion_matrix import ConfusionMatrixViz
import numpy as np


def test_confusionmatrixviz():
    # test that the confusion matrix is constructed correctly
    assert np.array_equal(ConfusionMatrixViz(y_true=[0, 0, 0, 0, 1], y_pred=[0, 0, 0, 1, 1]).cm,
                          np.array([[3, 1], [0, 1]])) is True
