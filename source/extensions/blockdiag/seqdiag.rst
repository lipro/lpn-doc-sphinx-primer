:topic: Sequence Diagram

.. index::
   triple: Sphinx; Extension; Sequence Diagram

Sequence Diagram
################

:doc:`bldiag:seqdiag/sphinxcontrib` is a |Sphinx| extension for embedding
sequence diagrams. You can embed sequence diagrams with the :rst:`.. seqdiag::`
directive.

:PyPI Package:   https://pypi.org/project/sphinxcontrib-seqdiag/
:Documentation:  http://blockdiag.com/en/seqdiag/sphinxcontrib.html
:Git Repository: https://github.com/blockdiag/sphinxcontrib-seqdiag

|Sphinx| extension for embedding sequence diagrams using
`seqdiag <https://github.com/blockdiag/seqdiag>`_.

:Features:

   1. Generate sequence-diagram from dot like text (basic feature).
   2. Multilingualism for node-label (utf-8 only).

.. todo:: activate "Sequence Diagram" extension.

Directive Body Diagram
**********************

.. rst:directive:: seqdiag

   For more details, see :doc:`bldiag:seqdiag/sphinxcontrib` in the
   extension demonstration and the :file:`README.rst` in the extension
   Git repository.

   :the example:

      .. literalinclude:: seqdiag-directive-body-example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   .. code-block:: rst

      :which gives:

         .. include:: seqdiag-directive-body-example.rsti

Description Table
*****************

:the example:

   .. literalinclude:: seqdiag-description-table-example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

.. code-block:: rst

   :which gives:

      .. include:: seqdiag-description-table-example.rsti

Include Diagram
***************

:the example:

   .. code-block:: rst
      :linenos:

      .. seqdiag:: seq.diag
         :caption: Style attributes to diagram and edges (Sequence Diagram example)
         :align: center
         :height: 640

.. code-block:: rst

   :which gives:

      .. seqdiag:: seq.diag
         :caption: Style attributes to diagram and edges (Sequence Diagram example)
         :align: center
         :height: 640

:which needs:

   The example above comes from the original
   :ref:`bldiag:seqdiag-sample-diagrams`
   web page and processed the following file content:

   .. literalinclude:: seq.diag
      :caption: Sequence Diagram example file (seq.diag)
      :language: dot
      :linenos:

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
