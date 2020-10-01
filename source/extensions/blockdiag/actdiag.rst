:topic: Activity Diagram

.. index::
   triple: Sphinx; Extension; Activity Diagram

Activity Diagram
################

:doc:`bldiag:actdiag/sphinxcontrib` is a |Sphinx| extension for embedding
activity diagrams. You can embed activity diagrams with the :rst:`.. actdiag::``
directive.

:PyPI Package:   https://pypi.org/project/sphinxcontrib-actdiag/
:Documentation:  http://blockdiag.com/en/actdiag/sphinxcontrib.html
:Git Repository: https://github.com/blockdiag/sphinxcontrib-actdiag

|Sphinx| extension for embedding activity diagrams using
`actdiag <https://github.com/blockdiag/actdiag>`_.

:Features:

   1. Generate activity-diagram from dot like text (basic feature).
   2. Multilingualism for node-label (utf-8 only).

:raw-latex:`\clearpage\phantomsection`

Directive Body Diagram
**********************

.. rst:directive:: actdiag

   For more details, see :doc:`bldiag:actdiag/sphinxcontrib` in the
   extension demonstration and the :file:`README.rst` in the extension
   Git repository.

   :the example:

      .. literalinclude:: actdiag/directive-body/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: actdiag/directive-body/example.rsti

:raw-latex:`\clearpage\phantomsection`

Description Table
*****************

:the example:

   .. literalinclude:: actdiag/description-table/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: actdiag/description-table/example.rsti

:raw-latex:`\clearpage\phantomsection`

Include Diagram
***************

:the example:

   .. code-block:: rst
      :linenos:

      .. blockdiag:: actdiag/example.diag
         :caption: Style attributes to frames and nodes (Activity Diagram example)
         :align: center
         :scale: 75
         :width: 480

:which gives:

   .. actdiag:: actdiag/example.diag
      :caption: Style attributes to frames and nodes (Activity Diagram example)
      :align: center
      :scale: 75
      :width: 480

:which needs:

   The example above comes from the original
   :ref:`bldiag:actdiag-sample-diagrams`
   web page and processed the following file content:

   .. literalinclude:: actdiag/example.diag
      :caption: Activity Diagram example file (actdiag/example.diag)
      :language: dot
      :linenos:

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
