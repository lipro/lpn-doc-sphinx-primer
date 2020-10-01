:topic: Use of whitespace

.. index::
   triple: Sphinx; Syntax; Use of whitespace

Use of whitespace
#################

All |reStructuredText| files **use an indentation of three (3) spaces**;
no tabs are allowed. The maximum **line length is 80 characters** for
normal text, but tables, deeply indented code samples and long links may
extend beyond that. *Code example* bodies should use *normal four-(4)-space*
indentation.

Make generous use of blank lines where applicable; they help group things
together.

Indentation
***********

Indentation is meaningful in |Sphinx| and |reStructuredText| text. Usually,
indenting a section means that is "belongs to" the line it is indented
under.

:for example:

   .. code-block:: rst
      :linenos:

      .. figure:: path-to-image.*

         This is the caption of the figure. Notice that it is indented under
         the line defining the figure.

The rules for indentation are:

- Use **spaces, not tabs**.
- Generally, indent **three (3) spaces**.
- Code example, indent **four (4) spaces**, except |reStructuredText| examples.

The exception to the three (3) spaces rule is |ul| and |ol|, where indentation
follows the content of the list item.

.. |ul| replace::
   :ref:`concepts/lists:Unordered (bullet) lists`

.. |ol| replace::
   :ref:`concepts/lists:Ordered (numbered) lists`

.. rubric:: unordered (bulleted) list

:(2) spaces:

   .. code-block:: rst
      :linenos:

      * This is a list item.

        This is some additional content related to first item. Notice that
        it is indented to the same column as the first line of content.
        In this case, that's three (2) spaces.

      .
      .
      .

      * The N-th item in a list.

.. rubric:: ordered (numbered) list

:(4) spaces:

   .. code-block:: rst
      :linenos:

      1.  This is a list item.

          This is some additional content related to Item 1. Notice that
          it is indented to the same column as the first line of content.
          In this case, that's three (3) spaces.

      .
      .
      .

      10. The tenth item in a list.

          This related content will be indented four (4) spaces.

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
