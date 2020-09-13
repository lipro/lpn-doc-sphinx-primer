:topic: Tables

.. index::
   triple: Sphinx; Syntax; Tables

Tables
######

For more details, see :dudir:`Table <table>` in |Docutils| or
:ref:`Tables Basics <sphinx:rst-tables>` and
:ref:`Tables Directives <sphinx:table-directives>`.

.. rst:directive:: table

   The :rst:`.. table::` directive serves as optional wrapper of the
   :ref:`concepts/tables:Grid Style` and :ref:`concepts/tables:Simple Style`.

.. rst:directive:: tabularcolumns

   The :rst:`.. tabularcolumns::` directive gives a ``column spec`` for
   the next table occurring in the source file. The spec is the second
   argument to the |LaTeX| :latex:`tabulary` package’s environment (which
   |Sphinx| uses to translate tables). For more details, see
   :rst:dir:`sphinx:tabularcolumns`.

:raw-latex:`\clearpage\phantomsection`

.. index::
   triple: Sphinx; Syntax; Grid Table

Grid Style
**********

For more details, see :duref:`Grid Tables <grid-tables>` in |Docutils|.

:the example:

   .. literalinclude:: tables/grid/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: tables/grid/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. index::
   triple: Sphinx; Syntax; Simple Table

Simple Style
************

For more details, see :duref:`Simple Tables <simple-tables>` in |Docutils|.

:the example:

   .. literalinclude:: tables/simple/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:which gives:

   .. include:: tables/simple/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. index::
   triple: Sphinx; Syntax; List Table

List Table
**********

.. rst:directive:: list-table

   For more details, see :dudir:`List Tables <list-table>` in |Docutils|.

   .. pull-quote::

      .. hint::

         For table content that needs a higher complexity than the
	 list table is able to support use the :rst:dir:`flat-table`.

   :the example:

      .. literalinclude:: tables/list/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: tables/list/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. index::
   triple: Sphinx; Syntax; CSV Table

CSV Table
*********

.. rst:directive:: csv-table

   For more details, see :dudir:`CSV Tables <csv-table>` in |Docutils|.

   .. pull-quote::

      .. hint::

         In almost all cases, :rst:dir:`csv-table` is the easiest
	 and most maintainable way to insert a table into a document.
	 It should be preferred unless there is a compelling reason
	 to use one of the other styles.

   :the example:

      .. literalinclude:: tables/csv/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: tables/csv/example.rsti

   Some of the options recognized are:

   .. rst:directive:option:: widths

      Contains a comma or space-separated list of relative column widths.
      The default is equal-width columns.

      The special value ``auto`` may be used by writers to decide whether
      to delegate the determination of column widths to the backend.

      In most cases, the best result is either the default or :rst:`auto`.
      If you're unsure, try it both ways and see which looks better to you.

   .. rst:directive:option:: header

      Contains column titles. It must use the same CSV format as the main
      CSV data.

   .. rst:directive:option:: delim

      Contains a one character string used to separate fields. Default value
      is comma. It must be a single character or Unicode code.

      The only reason to use something other than a comma is when copying
      large blocks of content from another source that uses a different style.
      If you are creating new table content yourself, use the comma.

      :the example:

         .. literalinclude:: tables/csv/delim/example.rsti
            :end-before: .. Local variables:
            :language: rst
            :linenos:

      :which gives:

         .. include:: tables/csv/delim/example.rsti

   .. rst:directive:option:: align

      It specifies the horizontal alignment of the table. It can be
      :rst:`left`, :rst:`right` or :rst:`center`.

      :the example:

         .. literalinclude:: tables/csv/align/example.rsti
            :end-before: .. Local variables:
            :language: rst
            :linenos:

      :which gives:

         .. include:: tables/csv/align/example.rsti

   .. rst:directive:option:: url

      Contains an Internet URL reference to a CSV data file.

   .. rst:directive:option:: file

      Contains the local file system path to a CSV data file.

      :the example:

         .. literalinclude:: tables/csv/srcfile/example.rsti
            :end-before: .. Local variables:
            :language: rst
            :linenos:

      :which gives:

         .. include:: tables/csv/srcfile/example.rsti

      :which needs:

         The example above processed the following CSV file content:

         .. literalinclude:: tables/csv/srcfile/example.csv
            :caption: CSV example file (tables/csv/srcfile/example.csv)
            :language: none
            :linenos:

.. pull-quote::

   .. note::

      There is no support for checking that the number of columns in
      each row is the same. However, this directive supports CSV
      generators that do not insert "empty" entries at the end of
      short rows, by automatically adding empty entries.

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
