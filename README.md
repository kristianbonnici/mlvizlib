[![Fancy fonts](https://see.fontimg.com/api/renderfont4/YzqJL/eyJyIjoiZHciLCJoIjoxMTcsInciOjEwMDAsImZzIjoxMTcsImZnYyI6IiMyMUJDQzUiLCJiZ2MiOiIjRkZGRkZGIn0/W01MXSBWaXogTGli/broshk-plum.png)](https://www.fontspace.com/category/fancy)

--------------------------------------

![PyPI Version](https://img.shields.io/pypi/v/mlvizlib)
![License](https://img.shields.io/pypi/l/mlvizlib)
[![codecov](https://codecov.io/gh/kristianbonnici/mlvizlib/branch/master/graph/badge.svg?token=UUGYAZMOZU)](https://codecov.io/gh/kristianbonnici/mlvizlib)

**MLVizLib (Machine Learning Visualization Library)** is a powerful
library for generating quick, insightful, and stylish visualizations for
machine learning (ML). Our goal is to enhance the ML workflow by
providing insightful visualizations with minimum effort.

-   Documentation: (COMING SOON) <https://mlvizlib.readthedocs.io>.

> **NOTE**
>
> This project is in early stage development, and can thus go trough major changes.

Install
-------

MLVizLib can be installed from
[PyPI](https://pypi.org/project/mlvizlib/):

``` {.sourceCode .python}
pip install mlvizlib
```

Features
--------

-   Confusion Matrix Visualization

> **note**
>
> More coming soon.

Confusion Matrix Visualization example
--------------------------------------

``` {.sourceCode .python}
import matplotlib.pyplot as plt
from mlvizlib.classification import confusion_matrix

# example data
y_true = [2,0,1,0,2,0,1,2,0,0,2,0,1,1,0,1,1,0,0,0,0,2,2]
y_pred = [2,0,0,0,2,0,1,2,1,0,2,2,1,1,0,2,1,0,1,0,0,1,2]

confusion_matrix(y_true, y_pred)
plt.show()
```
<p align="center">
  <img src="https://github.com/kristianbonnici/mlvizlib/blob/master/img/example-cm-viz.jpg?raw=true" width="800" />
</p>
