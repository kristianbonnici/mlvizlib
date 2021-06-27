[![Sports fonts](https://see.fontimg.com/api/renderfont4/AwO6/eyJyIjoiZnMiLCJoIjoxMzUsInciOjEwMDAsImZzIjoxMzUsImZnYyI6IiNCRjFBQUMiLCJiZ2MiOiIjQkYyMTIxIiwidCI6MX0/W01MXVZpekxpYg/sportrop-regular.png)](https://www.fontspace.com/category/sports)

--------------------------------------

![PyPI Version](https://img.shields.io/pypi/v/mlvizlib)
![License](https://img.shields.io/pypi/l/mlvizlib)

**MLVizLib (Machine Learning Visualization Library)** is a powerful
library for generating quick, insightful, and stylish visualizations for
machine learning (ML). Our goal is to enhance the ML workflow by
providing insightful visualizations with minimum effort.

-   Documentation: (COMING SOON) <https://mlvizlib.readthedocs.io>.

<div class="alert alert-block alert-danger">
<b>NOTE:</b> This project is in early stage development, and can thus go trough major changes.
</div>

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

eg_y_true = [1,0,0,0,1,1,0,0,0,1,1,0]  # example y_true values
eg_y_pred = [0,0,0,0,1,1,1,0,0,0,1,0]  # example y_pred values

confusion_matrix(eg_y_true, eg_y_pred)
plt.show()
```

