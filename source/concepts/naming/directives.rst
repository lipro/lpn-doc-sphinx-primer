:topic: Directives

.. index::
   triple: Sphinx; Syntax; Directives

Directives
##########

A :term:`sphinx:directive` is a generic block of :doc:`../explicit-markup`.
Besides roles, it is one of the extension mechanisms of |reStructuredText|,
and |Sphinx| makes heavy use of it.

Basically, a directive consists of a **name**, **arguments**, **options** and
**content**. Keep this terminology in mind, it is used in section
:doc:`../explicit-markup` describing custom directives. Looking at this
example, that allows marking a block of content with special meaning. 

.. rubric:: basic directive syntax looks like this

:the example:

   .. code-block:: rst
      :linenos:

      .. directive:: arg1 arg2 ...
         :option1: value
         :option2: value
         :option5: value
         ...

         Multiline content of the directive,
         ...

   *This line is no longer part of the block controlled by the directive.*

   ``directive``
      That is the *directive name*. It is given two arguments here.

   ``arg1, arg2, ...``
      *Arguments*. The last argument can contain spaces (depending on the
      directive implementation).

   ``:option0:, :option1:, ... :option9:``
      *Options* are optional. As you can see, options are given in the lines
      immediately following the arguments and indicated by the colons.

   ``Multiline content of the directive,``
      The *directive content* follows after a blank line and is indented
      relative to the directive start.

Directives are supplied not only by |Docutils|, but |Sphinx| and custom
extensions can add their own. Directives are written as a block.

|Docutils| supports the following directives (incomplete list):

* :doc:`../admonition`:
  :dudir:`attention`, :dudir:`caution`, :dudir:`danger`,
  :dudir:`error`, :dudir:`hint`, :dudir:`important`, :dudir:`note`,
  :dudir:`tip`, :dudir:`warning` and the generic
  :dudir:`admonition <admonitions>`. (Most themes style only "note" and
  "warning" specially.)

* :doc:`../images`:

  - :dudir:`image`
  - :dudir:`figure` (an image with caption and optional legend)

* Additional body elements:

  - :dudir:`contents <table-of-contents>` (a local, i.e. for the current file
    only, table of contents)
  - :dudir:`section numbering <automatic-section-numbering>` (automatically)
  - :dudir:`container` (a container with a custom class, useful to generate an
    outer ``<div>`` in |HTML|)
  - :dudir:`rubric` (a heading without relation to the document sectioning)
  - :dudir:`topic`, :dudir:`sidebar` (special highlighted body elements)
  - :dudir:`parsed-literal` (literal block that supports inline markup)
  - :dudir:`epigraph` (a block quote with optional attribution line)
  - :dudir:`highlights`, :dudir:`pull-quote` (block quotes with their own
    class attribute)
  - :dudir:`compound <compound-paragraph>` (a compound paragraph)

* Special :doc:`../tables`:

  - :dudir:`table` (a table with title)
  - :dudir:`csv-table` (a table generated from comma-separated values)
  - :dudir:`list-table` (a table generated from a list of lists)

* Special directives and :doc:`../reuse/includes`:

  - :dudir:`raw <raw-data-pass-through>` (include raw target-format markup)
  - :dudir:`include` (include |reStructuredText| from another file) -- in
    |Sphinx|, when given an absolute include file path, this directive takes
    it as relative to the source directory
  - :dudir:`class` (assign a class attribute to the next element) [#]_

* |HTML| specifics:

  - :dudir:`meta`
    (generation of |HTML| ``<meta>`` tags, see also :ref:`html-meta` below)
  - :dudir:`title <metadata-document-title>` (override document title)

* Influencing markup:

  - :dudir:`default-role` (set a new default role)
  - :dudir:`role` (create a new role)

  Since these are only per-file, better use |Sphinx|'s facilities for setting
  the :confval:`default_role`.

* References and :doc:`../reuse/substitutions`:

  - :dudir:`target footnotes <target-notes>` (for each external URL target)
  - :dudir:`replacement text <replacement-text>` (for a substitution)
  - :dudir:`unicode characters <unicode-character-codes>` (used in substitution)

.. pull-quote::

   .. warning::

      Do *not* use the directives :dudir:`sectnum`,
      :dudir:`header` and :dudir:`footer`.

.. seealso::

   * Refer to :ref:`sphinx:rst-directives`
     for directives provided by |Docutils|.
   * Refer to :doc:`sphinx:usage/restructuredtext/directives`
     for directives added by |Sphinx|.

.. rubric:: Footnotes

.. [#] When the default domain contains a **class** directive, this directive
       will be shadowed. Therefore, |Sphinx| re-exports it as **rst-class**.

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
