"""
Confusion Matrix visualization.
"""

# Author: Kristian Bonnici <kristiandaaniel@gmail.fi>

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from ..utils.input_validation import check_consistent_length
from ..utils.input_validation import check_array_type_support
from ..utils.input_transformation import numpy_to_list
from ..utils.input_transformation import pandas_to_list


class ConfusionMatrixViz:
    """Class for confusion matrix visualization.

    It is recommended to use confusion_matrix to create a ConfusionMatrixViz object.
    """

    def __init__(self, y_true, y_pred, normalized=False, cmap='RdPu', colorbar=True):
        self.y_true = y_true
        self.y_pred = y_pred
        self.normalized = normalized
        if self.normalized is False:
            self.cm = self.construct()
        else:
            self.cm = self.construct()
            self.cm = self.normalize()
        self.cmap = cmap
        self.colorbar = colorbar

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
             labels_fontsize=12,
             xticks_rotation='horizontal',
             ):
        """

        Parameters
        ----------
        * :

        labels :
             (Default value = None)

        labels_fontsize :
             (Default value = 12)

        xticks_rotation :
             (Default value = 'horizontal')

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
        plt.xlabel('Predicted label', fontsize=labels_fontsize)
        plt.ylabel('True label', fontsize=labels_fontsize)
        if labels is None:
            labels = list(np.unique(list(self.y_true) + list(self.y_pred)))
        tick_marks = np.arange(len(labels))
        plt.xticks(tick_marks, labels, fontsize=labels_fontsize, rotation=xticks_rotation)
        plt.yticks(tick_marks, labels, fontsize=labels_fontsize)

        # Loop over data dimensions and create text annotations.
        thresh = self.cm.max() / 2.
        for i in range(self.cm.shape[0]):
            for j in range(self.cm.shape[1]):
                plt.text(j, i, format(self.cm[i, j], fmt), ha="center", va="center",
                         color="white" if self.cm[i, j] > thresh else "black")

        if self.colorbar is True:
            plt.colorbar(fraction=0.046, pad=0.04)
        plt.tight_layout()
        return plt


def confusion_matrix(
    y_true,
    y_pred,
    *,
    base_norm_both='both',
    labels=None,
    labels_fontsize=12,
    xticks_rotation='horizontal',
    cmap='RdPu',
    figsize=(10, 5),
    colorbar=True
):
    """Plot Confusion Matrix.

    Parameters
    ----------
    y_true : array-like list, numpy.ndarray, pandas.core.frame.DataFrame, or pandas.core.series.Series of shape
             (n_samples,) or (n_samples,1)
        True values.

    y_pred : array-like list, numpy.ndarray, pandas.core.frame.DataFrame, or pandas.core.series.Series of shape
             (n_samples,) or (n_samples,1)
        Predicted values.

    labels : list of shape (n_classes,), default=None
        Label names used for plotting.

    labels_fontsize : float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}, default=12
        Fontsize for the labels. If float, the fontsize in points. The string values denote sizes relative to the
        default font size.

    xticks_rotation : {'vertical', 'horizontal'} or float, default='horizontal'
        Rotation of xticks labels in degrees.

    base_norm_both : {'base', 'norm', 'both'}, default='both'
        - if `'base'`, the displayed confusion matrix is not normalized;
        - if `'norm'`, the displayed confusion matrix is normalized over the true conditions;
        - if `'both'`, both, the 'base' and 'norm' matrices are displayed;

    cmap : str or matplotlib Colormap, default='YlGn'
        Colormap recognized by matplotlib.

    figsize : (float, float), default=(10, 5)
        Width, height in inches.

    colorbar : bool, default=True
        Includes colorbar on the side of the confusion matrix.

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
    check_array_type_support(y_true)
    check_array_type_support(y_pred)

    # convert y_true to list
    if isinstance(y_true, type(np.array([]))):
        y_true = numpy_to_list(y_true)
    elif isinstance(y_true, type(pd.DataFrame())) or isinstance(y_true, type(pd.Series(dtype=float))):
        y_true = pandas_to_list(y_true)
    elif isinstance(y_true, type(())):
        y_true = list(y_true)
    else:
        pass

    # convert y_pred to list
    if isinstance(y_pred, type(np.array([]))):
        y_pred = numpy_to_list(y_pred)
    elif isinstance(y_pred, type(pd.DataFrame())) or isinstance(y_pred, type(pd.Series(dtype=float))):
        y_pred = pandas_to_list(y_pred)
    elif isinstance(y_pred, type(())):
        y_pred = list(y_pred)
    else:
        pass

    # display setup
    if base_norm_both == 'both':
        plt.figure(figsize=figsize)
        plt.subplot(121)
        ConfusionMatrixViz(y_true, y_pred, normalized=False,
                           cmap=cmap, colorbar=colorbar).plot(labels=labels,
                                                              xticks_rotation=xticks_rotation,
                                                              labels_fontsize=labels_fontsize)
        plt.subplot(122)
        ConfusionMatrixViz(y_true, y_pred, normalized=True,
                           cmap=cmap, colorbar=colorbar).plot(labels=labels,
                                                              xticks_rotation=xticks_rotation,
                                                              labels_fontsize=labels_fontsize)
        plt.tight_layout()
        return plt
    elif base_norm_both == 'base':
        cm_object = ConfusionMatrixViz(y_true, y_pred, normalized=False, cmap=cmap, colorbar=colorbar)
        plt.figure(figsize=figsize)
        return cm_object.plot(labels=labels, xticks_rotation=xticks_rotation, labels_fontsize=labels_fontsize)
    elif base_norm_both == 'norm':
        cm_object = ConfusionMatrixViz(y_true, y_pred, normalized=True, cmap=cmap, colorbar=colorbar)
        plt.figure(figsize=figsize)
        return cm_object.plot(labels=labels, xticks_rotation=xticks_rotation, labels_fontsize=labels_fontsize)
