:topic: Explicit Markup

.. index::
   triple: Sphinx; Syntax; Explicit Markup

Explicit Markup
###############

:duref:`"Explicit markup" <explicit-markup-blocks>` is used in |reStructuredText|
for most constructs that need special handling, such as footnotes,
specially-highlighted paragraphs, comments, and generic directives.

An explicit markup block begins with a line starting with two dots followed
by whitespace (:rst:`".. "`) and is terminated by the next paragraph at the same
level of indentation. There needs to be a blank line between explicit markup
and normal paragraphs. This may all sound a bit complicated, but it is
intuitive enough when you write it.

.. index::
   triple: Sphinx; Syntax; Comments

Comments
********

Every explicit markup block which is not a valid markup construct (like the
footnotes above) is regarded as a :duref:`comment <comments>`.

However, it must have some text in the :rst:`".. "` line, otherwise it is
ignored, and content will be displayed (indented).

:the example:

   .. code-block:: rst
      :linenos:

      .. This is a comment
      ..
         _so: is this!
      ..
         [and] this!
      ..
         this:: too!
      ..
         |even| this:: !

.. index::
   triple: Sphinx; Syntax; Directives

Directives
**********

:doc:`./naming/directives` are generic blocks of explicit markup. Besides
:doc:`./naming/roles`, it is one of the extension mechanisms of
|reStructuredText|, and |Sphinx| makes heavy use of it. Basically, a directive
consists of a name, arguments, options and content. Keep this terminology in
mind, it is used in one of the next chapter describing custom directives.

:the example:

   .. code-block:: rst
      :linenos:

      .. cpp:function:: char* foo(x)
                        char* foo(y, z)
         :noindexentry:

         Return a line of text input from the user.

:which gives:

   .. cpp:function:: char* foo(x)
                     char* foo(y, z)
      :noindexentry:

      Return a line of text input from the user.

:rst:`.. cpp:function::` is the directive name. It is given two arguments
here, the remainder of the first line and the second line, as well as one
option :rst:`:noindexentry:`. As you can see, options are given in the lines
immediately following the arguments and indicated by the colons.

The directive content follows after a blank line and is indented relative to
the directive start.

If you want to suppress the addition of an entry in the shown index, you can
give the directive option flag :rst:`:noindexentry:`. If you want to typeset
an object description, without even making it available for cross-referencing,
you can give the directive option flag :rst:`:noindex:` (which implies
:rst:`:noindexentry:`).

.. pull-quote::

   .. hint::

      As far as possible, all examples in this document use the
      :rst:`:noindexentry:` option to keep the automatically created
      index as clean as possible but still be able to reference it.

.. index::
   triple: Sphinx; Syntax; Footnotes

Footnotes
*********

For :duref:`footnotes`, use :rst:`[#]_` to mark the footnote location, and
add the footnote body at the bottom of the document after a "Footnotes"
rubric heading.

:the example:

   .. code-block:: rst
      :linenos:

      Lorem ipsum [#]_ dolor sit amet ... [#]_

      .. rubric:: Footnotes

      .. [#] Text of the first footnote.
      .. [#] Text of the second footnote.

:which gives:

   Lorem ipsum [#]_ dolor sit amet ... [#]_

   .. rubric:: Footnotes

   .. [#] Text of the first footnote.
   .. [#] Text of the second footnote.

You can also explicitly number the footnotes for better context.

.. index::
   triple: Sphinx; Syntax; Citations

Citations
*********

:duref:`Citations <citations>` are identical to footnotes except that they
use only non-numeric labels such as :rst:`[note]_` or :rst:`[GVR2001]_`.
Citation labels are simple :duref:`reference names <reference-names>`
(case-insensitive single words consisting of alphanumerics plus internal
hyphens, underscores, and periods; no whitespace). Citations may be rendered
separately and differently from footnotes.

:the example:

   .. code-block:: rst
      :linenos:

      Here is a citation reference: [CIT2002]_.

      .. [CIT2002] This is the citation. It's just like a footnote,
         except the label is textual.

:which gives:

   Here is a citation reference: [CIT2002]_.

   .. [CIT2002] This is the citation. It's just like a footnote,
      except the label is textual.

To use a professional bibliography, you should use the |Sphinx| extension
:doc:`../extensions/bibtex`.

:raw-latex:`\clearpage\phantomsection`

.. spelling::

   Lorem
   ipsum
   dolor
   sit
   amet

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
