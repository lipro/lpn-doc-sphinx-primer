:topic: Downloadable Files

.. index::
   triple: Sphinx; Syntax; Downloadable Files

Downloadable Files
##################

To place a downloadable file in a document, use the :rst:role:`download` role.

.. code-block:: rst

  To understand the procedure better, see this
  :download:`example script </_downloads/contributing/example_script.py>`.

Downloadable files with a dedicated context to a specific part of the
documentation should also be placed exactly at this point in the source
tree of the documentation. Other common artefacts should be put in the
documentation root or the :file:`/_downloads/` subdirectory, and they
should be in a subdirectory with the same name as the document in which
they appear (that is, the filename without the :file:`.rst` extension).

.. pull-quote::

   .. attention::

      Downloads are not fully supported by all |Sphinx| builders.
      Especially offline documents like |LaTeX|/|PDF| will be created
      correctly, but will not provide additional artifacts.

.. rst:role:: download

   For more details, see :rst:role:`sphinx:download` role.

   :the example:

      .. literalinclude:: downloads/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: downloads/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
