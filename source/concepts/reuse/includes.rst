.. index::
   triple: Sphinx; Syntax; Includes

Include a Shared File
#####################

.. rst:directive:: include

   For more details, see
   :dudir:`Including an External Document Fragment <including-an-external-document-fragment>`
   in |Docutils|.

   You can store complex content, such as tasks, or code samples, in a file
   that is then included in multiple |reStructuredText| document files.

   If you are working on multiple documents, you can save entire topics in
   shared files, and include those files in multiple documents.

   You add a shared file to content in your project with the
   :rst:`.. include::` directive. For example:

   .. code-block:: rst

      .. include:: /{absolut-document-subdirectory}/{file}.rsti
      .. include:: {relative-document-subdirectory}/{file}.rsti

   The contents of the shared file will then be built in the document.

   .. pull-quote::

      .. caution::
   
         Include paths are relative to the file in the document project,
         not the file in shared content.

   Standard data files intended for inclusion in |reStructuredText| documents
   are distributed with the |Docutils| source code, located in the :py:mod:`docutils`
   package in the :file:`docutils/parsers/rst/include` directory. To access
   these files, use the special syntax for standard include data files, angle
   brackets around the file name:

   .. code-block:: rst

      .. include:: <isonum.txt>

   .. pull-quote::

      .. note::

         You must reference the shared file from a file within the
	 document. You cannot use a direct TOC reference to files
	 outside of the document directory.

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
