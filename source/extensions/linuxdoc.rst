:topic: LinuxDoc

.. index::
   triple: Sphinx; Extension; LinuxDoc

LinuxDoc
########

:Documentation:  https://return42.github.io/linuxdoc/
:Git Repository: https://github.com/return42/linuxdoc

The LinuxDoc library with extensions of the |Linux|-Kernel documentation,
you can use these extensions in common |Sphinx| projects. It consists:

* :py:mod:`lxdoc:linuxdoc.rstFlatTable`:
  the :rst:`.. flat-table::` reST-directive
* :py:mod:`lxdoc:linuxdoc.rstKernelDoc`:
  the :rst:`.. kernel-doc::` reST-directive
* :py:mod:`lxdoc:linuxdoc.kernel_include`:
  the :rst:`.. kernel-include::` reST-directive
* :py:mod:`lxdoc:linuxdoc.manKernelDoc`: the :program:`kernel-doc-man` builder
* :py:mod:`lxdoc:linuxdoc.cdomain`: replacement for the sphinx C-domain
* :py:mod:`lxdoc:linuxdoc.kfigure`: implements scalable image handling

Flat list table
***************

.. rst:directive:: flat-table

   .. seealso::

      :ref:`lxdoc:xref_table_concerns`: :ref:`lxdoc:rest-flat-table`

   The :rst:`.. flat-table::`` (FlatTable) is a double-stage list similar
   to the :rst:`.. list-table::`` with some additional features:

   * *column-span*: with the role :rst:`:cspan:`num`` a cell can be extended
     through additional columns
   * *row-span*: with the role :rst:`:rspan:`num`` a cell can be extended
     through additional rows
   * *auto-span*: rightmost cell of a table row over the missing cells on
     the right side of that table-row. With Option :rst:`:fill-cells:` this
     behavior can changed from auto span to auto fill, which automatically
     inserts (empty) cells instead of spanning the last cell.

   :options:

      .. rst:directive:option:: header-rows
         :type: integer

         count of header rows

      .. rst:directive:option:: stub-columns
         :type: integer

         count of stub columns

      .. rst:directive:option:: widths
         :type: list of integer

         widths of columns

      .. rst:directive:option:: fill-cells

         instead of auto-span missing cells, insert missing cells

   :roles:

      .. rst:role:: cspan

         **(integer)**: additional columns (*morecols*)

      .. rst:role:: rspan

         **(integer)**: additional rows (*morerows*)

The example below shows how to use this markup.  The first level of the staged
list is the *table-row*. In the *table-row* there is only one markup allowed,
the list of the cells in this *table-row*. Exception are *comments* ( ``..`` )
and *targets* (e.g. a ref to :ref:`row 2 of table's body <row body 2>`).

:the example:

   .. pull-quote::

      .. attention::

         **line 2:** The option :rst:`:class: longtable` will not interpreted
         from directive :rst:`.. flat-table::` and has no effects.

   .. literalinclude:: linuxdoc/flat-table/example.rsti
      :end-before: .. Local variables:
      :emphasize-lines: 2
      :language: rst
      :linenos:

:which gives:

   .. include:: linuxdoc/flat-table/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
