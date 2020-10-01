:topic: Paneled Content

.. index::
   triple: Sphinx; Extension; Paneled Content

Paneled Content
###############

.. pull-quote::

   .. todo:: Evaluate the integration and coexistence of this
             "Paneled Content" extension with all other. See
             :file:`conf.py` for more details.

   .. attention::

      Only practicable and usable for |HTML| builder.

:PyPI Package:   https://pypi.org/project/sphinx-panels/
:Documentation:  https://sphinx-panels.readthedocs.io/
:Git Repository: https://github.com/executablebooks/sphinx-panels

Create paneled content in |Sphinx| documentation when building |HTML|.

:Features:

   1. Panels in grid or cards layout.
   2. Panels with click-able link-button.
   3. Panels with toggle-able content by drop-downs.
   4. Panels with styling: header, footer, images, icons, |badges|, animations

   For more details, see :doc:`spxpanels:index` in the extension demonstration
   and the :file:`README.md` in the extension Git repository.

.. rst:directive:: panels

   For more details, see :spxpanels:`Panels Usage <id1>`.

.. rst:directive:: dropdown

   For more details, see :spxpanels:`Dropdown Usage <dropdown-usage>`.

.. rst:directive:: link-button

   For more details, see :spxpanels:`Link Buttons <link-buttons>`.

.. rst:directive:: div

   For more details, see :spxpanels:`Div Directive <div-directive>`.

.. rst:role:: badge
.. rst:role:: link-badge

   For more details, see :spxpanels:`Link Badges <link-badges>`.

.. rst:role:: opticon
.. rst:role:: fa

   For more details, see :spxpanels:`Inline Icons <inline-icons>`.

.. only:: not html or not sphinx_panels

   .. pull-quote::

      .. admonition:: Extension not applicable
         :class: danger

         This |Sphinx| extension is quite new and is under constant
         development. The current behavior disturbs the integration,
         so the extension is disabled for now (see :file:`conf.py`).
         Currently known bugs are:

         * annoying side effects with the :doc:`./sphinx-tabs` extension by
           the automatically integrated and delivered Bootstrap 4.0 |CSS|
         * no proper and practical |LaTeX| builder support

.. only:: html and sphinx_panels

   .. _panels/example:

   :the example:

      .. literalinclude:: sphinx-panels/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: sphinx-panels/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
