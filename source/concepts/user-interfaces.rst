:topic: Writing about User Interface

.. index::
   triple: Sphinx; Syntax; User Interface
   triple: Sphinx; Syntax; Other Semantic Markup

Writing about User Interface
############################

Several roles are used when describing user interactions.

.. rst:role:: guilabel

   Marks up *actual UI text* of form labels or buttons.
   For more details, see :rst:role:`sphinx:guilabel` role.

   :the example:

      .. literalinclude:: user-interfaces/guilabel/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: user-interfaces/guilabel/example.rsti

.. rst:role:: menuselection

   Marks up the *actual UI text* of a navigation menu or form select element.
   For more details, see :rst:role:`sphinx:menuselection` role.

   :the example:

      .. literalinclude:: user-interfaces/menuselection/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: user-interfaces/menuselection/example.rsti

   When writing about multi-level menus, use a single :rst:`:menuselection:`
   role, and separate menu choices with :rst:`-->`.

   .. pull-quote::

      .. note::

         In some situations you might not be clear about which option,
         :rst:role:`sphinx:menuselection` or :rst:role:`sphinx:guilabel`,
         to use. |GUI|\ s in real life can sometimes be ambiguous. The general
         rule is:

         * Actual |UI| text will always receive :rst:role:`sphinx:guilabel`
           role unless the text could reasonably be understood to be part
           of a menu.
         * If the actual |UI| text could be understood as a menu,
           :rst:role:`sphinx:menuselection` should be used.

         These both render the same on output, so don't worry too much if
         you get it wrong. Just use your judgment and take your best guess.

.. rst:role:: kbd

   Marks up a sequence of literal keyboard strokes.
   For more details, see :rst:role:`sphinx:kbd` role.

   :the example:

      .. literalinclude:: user-interfaces/kbd/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: user-interfaces/kbd/example.rsti

.. rst:role:: command

   Marks up a terminal command.
   For more details, see :rst:role:`sphinx:command` role.

   :the example:

      .. literalinclude:: user-interfaces/command/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: user-interfaces/command/example.rsti

To document a |CLI| application, you will find more information in
:doc:`./semantic-referencing`.

Other Semantic Markup
*********************

.. rst:role:: abbr

   Marks up an abbreviation. If the role content contains a parenthesized
   explanation, it will be treated specially: it will be shown in a tool-tip
   in |HTML|. For more details, see :rst:role:`sphinx:abbr` role.

   :the example:

      .. literalinclude:: user-interfaces/abbr/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: user-interfaces/abbr/example.rsti

.. rst:role:: dfn

   Marks the defining instance of a term outside the index or glossary.
   For more details, see :rst:role:`sphinx:dfn` role.

   :the example:

      .. literalinclude:: user-interfaces/dfn/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: user-interfaces/dfn/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
