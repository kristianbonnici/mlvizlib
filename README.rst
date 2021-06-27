========
mlvizlib
========


.. image:: https://img.shields.io/pypi/v/mlvizlib.svg
        :target: https://pypi.python.org/pypi/mlvizlib

.. image:: https://img.shields.io/travis/kristianbonnici/mlvizlib.svg
        :target: https://travis-ci.com/kristianbonnici/mlvizlib

.. image:: https://readthedocs.org/projects/mlvizlib/badge/?version=latest
        :target: https://mlvizlib.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




**MLVizLib (Machine Learning Visualization Library)** is a powerful package for generating quick, insightful, and stylish visualizations for machine learning (ML). The main goal is to enhance the ML workflow by providing insightful visualizations with minimum effort.

* Free software: MIT license
* Documentation: (COMING SOON) https://mlvizlib.readthedocs.io.

Install
--------
MLVizLib can be installed from PyPI_:

.. _PyPI: https://pypi.org/project/mlvizlib/

.. code-block:: python

   pip install mlvizlib

Features
--------

* Confusion Matrix Visualization

.. note::  More coming soon.

Confusion Matrix Visualization example
--------------------------------------

.. code-block:: python

   import matplotlib.pyplot as plt
   from mlvizlib.classification import confusion_matrix

   eg_y_true = [1,0,0,0,1,1,0,0,0,1,1,0]  # example y_true values
   eg_y_pred = [0,0,0,0,1,1,1,0,0,0,1,0]  # example y_pred values

   confusion_matrix(eg_y_true, eg_y_pred)
   plt.show()

Credits
-------

This package was initiated with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
