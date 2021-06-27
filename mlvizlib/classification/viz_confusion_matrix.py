"""
Confusion Matrix visualization.
"""

# Author: Kristian Bonnici <kristiandaaniel@gmail.fi>

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from ..utils.input_validation import check_consistent_length


class ConfusionMatrixViz:
    """Class for confusion matrix visualization."""

    def __init__(self, y_true, y_pred, normalized=False, cmap='YlGn'):
        self.y_true = y_true
        self.y_pred = y_pred
        self.normalized = normalized
        if self.normalized is False:
            self.cm = self.construct()
        else:
            self.cm = self.construct()
            self.cm = self.normalize()
        self.cmap = cmap

    def construct(self):
        """ """
        check_consistent_length(list(self.y_true), list(self.y_pred))
        data = {'y_true': list(self.y_true),
                'y_pred': list(self.y_pred)}
        df = pd.DataFrame(data, columns=['y_true', 'y_pred'])
        cm = pd.crosstab(df['y_true'], df['y_pred'], rownames=['true'], colnames=['pred']).to_numpy()
        self.normalized = False
        return cm

    def normalize(self):
        """ """
        self.normalized = True
        return self.cm.astype('float') / self.cm.sum(axis=1)[:, np.newaxis]

    def plot(self,
             *,
             labels=None,
             ):
        """

        Parameters
        ----------
        * :

        labels :
             (Default value = None)

        Returns
        -------

        """
        plt.imshow(self.cm, cmap=self.cmap)
        if self.normalized is False:
            plt.title('Confusion matrix, without normalization')
            fmt = 'd'
        else:
            plt.title('Normalized confusion matrix')
            fmt = '.2f'
        plt.xlabel('Predicted label')
        plt.ylabel('True label')
        if labels is None:
            labels = list(np.unique(list(self.y_true) + list(self.y_pred)))
        tick_marks = np.arange(len(labels))
        plt.xticks(tick_marks, labels)
        plt.yticks(tick_marks, labels)

        # Loop over data dimensions and create text annotations.
        thresh = self.cm.max() / 2.
        for i in range(self.cm.shape[0]):
            for j in range(self.cm.shape[1]):
                plt.text(j, i, format(self.cm[i, j], fmt), ha="center", va="center",
                         color="white" if self.cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.colorbar()
        return plt


def confusion_matrix(
    y_true,
    y_pred,
    *,
    base_norm_both='both',
    cmap='YlGn',
    figsize=(13, 6)
):
    """Plot Confusion Matrix.

    Parameters
    ----------
    y_true : list
        True values.

    y_pred : list
        Predicted values.

    base_norm_both : {'base', 'norm', 'both'}, default='both'
        - if `'base'`, the displayed confusion matrix is not normalized;
        - if `'norm'`, the displayed confusion matrix is normalized over the true conditions;
        - if `'both'`, both, the 'base' and 'norm' matrices are displayed;

    cmap : str or matplotlib Colormap, default='YlGn'
        Colormap recognized by matplotlib.

    figsize : (float, float), default=(13, 6)
        Width, height in inches.

    Returns
    -------
    display : :class:`~mlvizlib.classification.ConfusionMatrixViz`

    Examples
    --------
    >> import matplotlib.pyplot as plt
    >> from mlvizlib.classification import confusion_matrix
    >>
    >> eg_y_true = [1,0,0,0,1,1,0,0,0,1,1,0]  # example y_true values
    >> eg_y_pred = [0,0,0,0,1,1,1,0,0,0,1,0]  # example y_pred values
    >>
    >> confusion_matrix(eg_y_true, eg_y_pred)
    >> plt.show()
    """
    if base_norm_both == 'both':
        plt.figure(figsize=figsize)
        plt.subplot(121)
        ConfusionMatrixViz(y_true, y_pred, normalized=False, cmap=cmap).plot()
        plt.subplot(122)
        ConfusionMatrixViz(y_true, y_pred, normalized=True, cmap=cmap).plot()
        plt.tight_layout()
        return plt
    elif base_norm_both == 'base':
        cm_object = ConfusionMatrixViz(y_true, y_pred, normalized=False, cmap=cmap)
        plt.figure(figsize=figsize)
        return cm_object.plot()
    elif base_norm_both == 'norm':
        cm_object = ConfusionMatrixViz(y_true, y_pred, normalized=True, cmap=cmap)
        plt.figure(figsize=figsize)
        return cm_object.plot()
