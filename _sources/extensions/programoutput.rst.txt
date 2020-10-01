:topic: Program Output

.. index::
   triple: Sphinx; Extension; Program Output

Program Output
##############

:PyPI Package:   https://pypi.org/project/sphinxcontrib-programoutput/
:Documentation:  https://sphinxcontrib-programoutput.readthedocs.org/
:Git Repository: https://github.com/NextThought/sphinxcontrib-programoutput

Literally insert the output of arbitrary commands into documents, helping
you to keep your command examples up to date. It consists:

* :py:mod:`scprgout:sphinxcontrib.programoutput`: insert command output

Complete output
***************

To include the output of a command into your document, use the
:rst:`.. program-output::` directive provided by this extension.

.. rst:directive:: program-output

   For more details, see :rst:dir:`scprgout:program-output` directive.

   :the example:

      .. code-block:: rst
         :linenos:

         .. program-output:: python --version

   :which gives:

      .. program-output:: python --version

The whole output of ``python --version``, including any messages on
standard error, is inserted into the current document, formatted as
literal text without any syntax highlighting. You can omit the content
of the standard error stream with the :rst:`:nostderr:` option.

By default, commands are executed in the top-level source directory. You can
choose an alternate working directory with the :rst:`:cwd:` option. The
argument of this option is either a path relative to the current source
file, or a absolute path which means that it is relative to the top level
source directory.

Shortening the output
*********************

Lengthy output can be shortened with the :rst:`:ellipsis:` option. Its value
denotes lines to omit when inserting the output of the command. Instead,
a single ellipsis ``...`` is inserted.

:the example:

   If used with a single number, all lines after the specified line
   are omitted:

   .. code-block:: rst
      :linenos:

      .. program-output:: python --help
         :ellipsis: 2

:which gives:

   The above omits all lines after the second one:

   .. program-output:: python --help
      :ellipsis: 2

Negative numbers count from the last line backwards, thus replacing ``2``
with ``-2`` in the above example would only omit the last two lines.

:the example:

   If used with two comma-separated line numbers, all lines in between
   the specified lines are omitted. Again, a negative number counts
   from the last line backwards:

   .. code-block:: rst
      :linenos:

      .. program-output:: python --help
         :caption: First two and last second lines from :command:`python --help`
         :name: program-output-python-help
         :ellipsis: 2,-2

:which gives:

   The above omits all lines except the first two and the last two lines:

   .. program-output:: python --help
      :caption: First two and last second lines from :command:`python --help`
      :name: program-output-python-help
      :ellipsis: 2,-2

Mimicking shell input
*********************

You can mimic shell input with the :rst:`.. command-output::` directive
[#alias]_. This directive inserts the command along with its output into
the document.

.. rst:directive:: command-output

   For more details, see :rst:dir:`scprgout:command-output` directive.

   :the example:

      .. code-block:: rst
         :linenos:

         .. command-output:: python --version

   :which gives:

      .. command-output:: python --version

The appearance of this output can be configured with
:literal:`programoutput_prompt_template`.  When used in conjunction with
:rst:`:ellipsis:`, the command itself and any additional text is *never*
omitted. :rst:`:ellipsis:` always refers to the *immediate output* of the
command.

:the example:

   .. code-block:: rst
      :linenos:

      .. command-output:: python --help
         :caption: First two lines from :command:`python --help` with prompt
         :name: command-output-python-help
         :ellipsis: 2

:which gives:

   .. command-output:: python --help
      :caption: First two lines from :command:`python --help` with prompt
      :name: command-output-python-help
      :ellipsis: 2

Command execution and shell expansion
*************************************

Normally the command is splittet according to the |POSIX| shell syntax (see
:py:mod:`pydocs:shlex`), and executed directly.  Thus special shell features
like expansion of environment variables will not work.

:the example:

   .. code-block:: rst
      :linenos:

      .. command-output:: echo "$USER"

:which gives:

   .. command-output:: echo "$USER"

To enable these features, enable the :rst:`:shell:` option.  With this
option, the command is literally passed to the system shell.

:the example:

   .. code-block:: rst
      :linenos:

      .. command-output:: echo "$USER"
         :shell:

:which gives:

   .. command-output:: echo "$USER"
      :shell:

Other shell features like process expansion consequently work, too.

:the example:

   .. code-block:: rst
      :linenos:

      .. command-output:: ls -l $(which grep)
         :shell:

:which gives:

   .. command-output:: ls -l $(which grep)
      :shell:

.. pull-quote::

   .. warning:: Remember to use :rst:`:shell:` carefully to avoid unintended
                interpretation of shell syntax and swallowing of fatal errors!

Error handling
**************

If an unexpected exit code (also known as *return code*) is returned by a
command, it is considered to have failed. In this case, a build warning is
emitted to help you to detect misspelled commands or similar errors. By
default, a command is expected to exit with an exit code of 0, all other
codes indicate an error. In some cases however, it may be reasonable to
demonstrate failed programs. To avoid a (superfluous) warning in such a
case, you can specify the expected return code of a command with the
:rst:`:returncode:` option.

:the example:

   .. code-block:: rst
      :linenos:

      .. command-output:: python -c 'import sys, platform; print(sys.version); sys.exit(1)'
         :returncode: 1

:which gives:

   .. command-output:: python -c 'import sys, platform; print(sys.version); sys.exit(1)'
      :returncode: 1

The above command returns the exit code 1 (as given to
:py:func:`pydocs:sys.exit()`), but no warning will be emitted. On the
contrary, a warning will be emitted, should the command return 0!

.. pull-quote::

   .. note::

      Upon fatal errors which even prevent the execution of the command
      neither return code nor command output are available. In this case
      an error message is inserted into the document instead.

      If :rst:`:shell:` is set however, most of these fatal errors are
      handled by the system shell and turned into return codes instead.
      In this case the error message will only appear in the output of
      the shell. If you're using :rst:`:shell:`, double-check the output
      for errors. Best avoid :rst:`:shell:`, if possible.

.. rubric:: Footnotes

.. [#alias] This directive is just an alias for the :rst:`.. program-output::`
            directive with the :rst:`:prompt:` option set.

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
