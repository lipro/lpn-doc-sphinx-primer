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

.. todo:: activate "Activity Diagram" extension.

Directive Body Diagram
**********************

.. rst:directive:: actdiag

   For more details, see :doc:`bldiag:actdiag/sphinxcontrib` in the
   extension demonstration and the :file:`README.rst` in the extension
   Git repository.

   :the example:

      .. literalinclude:: actdiag-directive-body-example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   .. code-block:: rst

      :which gives:

         .. include:: actdiag-directive-body-example.rsti

Description Table
*****************

:the example:

   .. literalinclude:: actdiag-description-table-example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

.. code-block:: rst

   :which gives:

      .. include:: actdiag-description-table-example.rsti

Include Diagram
***************

:the example:

   .. code-block:: rst
      :linenos:

      .. blockdiag:: act.diag
         :caption: Style attributes to frames and nodes (Activity Diagram example)
         :align: center
         :scale: 75
         :width: 640

.. code-block:: rst

   :which gives:

      .. actdiag:: act.diag
         :caption: Style attributes to frames and nodes (Activity Diagram example)
         :align: center
         :scale: 75
         :width: 640

:which needs:

   The example above comes from the original
   :ref:`bldiag:actdiag-sample-diagrams`
   web page and processed the following file content:

   .. literalinclude:: act.diag
      :caption: Activity Diagram example file (act.diag)
      :language: dot
      :linenos:

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
