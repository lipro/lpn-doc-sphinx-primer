:topic: Referencing

.. index::
   triple: Sphinx; Syntax; Referencing

Referencing
###########

Another important |Sphinx| feature is that it allows referencing across
documents. This is another powerful way to tie documents together.

The simplest way to do this is to define an explicit reference object which
can then be referenced directly as internal hyperlink target or with
:rst:`:ref:`refname`` or in rare cases with :rst:`:numref:`refname`` depending
on the :rst:dir:`sphinx:toctree` section numbering setup. |Sphinx| also supports
:rst:`:doc:`docname`` for linking to a document via built-in extension
:py:mod:`sphinx:sphinx.ext.intersphinx` and also supports auto-generated labels
for each section via built-in extension :py:mod:`sphinx:sphinx.ext.autosectionlabel`.

The :duref:`Hyperlink Targets <hyperlinks>` in |Docutils| provides the basic
specification for :duref:`internal <internal-hyperlink-targets>` and
:duref:`external <external-hyperlink-targets>` hyperlink targets. These are
also called :duref:`explicit <explicit-hyperlink-targets>` and also available
as :duref:`implicit <implicit-hyperlink-targets>` hyperlink targets.

.. rst:role:: doc
.. rst:role:: ref
.. rst:role:: numref

   For more details, see :rst:role:`sphinx:doc`, :rst:role:`sphinx:ref` and
   :rst:role:`sphinx:numref` role.

   :the example:

      .. literalinclude:: referencing/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

      .. code-block:: rst
         :linenos:

         .. _reference-name:

         A cool section
         """"""""""""""

         .. _target:

         The hyperlink target above points to this paragraph.

   :which gives:

      .. include:: referencing/example.rsti

.. rst-class:: centered

.. _reference-name:

A cool section
""""""""""""""

.. rst-class:: centered

.. _target:

The hyperlink target above points to this paragraph.

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
