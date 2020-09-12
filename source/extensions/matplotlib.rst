:topic: Mathematical Plots

.. index::
   triple: Sphinx; Extension; Mathematical Plots

Mathematical Plots
##################

.. attention::

   Matplotlib does not support labels and auto-references. You can not refer
   to a equation and you will never see an entry to :rst:`.. mathmpl::`
   expressions in the list of equations.

:PyPI Package:   https://pypi.org/project/matplotlib/
:Project Home:   https://matplotlib.org/
:Documentation:  https://matplotlib.org/contents.html
:Git Repository: https://github.com/matplotlib/matplotlib

:Documentation:  https://matplotlib.org/sampledoc/index.html
:Git Repository: https://github.com/matplotlib/sampledoc

Matplotlib is a comprehensive library for creating static, animated, and
interactive visualizations in Python. It consists:

* ``matplotlib.sphinxext.mathmpl``: Matplotlib math-text in a |Sphinx| document
* :py:mod:`mplref:matplotlib.sphinxext.plot_directive`:
  Matplotlib plot in a |Sphinx| document

.. todo:: activate "Mathematical Plots" extension.

Expressions
***********

See the :doc:`mplref:tutorials/text/mathtext` for lots more information
how to writing mathematical expressions in matplotlib.

.. code-block:: rst

   With matplotlib in |Sphinx| you can include inline math
   :mathmpl:`(\alpha^{ic} > \beta_{ic})` (as role
   :rst:`:mathmpl:`(\alpha^{ic} > \beta_{ic})``) or display math:

   .. mathmpl::

      \sum_{i=0}^\infty x_i

.. rst:directive:: mathmpl

   :the example:

      .. literalinclude:: matplotlib-mathmpl-example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   .. code-block:: rst

      :which gives:

         .. include:: matplotlib-mathmpl-example.rsti

Plots
*****

.. rst:directive:: plot

   See the matplotlib :doc:`mplref:tutorials/introductory/pyplot` and the
   :doc:`mplref:gallery/index` for lots of examples of matplotlib plots.

The source code for the plot may be included in one of three ways:

:raw-latex:`\clearpage\phantomsection`

.. rubric:: inline content

:the example:

   .. literalinclude:: matplotlib-inline-example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

.. code-block:: rst

   :which gives:

      .. include:: matplotlib-inline-example.rsti

:raw-latex:`\clearpage\phantomsection`

.. rubric:: doctest content

:the example:

   .. literalinclude:: matplotlib-doctest-example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

.. code-block:: rst

   :which gives:

      .. include:: matplotlib-doctest-example.rsti

:raw-latex:`\clearpage\phantomsection`

.. rubric:: source file content

When a path to a source file is given, the |Sphinx| configuration option
``plot_basedir`` will respect. It is the base directory, to which
:rst:`.. plot::` file names are relative to. If **None or empty**, file names
are **relative** to the directory where the file containing the directive is.

.. code-block:: rst

   .. ifconfig:: not plot_basedir

      :plot_basedir: **None or empty**, file names are **relative**

   .. ifconfig:: plot_basedir

      :plot_basedir: currently set to :file:`{plot_basedir}`.

:the example:

   .. literalinclude:: matplotlib-srcfile-example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

.. code-block:: rst

   :which gives:

      .. include:: matplotlib-srcfile-example.rsti

:raw-latex:`\clearpage\phantomsection`

3D-Plots
========

See :doc:`mplref:api/toolkits/mplot3d/index`,
:doc:`mplref:api/toolkits/mplot3d/faq`, and
:doc:`mplref:api/toolkits/mplot3d`.

:the example:

   .. literalinclude:: matplotlib-mplot3d-example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

.. code-block:: rst

   :which gives:

      .. include:: matplotlib-mplot3d-example.rsti

.. :raw-latex:`\clearpage\phantomsection`

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
