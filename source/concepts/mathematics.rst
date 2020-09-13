:topic: Mathematics

.. index::
   triple: Sphinx; Syntax; Mathematics

Mathematics
###########

In |Sphinx| you can include inline math :math:`x\leftarrow y\ x\forall y\ x-y`
(as role :rst:`:math:`x\leftarrow y\ x\forall y\ x-y``) or display math as
directive block which is able to cross-referencing equations:

.. math::

   W^{3\beta}_{\delta_1 \rho_1 \sigma_2}
   = U^{3\beta}_{\delta_1 \rho_1}
   + \frac{1}{8 \pi 2} \int^{\alpha_2}_{\alpha_2} d \alpha^\prime_2 \left[
       \frac{
         U^{2\beta}_{\delta_1 \rho_1}
         - \alpha^\prime_2U^{1\beta}_{\rho_1 \sigma_2}
       }{U^{0\beta}_{\rho_1 \sigma_2}}\right
     ]

.. rst:directive:: math

   To include math in your document, just use the :rst:`.. math::` directive.
   For more details, see :rst:dir:`sphinx:math` directive.

   :the example:

      .. literalinclude:: mathematics/simple/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: mathematics/simple/example.rsti

.. rst:role:: math:numref

   The math domain (name **math**) provides the role
   :rst:`:math:numref:`label`` which is for cross-referencing equations
   defined by :rst:`.. math::` directive via their label.
   For more details, see :rst:role:`sphinx:math:numref` role.

   :the example:

      .. literalinclude:: mathematics/label/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: mathematics/label/example.rsti

   When the equation is only one line of text, it can also be given
   as a directive argument (as used in Euler's identity above).
   
.. rst:role:: eq

   The role :rst:`:eq:`euler`` is the same as :rst:`:math:numref:`euler``.
   For more details, see :rst:role:`sphinx:eq` role.

Recent versions of |Sphinx| include built-in support for math.
There are three flavors:

* :py:mod:`sphinx:sphinx.ext.imgmath`: uses dvipng to render the equation
* :py:mod:`sphinx:sphinx.ext.mathjax`: renders the math in the browser using Javascript
* :py:mod:`sphinx:sphinx.ext.jsmath`: it's an older code, but it checks out

Additionally, there are special |Sphinx| extensions provided by
`matplotlib <https://matplotlib.org/>`_ that has its own math
support for writing mathematical expressions and inserting
automatically-generated plots:

* ``matplotlib.sphinxext.mathmpl``
* :py:mod:`mplref:matplotlib.sphinxext.plot_directive`

.. seealso::

   See :doc:`../extensions/matplotlib` for more details
   about the |Sphinx| matplotlib extensions with examples.

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
