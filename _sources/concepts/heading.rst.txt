:topic: Parts, Chapters, Titles, Sections

.. index::
   triple: Sphinx; Syntax; Header

Parts, Chapters, Titles, Sections
#################################

Every |Sphinx| document has multiple level of headings.
:duref:`Section headers <sections>` are created by underlining (and optionally
overlining) the section title with a punctuation character, at least as long
as the text.

Normally, there are no heading levels assigned to certain characters as the
structure is determined from the succession of headings. However, for this
documentation, here is a suggested convention as covered in the |Sphinx|
:ref:`sphinx:rst-primer` to use them in this order:

* ``#`` for title -- with overline, for parts
* ``*`` for subtitle -- with overline, for chapters
* ``=``, for sections
* ``-``, for subsections
* ``^``, for subsubsections
* ``=``, for paragraphs

They give structure to the document, which is used in navigation and in the
display in all output formats. The part section header is not used at all. All
regular documents starts with a title heading underlined by ``#``. Therefore
the specific names part, chapter, section, |...|\  might not match the actual
context. Generally we speak about "sections" (or "section headings" or
"section markers").

.. pull-quote::

   .. note::

      With |reStructuredText|, there is no leaving out a section level.
      If you write a chapter it is not possible to continue with a paragraph.
      Instead the next section must be of the type title.

      If you try to do it overwise (chapter 1 ``*`` with overline |CRT|
      paragraph ``"``), the "paragraph" is treated as a "title". And if
      you continue by another chapter in the same file (chapter 2 ``*``
      with overline |CRT| title ``#``), :program:`sphinx-build` got
      confused and at least produces a warning (*Title level inconsistent*)
      and possibly renders the result incorrectly.

:raw-latex:`\clearpage\phantomsection`

:the convention:

   .. code-block:: rst
      :linenos:

      ####################################
      Part -- Number Signs above and below
      ####################################

      with overline, for parts

      ************************************
      Chapter -- Asterisks above and below
      ************************************

      with overline, for chapters

      Title -- Number Signs
      #####################

      Suptitle -- Asterisks
      *********************

      Section -- Equal Signs
      ======================

      Subsection -- Hyphens
      ---------------------

      Subsubsection -- Circumflex
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^

      Paragraph -- Double Quotes
      """"""""""""""""""""""""""

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
