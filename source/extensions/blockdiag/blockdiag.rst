:topic: Block Diagram

.. index::
   triple: Sphinx; Extension; Block Diagram

Block Diagram
#############

:doc:`bldiag:blockdiag/sphinxcontrib` is a Sphinx extension for embedding
block diagrams. You can embed block diagrams with the :rst:`.. blockdiag::`
directive.

:PyPI Package:   https://pypi.org/project/sphinxcontrib-blockdiag/
:Documentation:  http://blockdiag.com/en/blockdiag/sphinxcontrib.html
:Git Repository: https://github.com/blockdiag/sphinxcontrib-blockdiag

Sphinx extension for embedding block diagrams using
`blockdiag <https://github.com/blockdiag/blockdiag>`_.

:Features:

   1. Generate block-diagram from dot like text (basic feature).
   2. Multilingualism for node-label (utf-8 only).

.. todo:: activate "Block Diagram" extension.

Directive Body Diagram
**********************

.. rst:directive:: blockdiag

   For more details, see :doc:`bldiag:blockdiag/sphinxcontrib` in the
   extension demonstration and the :file:`README.rst` in the extension
   Git repository.

   :the example:

      .. literalinclude:: blockdiag-directive-body-example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   .. code-block:: rst

      :which gives:

         .. include:: blockdiag-directive-body-example.rsti

Description Table
*****************

:the example:

   .. literalinclude:: blockdiag-description-table-example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

.. code-block:: rst

   :which gives:

      .. include:: blockdiag-description-table-example.rsti

Include Diagram
***************

:the example:

   .. code-block:: rst
      :linenos:

      .. blockdiag:: block.diag
         :caption: Style attributes to nodes and edges (Block Diagram example)
         :align: center
         :width: 640

.. code-block:: rst

   :which gives:

      .. blockdiag:: block.diag
         :caption: Style attributes to nodes and edges (Block Diagram example)
         :align: center
         :width: 640

:which needs:

   The example above comes from the original
   :ref:`bldiag:blockdiag-sample-diagrams`
   web page and processed the following file content:

   .. literalinclude:: block.diag
      :caption: Block Diagram example file (block.diag)
      :language: dot
      :linenos:

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
