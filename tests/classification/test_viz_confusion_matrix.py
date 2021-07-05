from mlvizlib.classification.viz_confusion_matrix import ConfusionMatrixViz, confusion_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_confusionmatrixviz():
    # test that the confusion matrix is constructed correctly
    assert np.array_equal(ConfusionMatrixViz(y_true=[0, 0, 0, 0, 1], y_pred=[0, 0, 0, 1, 1]).cm,
                          np.array([[3, 1], [0, 1]])) is True

    # test that the normalized confusion matrix is constructed correctly
    assert np.array_equal(ConfusionMatrixViz(y_true=[0, 0, 0, 0, 1], y_pred=[0, 0, 0, 1, 1], normalized=True).cm,
                          np.array([[0.75, 0.25], [0., 1.]])) is True


def test_confusion_matrix():
    # test that confusion_matrix(list, list) returns plt without errors
    assert confusion_matrix([0, 0, 1, 0], [0, 1, 1, 0]) == plt
    # test that confusion_matrix(np.array, np.array) returns plt without errors
    assert confusion_matrix(np.array([0, 0, 1, 0]), np.array([0, 1, 1, 0])) == plt
    # test that confusion_matrix(pd.DataFrame, pd.Series) returns plt without errors
    assert confusion_matrix(pd.DataFrame([0, 0, 1, 0]), pd.Series([0, 1, 1, 0])) == plt
    # test that confusion_matrix(tuple, tuple) returns plt without errors
    assert confusion_matrix((0, 0, 1, 0), (0, 1, 1, 0)) == plt

    # test that confusion_matrix(base_norm_both='base') returns plt without errors
    assert confusion_matrix([0, 0, 1, 0], [0, 1, 1, 0], base_norm_both='base') == plt
    # test that confusion_matrix(base_norm_both='norm') returns plt without errors
    assert confusion_matrix([0, 0, 1, 0], [0, 1, 1, 0], base_norm_both='norm') == plt
