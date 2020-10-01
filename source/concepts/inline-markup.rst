:topic: Inline Markup

.. index::
   triple: Sphinx; Syntax; Inline Markup

Inline Markup
#############

If you want to make sure that text is shown in monospaced fonts for code
examples or concepts, use double backticks around it. It looks ``like this``
on output.

:the example:

   .. code-block:: rst
      :linenos:

      You can use **backticks** for showing ``highlighted`` code.

:which gives:

      You can use **backticks** for showing ``highlighted`` code.

Refer to :ref:`sphinx:rst-inline-markup` added by |Sphinx|.

All the standard |reStructuredText| inline markups are quite simple, use:

* one asterisk:  :rst:`*text*` for emphasis (*italics*),
* two asterisks: :rst:`**text**` for strong emphasis (**boldface**), and
* backquotes:    ````text```` for code samples as shown above (``literal``).

If asterisks or backquotes appear in running text and could be confused
with inline markup delimiters, they have to be escaped with a backslash
or encapsulated by :doc:`./naming/roles`:

.. rubric:: one escaped asterisk

:the example:

   .. code-block:: rst
      :linenos:

      *italics \*with\* asterisk*,
      **boldface \*with\* asterisk**

:which gives:

      *italics \*with\* asterisk*,
      **boldface \*with\* asterisk**

.. rubric:: two escaped asterisks

:the example:

   .. code-block:: rst
      :linenos:

      *italics \*\*with\*\* asterisks*,
      **boldface \*\*with\*\* asterisks**

:which gives:

      *italics \*\*with\*\* asterisks*,
      **boldface \*\*with\*\* asterisks**,

.. rubric:: two escaped backquotes

:the example:

   .. code-block:: rst
      :linenos:

      *italics \`\`with\`\` backquotes*,
      **boldface \`\`with\`\` backquotes**

:which gives:

      *italics \`\`with\`\` backquotes*,
      **boldface \`\`with\`\` backquotes**

.. rubric:: escaped backquote and asterisks

:the example:

   .. code-block:: rst
      :linenos:

      :literal:`literal \`\`with\`\` backquotes **and** asterisks`

:which gives:

      :literal:`literal \`\`with\`\` backquotes **and** asterisks`

Be aware of some restrictions of this markup:

* it may not be nested (see
  :dutodo:`nested inline markup <nested-inline-markup>`
  in |Docutils| To Do List),
* content may not start or end with whitespace: :rst:`* text*` is wrong,
* it must be separated from surrounding text by non-word characters.
  Use a backslash escaped space to work around that:
  :rst:`thisis\ **one**\ word` (thisis\ **one**\ word).

:raw-latex:`\clearpage\phantomsection`

.. spelling::

   thisis

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
