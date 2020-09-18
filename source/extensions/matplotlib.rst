:topic: Mathematical Plots

.. index::
   triple: Sphinx; Extension; Mathematical Plots

Mathematical Plots
##################

.. pull-quote::

   .. attention::

      Matplotlib does not support labels and auto-references. You
      can not refer to a equation and you will never see an entry
      in the list of equations to :rst:`.. mathmpl::` expressions.

      Only practicable and usable for |HTML|/|EPUB| and |LaTeX|/|PDF|
      builder.


      .. admonition:: Extension not applicable for textual output
         :class: danger

         The intended use of this |Sphinx| extension is for output
         systems with graphical support, not for pure text based
         systems like man or info pages. That is why many of the
         rendering functions are implemented exclusively for |HTML|
         or |LaTeX| output.

:PyPI Package:   https://pypi.org/project/matplotlib/
:Project Home:   https://matplotlib.org/
:Documentation:  https://matplotlib.org/contents.html
:Git Repository: https://github.com/matplotlib/matplotlib

:Documentation:  https://matplotlib.org/sampledoc/index.html
:Git Repository: https://github.com/matplotlib/sampledoc

Matplotlib is a comprehensive library for creating static, animated, and
interactive visualizations in |Python|. It consists:

* ``matplotlib.sphinxext.mathmpl``: Matplotlib math-text in a |Sphinx| document
* :py:mod:`mplref:matplotlib.sphinxext.plot_directive`:
  Matplotlib plot in a |Sphinx| document

.. rubric:: Runtime setup

.. confval:: plot_pre_code

   Code that should be executed before each plot runs will setup over the
   |Sphinx| configuration option :confval:`plot_pre_code`. If not specified
   or **None or empty** it will default to a string containing:
   :python:`import numpy as np; from matplotlib import pyplot as plt;`.

   .. ifconfig:: not plot_pre_code

      :plot_pre_code: **None or empty**, use extension's default.

   .. ifconfig:: plot_pre_code

      :plot_pre_code: Currently set to:

                      .. literalinclude:: {plot_preincl}
                         :language: python
                         :start-after: START: LDSP
                         :end-before: END: LDSP
                         :linenos:

.. confval:: plot_working_directory

   By default, if **None or empty**, the :confval:`plot_working_directory` will
   be changed to the directory of the example, so the code can get at its data
   files, if any. Also its path will be added to :python:`sys.path` so it can
   import any helper modules sitting beside it. This configuration option can
   be used to specify a central directory (also added to :python:`sys.path`)
   where data files and helper modules for all code are located.

   .. ifconfig:: not plot_basedir

      :plot_working_directory: **None or empty**, directory is **relative**.

   .. ifconfig:: plot_basedir

      :plot_working_directory: Currently set to :file:`{plot_workdir}`.

.. confval:: plot_basedir

   When a path to a source file is given, the |Sphinx| configuration option
   :confval:`plot_basedir` will respect. It is the base directory, to which
   :rst:`.. plot::` file names are relative to. If **None or empty**, file
   names are **relative** to the directory where the file containing the
   directive is.

   .. ifconfig:: not plot_basedir

      :plot_basedir: **None or empty**, file names are **relative**.

   .. ifconfig:: plot_basedir

      :plot_basedir: Currently set to :file:`{plot_basedir}`.

Expressions
***********

See the :doc:`mplref:tutorials/text/mathtext` for lots more information
how to writing mathematical expressions in matplotlib.

With matplotlib in |Sphinx| you can include inline math
:mathmpl:`(\alpha^{ic} > \beta_{ic})` (as role
:rst:`:mathmpl:`(\alpha^{ic} > \beta_{ic})``) or display math:

.. mathmpl::

   \sum_{i=0}^\infty x_i

.. rst:directive:: mathmpl

   :the example:

      .. literalinclude:: matplotlib/mathmpl/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: matplotlib/mathmpl/example.rsti

:raw-latex:`\clearpage\phantomsection`

Plots
*****

.. rst:directive:: plot

   See the matplotlib :doc:`mplref:tutorials/introductory/pyplot` and the
   :doc:`mplref:gallery/index` for lots of examples of matplotlib plots.

The source code for the plot may be included in one of three ways:

.. rubric:: inline content

:the example:

   .. literalinclude:: matplotlib/inline/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: matplotlib/inline/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. rubric:: doctest content

:the example:

   .. literalinclude:: matplotlib/doctest/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: matplotlib/doctest/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. rubric:: source file content

:the example:

   .. literalinclude:: matplotlib/srcfile/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: matplotlib/srcfile/example.rsti

:raw-latex:`\clearpage\phantomsection`

3D-Plots
========

See :doc:`mplref:api/toolkits/mplot3d/index`,
:doc:`mplref:api/toolkits/mplot3d/faq`, and
:doc:`mplref:api/toolkits/mplot3d`.

:the example:

   .. literalinclude:: matplotlib/mplot3d/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: matplotlib/mplot3d/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
