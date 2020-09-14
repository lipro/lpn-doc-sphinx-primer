:topic: Code Example

.. index::
   triple: Sphinx; Syntax; Code Example

Code Example
############

The syntax for displaying code is the ``::`` mark, see
:ref:`sphinx:rst-literal-blocks`. When it is used at the end of a sentence,
|Sphinx| is smart and displays one ``:`` sign in the output, and knows there
is a code example in the following indented block, the
:duref:`Indented literal (code) block <indented-literal-blocks>`.
:duref:`Quoted literal (code) block <quoted-literal-blocks>` are unindented
contiguous blocks of text where each line begins with the same non-alphanumeric
printable 7-bit ASCII character.

.. rst:directive:: highlight

   For more details, see :rst:dir:`sphinx:highlight` directive.

   :the example:

      .. literalinclude:: code-example/literal-block/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

         .. include:: code-example/literal-block/example.rsti

The handling of the ``::`` marker is smart:

* If it occurs as a paragraph of its own, that paragraph is completely left
  out of the document.
* If it is preceded by whitespace, the marker is removed.
* If it is preceded by non-whitespace, the marker is replaced by a single
  colon.

That way, the first sentence in the above example's first paragraph would
be rendered as "... The next paragraph is a code sample:".

|Sphinx| extends the default language setup for each literal (code) block
with the :rst:`.. highlight::` directive. That is very useful if a specific
directive is not able to set the language by argument or option, even in this
case here.

:raw-latex:`\clearpage\phantomsection`

.. index::
   triple: Sphinx; Syntax; Code Blocks

Explicit Code Blocks
********************

Source code will be formatted by the directive :rst:`.. code-block::`.
|Sphinx|, like |Python|, uses meaningful whitespace. Blocks of content are
structured based on the indention level they are on.

.. rst:directive:: code-block

   For more details, see :rst:dir:`sphinx:code-block` directive.

   :the example:

      .. literalinclude:: code-example/code-block/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

         .. include:: code-example/code-block/example.rsti

Valid values for the highlighting :rst:`:language:` (first argument) are:

  * ``none`` (no highlighting)
  * ``python`` (the default)
  * ``c`` and ``cpp`` (|C/C++|)
  * ``rst`` or ``rest`` (|reStructuredText|)
  * ``bash`` or ``ksh`` or ``sh`` (Unix Shell scripts)
  * ``shell-session`` (Unix Shell sessions)
  * ``ps1`` or ``posh`` or ``powershell`` (Windows PowerShell code)
  * ``ps1con`` (Windows PowerShell sessions)
  * ``dosbatch`` or ``winbatch`` (|MS-DOS|/Windows Batch file)
  * ``doscon`` (|MS-DOS| sessions)
  * ``cfg`` or ``ini`` (Generic configuration file, mostly INI files)
  * ``sql`` (Generic |SQL| commands)
  * ``registry`` (Windows Registry files produced by :command:`regedit`)
  * ``guess`` (let |Pygments| guess the lexer based on contents, only works with
    certain well-recognizable languages)
  * ... and any other `lexer alias that Pygments supports
    <https://pygments.org/docs/lexers/>`_.

:raw-latex:`\clearpage\phantomsection`

.. index::
   triple: Sphinx; Syntax; Literalinclude

Explicit Code Includes
**********************

If the text resides in a separate file, use the :rst:`.. literalinclude::`
directive:

.. rst:directive:: literalinclude

   For more details, see :rst:dir:`sphinx:literalinclude` directive.

   :the example:

      .. literalinclude:: code-example/literalinclude/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

         .. include:: code-example/literalinclude/example.rsti

All included files could be located under :file:`/include`. The beginning
:file:`/` means, root directory of the documentation source directory. Without
it, the path is relative to the directory of the including file.

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
