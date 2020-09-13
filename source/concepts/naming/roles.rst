:topic: Roles

.. index::
   triple: Sphinx; Syntax; Roles

Roles
#####

A :term:`sphinx:role` or "custom interpreted text role" is an inline piece
of explicit markup, see :doc:`../inline-markup` and :doc:`../explicit-markup`.
It signifies that the enclosed text should be interpreted in a specific way.
|Sphinx| uses this to provide semantic markup and cross-referencing of
identifiers, as described in the appropriate section.

The general syntax is :rst:`:rolename:`content``. Like
:doc:`../naming/directives`, roles are extensible. Own roles can be created.
They are used inside other text structures.

|Docutils| supports the following roles (incomplete list):

.. rst:role:: emphasis

   :durole:`emphasis` --
   :rst:`:emphasis:`emphasis`` --
   equivalent of :rst:`*emphasis*`

.. rst:role:: strong

   :durole:`strong` --
   :rst:`:strong:`strong`` --
   equivalent of :rst:`**strong**`

.. rst:role:: literal

   :durole:`literal` --
   :rst:`:literal:`literal`` --
   equivalent of ````literal````

.. rst:role:: code

   :durole:`code` --
   :rst:`:code:`code`` --
   equivalent of ````code````

.. rst:role:: subscript

   :durole:`subscript` --
   :rst:`:subscript:`subscript`` --
   subscript text

   :the example:

      The Fibonacci numbers (without inline role for :doc:`../mathematics`).

      .. literalinclude:: roles/subscript/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: roles/subscript/example.rsti

.. rst:role:: superscript

   :durole:`superscript` --
   :rst:`:superscript:`superscript`` --
   superscript text

   :the example:

      The elementary charge (without inline role for :doc:`../mathematics`).

      .. literalinclude:: roles/superscript/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: roles/superscript/example.rsti

.. rst:role:: math

   :durole:`math` --
   :rst:`:math:`mathematic equations`` --
   for :doc:`../mathematics` equations

.. rst:role:: pep-reference

   :durole:`pep-reference` --
   :rst:`:pep-reference:`pep-reference`` --
   equivalent to :rst:`:pep:`pep reference number`` --
   for :doc:`../external-referencing`
   into the |PEP| index

.. rst:role:: rfc-reference

   :durole:`rfc-reference` --
   :rst:`:rfc-reference:`rfc-reference`` --
   equivalent to :rst:`:rfc:`rfc reference number`` --
   for :doc:`../external-referencing`
   into the |RFC| index

.. rst:role:: title-reference

   :durole:`title-reference` --
   :rst:`:title-reference:`title-reference`` --
   for titles of books, periodicals, and other materials

.. seealso::

   * Refer to :ref:`sphinx:rst-roles-alt`
     for roles provided by |Docutils|.
   * Refer to :doc:`sphinx:usage/restructuredtext/roles`
     for roles added by |Sphinx|.

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
