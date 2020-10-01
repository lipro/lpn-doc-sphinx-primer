:topic: Paragraphs

.. index::
   triple: Sphinx; Syntax; Paragraphs

Paragraphs
##########

The :duref:`paragraph <paragraphs>` is the most basic block in a
|reStructuredText| document. Paragraphs are simply chunks of text separated
by one or more blank lines. As in |Python|, indentation is significant in
|reStructuredText|, so all lines of the same paragraph must be left-aligned
to the same level of indentation. General rules can be looked up under
:doc:`./whitespace`.

:the example:

   .. literalinclude:: paragraphs/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: paragraphs/example.rsti

.. index::
   triple: Sphinx; Syntax; Block Quotation
   triple: Sphinx; Syntax; Quotes

Quotes (block quotation) Element
********************************

:duref:`Block quoted <block-quotes>` paragraphs are quoted by just indenting
them more than the surrounding paragraphs.

:the example:

   .. literalinclude:: paragraphs/block-quote/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: paragraphs/block-quote/example.rsti

.. rst:directive:: pull-quote

   :dudir:`Pull-quoted <pull-quotes>` paragraphs are similar to block quotes
   but are directives for small selection of text to "pull out and quote",
   typically in a larger typeface.

   :the example:

      .. literalinclude:: paragraphs/pull-quote/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: paragraphs/pull-quote/example.rsti

.. index::
   triple: Sphinx; Syntax; Line Blocks

Line Blocks
***********

:duref:`Line blocks <line-blocks>` are useful for addresses, verse, and
adornment-free lists. They are quoted by just a ``|`` pipe sign in front
of each single line.

:the example:

   .. literalinclude:: paragraphs/line-block/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: paragraphs/line-block/example.rsti

.. index::
   triple: Sphinx; Syntax; Doctest Blocks

Doctest Blocks
**************

:duref:`Doctest blocks <doctest-blocks>` are interactive |Python| sessions
cut-and-pasted into docstrings. They do not require the
:doc:`literal blocks <./code-example>` syntax. The doctest block must end
with a blank line and should not end with an unused prompt, see
:ref:`sphinx:rst-doctest-blocks` in |Sphinx| for more informations.

:the example:

   .. literalinclude:: paragraphs/doctest/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: paragraphs/doctest/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
