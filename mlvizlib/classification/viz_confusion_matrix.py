"""
Confusion Matrix visualization.
"""

# Author: Kristian Bonnici <kristiandaaniel@gmail.fi>

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from ..utils.input_validation import check_consistent_length


class ConfusionMatrixViz:
    """Class for confusion matrix visualization.
    """

    def __init__(self, y_true, y_pred, normalized=False):
        self.y_true = y_true
        self.y_pred = y_pred
        self.normalized = normalized
        if self.normalized is False:
            self.cm = self.construct()
        else:
            self.cm = self.construct()
            self.cm = self.normalize()

    def construct(self):
        check_consistent_length(list(self.y_true), list(self.y_pred))
        data = {'y_true': list(self.y_true),
                'y_pred': list(self.y_pred)}
        df = pd.DataFrame(data, columns=['y_true', 'y_pred'])
        cm = pd.crosstab(df['y_true'], df['y_pred'], rownames=['true'], colnames=['pred']).to_numpy()
        self.normalized = False
        return cm

    def normalize(self):
        self.normalized = True
        return self.cm.astype('float') / self.cm.sum(axis=1)[:, np.newaxis]

    def plot(self,
             *,
             labels=None,
             cmap='magma'
             ):
        plt.imshow(self.cm, cmap=cmap)
        plt.title('Confusion matrix')
        plt.xlabel('Predicted label')
        plt.ylabel('True label')
        if labels is None:
            labels = list(np.unique(list(self.y_true) + list(self.y_pred)))
        tick_marks = np.arange(len(labels))
        plt.xticks(tick_marks, labels)
        plt.yticks(tick_marks, labels)

        # Loop over data dimensions and create text annotations.
        fmt = '.2f' if self.normalized else 'd'
        thresh = self.cm.max() / 2.
        for i in range(self.cm.shape[0]):
            for j in range(self.cm.shape[1]):
                plt.text(j, i, format(self.cm[i, j], fmt), ha="center", va="center",
                         color="white" if self.cm[i, j] < thresh else "black")

        plt.tight_layout()
        plt.colorbar()
        return plt


def confusion_matrix(
    y_true,
    y_pred,
    *,
    normalize=False
):
    cm_object = ConfusionMatrixViz(y_true, y_pred, normalized=normalize)
    return cm_object.plot()


def confusion_matrix_kalastaja(
    y_true,
    y_pred,
    *,
    normalize=True
):
    cm_object = ConfusionMatrixViz(y_true, y_pred, normalized=normalize)
    return cm_object.plot()
