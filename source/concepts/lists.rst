:topic: Lists, Definition Lists

.. index::
   triple: Sphinx; Syntax; Lists, Definition Lists

Lists, Definition Lists
#######################

List markup is natural: just place an asterisk or hyphen at the start of a
paragraph and indent properly. The same goes for numbered list (number or
letter with tailed dot); they can also be automatically numbered using a
``#`` sign.

Nested lists are possible, but be aware that they must be separated from
the parent list items by blank lines.

.. index::
   triple: Sphinx; Syntax; Unordered Lists

Unordered (bullet) Lists
************************

:duref:`Bullet lists <bullet-lists>` contains list item elements which are
uniformly marked with bullets. Bullets are typically simple dingbats (symbols)
such as circles and squares.

.. rubric:: bulleted lists ( ``<ul>`` )

:the example:

   .. literalinclude:: lists/unordered/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: lists/unordered/example.rsti

.. index::
   triple: Sphinx; Syntax; Ordered Lists

Ordered (numbered) Lists
************************

:duref:`Enumerated lists <enumerated-lists>` (a.k.a. "ordered" lists)
are similar to bullet lists, but use enumerators instead of bullets.
An enumerator consists of an enumeration sequence member and formatting,
followed by whitespace. Different enumeration sequences are possible,
e.g. Arabic or Roman numerals or alphabet characters.

.. rubric:: numbered lists ( ``<ol>`` )

:the example:

   .. literalinclude:: lists/ordered/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: lists/ordered/example.rsti

.. index::
   triple: Sphinx; Syntax; Definition Lists

Definition (description) Lists
******************************

:duref:`Definition Lists <definition-lists>` contains a list of terms and
their definitions. Each list item element contains a term, optional
classifiers, and a definition.

.. rubric:: definition list ( ``<dl>`` )

:the example:

   .. literalinclude:: lists/definition/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: lists/definition/example.rsti

.. index::
   triple: Sphinx; Syntax; Field Lists

Field (description) Lists
=========================

:duref:`Field lists <field-lists>` are special definition lists.
They may also be used for two-column table-like structures resembling
database records (label & data pairs). |Sphinx| extends standard docutils
behavior for :doc:`sphinx:usage/restructuredtext/field-lists` and
intercepts field lists specified at the beginning of documents and
adds some extra (optional) functionality.

.. rubric:: field list

:the example:

   .. literalinclude:: lists/field/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: lists/field/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
