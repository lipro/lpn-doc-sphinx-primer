:topic: |project|

.. Li-Pro.Net Sphinx Primer documentation master file, created by
   sphinx-quickstart on Sat Sep  5 12:37:04 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _home:

#########
|project|
#########

.. include:: docsummary.rsti

.. only:: latex

   .. include:: doclegal.rsti
   .. include:: docversions.rsti

:raw-latex:`\cleardoublepage\phantomsection`

.. ...........................................................................

.. topic:: PREAMBLE

   .. rst-class:: centered

   .. rubric:: |about|

   Excerpts from the `Sphinx Tutorial by Eric Holscher`_ and
   `Documentation Style Guide by Bareos GmbH & Co. KG and others`_.
   See :cite:`hasecke2019sphinx` for an introduction to |Sphinx|.

   This documentation is built using |Sphinx|, a static-site generator designed
   to create structured, semantic, and internally consistent documentation.
   Source documents are written in |reStructuredText|, a semantic, extensible
   markup syntax similar to Markdown. |reStructuredText| is a
   `better tool than Markdown for documentation`_.

   * :duuser:`reStructuredText Primer <quickstart>` --
     introduction to reStructuredText

     * :duuser:`reStructuredText Quick Reference <quickref>`
     * :duuser:`reStructuredText 1-page cheat sheet <cheatsheet>`

   * :doc:`Sphinx Markup <sphinx:usage/restructuredtext/index>` --
     detailed guide to Sphinx's markup concepts and reStructuredText extensions

   * :doc:`spxmemo:index` --
     serve as quick reference for reStructuredText and Sphinx syntax

   .. note::

      |Sphinx| and |reStructuredText| can be very flexible. For the sake of
      consistency and maintainability, this how to guide is *highly opinionated*
      about how documentation source files are organized and marked up.

:raw-latex:`\cleardoublepage\phantomsection`

.. ...........................................................................

.. toctree::
   :caption: Table of Contents
   :numbered: 3
   :maxdepth: 4
   :hidden:
   :includehidden:

   concepts
   extensions
   themes
   cheatsheet

:raw-latex:`\appendix`

.. toctree::
   :caption: Appendices
   :titlesonly:
   :hidden:

   appendix
   glossary

.. toctree::
   :caption: Lists and References
   :titlesonly:
   :hidden:

   indexlol
   indexlot
   indexlof
   indexloe
   indexlod
   indexloi
   bibliography

.. ...........................................................................

.. only:: not latex and not html

   .. include:: doclegal.rsti

.. only:: not latex

   .. include:: docversions.rsti

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
