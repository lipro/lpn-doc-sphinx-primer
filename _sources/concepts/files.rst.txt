:topic: File, Directory, Path

.. index::
   triple: Sphinx; Syntax; Files

File, Directory, Path
#####################

File and directories (or generally paths) are formated by :rst:`:file:`
inline markup. Backslashes (Windows paths) ``\`` have to written as ``\\``.
The name of an executable program should be documented by :rst:`:program:`
inline markup. This may differ from the file name for the executable for
some platforms. In particular, the :file:`.exe` (or other) extension should
be omitted for Windows programs. For OS-level command use :rst:`:command:`
inline markup.

.. rst:role:: file

   For more details, see :rst:role:`sphinx:file` role; about the
   :rst:role:`sphinx:program` role in :doc:`./semantic-referencing`, and
   about the :rst:role:`sphinx:command` role in :doc:`./user-interfaces`.

   :the example:

      .. literalinclude:: files/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: files/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
