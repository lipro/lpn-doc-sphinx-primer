:topic: Index

.. index::
   triple: Sphinx; Syntax; Index

Index
#####

.. rst:directive:: index

   For more details, see :rst:dir:`sphinx:index` directive.

   Some roles and directives do already create indices automatically.

   However, there is also an explicit directive available, to make the index
   more comprehensive and enable index entries in documents where information
   is not mainly contained in information units.

   The directive is :rst:`.. index::` and contains one or more index entries
   Each entry consists of a type and a value, separated by a colon.
   For example:

   .. code-block:: rst

      .. index::
         single: execution; context
         triple: module; search; path

.. rst:role:: index

   For more details, see :rst:role:`sphinx:index` role.

   While the :rst:dir:`index` directive is a block-level markup and links to
   the beginning of the next paragraph, there is also a corresponding role
   that sets the link target directly where it is used.

   The content of the role can be a simple phrase, which is then kept in the
   text and used as an index entry. It can also be a combination of text and
   index entry, styled like with explicit targets of cross-references. In that
   case, the "target" part can be a full entry as described for the directive
   above. For example:

   .. code-block:: rst

       This is a normal reST :index:`paragraph` that contains several
       :index:`index entries <pair: index; entry>`.

   .. pull-quote::

      .. note::

         The :rst:`:index:` role must contain text. This text will be
         printed and referenced by the index.

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
