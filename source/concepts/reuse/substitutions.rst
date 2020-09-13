:topic: Substitutions

.. index::
   triple: Sphinx; Syntax; Substitutions

Substitutions
#############

Substitutions are a useful way to define a value which is needed in many
places. Substitution definitions are indicated by an explicit markup start
(:rst:`".. "`) followed by a vertical bar, the substitution text (which gets
substituted), another vertical bar, whitespace, and the definition block.

A substitution definition block may contain inline-compatible directives
such as :doc:`../images`, :doc:`../downloads`, or other
:dudir:`Substitution Directives <directives-for-substitution-definitions>`:

* :dudir:`Replacement Text <replacement-text>`
* :dudir:`Unicode Character Codes <unicode-character-codes>`
* :dudir:`Date <date>`

For more information, see :doc:`sphinx:usage/restructuredtext/basics`,
section *Substitutions*, or refer the
:duref:`Substitution References <substitution-definitions>`. |Sphinx| provides
additional predefined :ref:`sphinx:default-substitutions`.

.. rst:directive:: replace

   :the example:

      .. literalinclude:: substitutions/replace/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: substitutions/replace/example.rsti

.. index::
   triple: Sphinx; Syntax; Styled Reference

Styled Reference
****************

You can also create a reference with styled text,
:dufaq:`nested inline markup <is-nested-inline-markup-possible>`.

:the example:

   .. literalinclude:: substitutions/nested-inline-markup/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: substitutions/nested-inline-markup/example.rsti

.. index::
   triple: Sphinx; Syntax; RST Prolog
   triple: Sphinx; Syntax; RST Epilog

Use Prolog and Epilog
*********************

The |Sphinx| configuration values :confval:`sphinx:rst_prolog` and
:confval:`sphinx:rst_epilog` in :file:`conf.py` contains a list of global
substitutions that can be used from any file. The (incomplete) list for this
document is given below:

:|f_project|:   |CRT| leads to: "|project|"
:|f_author|:    |CRT| leads to: "|author|"
:|f_publisher|: |CRT| leads to: "|publisher|"
:|f_copyright|: |CRT| leads to: "|copyright|"
:|f_LICENSE|:   |CRT| leads to: "|LICENSE|"
:|f_CREDITS|:   |CRT| leads to: "|CREDITS|"

.. |f_project|   replace:: :rst:`"|project|"`
.. |f_author|    replace:: :rst:`"|author|"`
.. |f_publisher| replace:: :rst:`"|publisher|"`
.. |f_copyright| replace:: :rst:`"|copyright|"`
.. |f_LICENSE|   replace:: :rst:`"|LICENSE|"`
.. |f_CREDITS|   replace:: :rst:`"|CREDITS|"`

.. index::
   triple: Sphinx; Syntax; Inline Image

Inline Image
************

You can add inline images in the document using substitutions. The following
block of code substitutes arrow in the text with the image specified.

:the example:

   .. literalinclude:: substitutions/inline-images/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: substitutions/inline-images/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
