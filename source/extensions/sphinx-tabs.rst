:topic: Tabbed Content

.. index::
   triple: Sphinx; Extension; Tabbed Content

Tabbed Content
##############

.. pull-quote::

   .. attention::

      Only practicable and usable for |HTML| builder.

:PyPI Package:   https://pypi.org/project/sphinx-tabs/
:Documentation:  https://sphinx-tabs.readthedocs.io/
:Git Repository: https://github.com/executablebooks/sphinx-tabs

Create tabbed content in |Sphinx| documentation when building |HTML|.

:Features:

   1. Basic and nested tabs.
   2. Grouped Tabs.
   3. Code Tabs.

:raw-latex:`\clearpage\phantomsection`

.. rst:directive:: tabs
.. rst:directive:: tab

   For more details, see :doc:`spxtabs:index` in the extension demonstration
   and the :file:`README.md` in the extension Git repository.

   :the example:

      .. literalinclude:: sphinx-tabs/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: sphinx-tabs/example.rsti

   :raw-latex:`\clearpage\phantomsection`

   Nested tabs are also possible.

   :the example:

      .. literalinclude:: sphinx-tabs/nested/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: sphinx-tabs/nested/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. rst:directive:: group-tab

   Also tabs can stick together in groups.

   :the example:

      .. literalinclude:: sphinx-tabs/group/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: sphinx-tabs/group/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. rst:directive:: code-tab

   Similar to grouped tabs they can contain code areas with
   syntax highlighting.

   :the example:

      .. literalinclude:: sphinx-tabs/code/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: sphinx-tabs/code/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. spelling::

   Proxima
   Centauri

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
