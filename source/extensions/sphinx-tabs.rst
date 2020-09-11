:topic: Tabbed Content

.. index::
   triple: Sphinx; Extension; Tabbed Content

Tabbed Content
##############

.. attention::

   Only practicable and usable for HTML builder.

:PyPI Package:   https://pypi.org/project/sphinx-tabs/
:Documentation:  https://sphinx-tabs.readthedocs.io/
:Git Repository: https://github.com/executablebooks/sphinx-tabs

Create tabbed content in Sphinx documentation when building HTML.

:Features:

   1. Basic and nested tabs.
   2. Grouped Tabs.
   3. Code Tabs.

.. todo:: activate "Tabbed Content" extension.

.. rst:directive:: tabs
.. rst:directive:: tab

   For more details, see :doc:`spxtabs:index` in the extension demonstration
   and the :file:`README.md` in the extension Git repository.

   :the example:

      .. literalinclude:: sphinx-tabs-example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   .. code-block:: rst

      :which gives:

         .. include:: sphinx-tabs-example.rsti

   Nested tabs are also possible.

   :the example:

      .. literalinclude:: sphinx-tabs-nested-example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   .. code-block:: rst

      :which gives:

         .. include:: sphinx-tabs-nested-example.rsti

.. rst:directive:: group-tab

   Also tabs can stick together in groups.

   :the example:

      .. literalinclude:: sphinx-tabs-group-example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   .. code-block:: rst

      :which gives:

         .. include:: sphinx-tabs-group-example.rsti

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
