:topic: Hyperlink

.. index::
   triple: Sphinx; Syntax; Hyperlink

Hyperlink
*********

The link text is set by putting a ``_`` after some text. The ````` is used
to group text, allowing you to include multiple words in your link text.
You should use the `````, even when the link text is only one word. This
keeps the syntax consistent.

The link target is defined inline or at the bottom of the section with
:rst:`.. _<link text>: <target>` (*reference style*).

The :duref:`Hyperlink Targets <hyperlinks>` in |Docutils| provides the basic
specification for :duref:`external <external-hyperlink-targets>` and
:duref:`anonymous <anonymous-hyperlinks>` hyperlink targets. These are also
called :duref:`explicit hyperlink targets <explicit-hyperlink-targets>`.

:the example:

   .. literalinclude:: hyperlink/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: hyperlink/example.rsti

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
