.. Li-Pro.Net Sphinx Primer documentation master file, created by
   sphinx-quickstart on Sat Sep  5 12:37:04 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:topic: |project|

.. _home:

#########
|project|
#########

.. only:: latex

   .. include:: doclegal.rsti
   .. include:: docversions.rsti

.. raw:: latex

   \cleardoublepage\phantomsection

.. ...........................................................................

.. topic:: PREAMBLE

   .. rst-class:: centered

   .. rubric:: |about|

   Excerpts from the `Sphinx Tutorial by Eric Holscher`_ and
   `Documentation Style Guide by Bareos GmbH & Co. KG and others`_.
   See [juh2019swdocwspx]_ for an introduction to Sphinx.

   This documentation is built using |Sphinx|, a static-site generator designed
   to create structured, semantic, and internally consistent documentation.
   Source documents are written in |reStructuredText|, a semantic, extensible
   markup syntax similar to Markdown.

   * :duuser:`reStructuredText Primer <quickstart>` --
     Introduction to reStructuredText

     * :duuser:`reStructuredText Quick Reference <quickref>`
     * :duuser:`reStructuredText 1-page cheat sheet <cheatsheet>`

   * :doc:`Sphinx Markup <sphinx:usage/restructuredtext/index>` --
     Detailed guide to Sphinx's markup concepts and reStructuredText extensions

   .. note::

      |Sphinx| and |reStructuredText| can be very flexible. For the sake of
      consistency and maintainability, this how to guide is *highly opinionated*
      about how documentation source files are organized and marked up.

.. toctree::
   :caption: Table of Contents
   :numbered: 3
   :maxdepth: 3
   :includehidden:

   sphinx/concepts
   sphinx/extensions
   sphinx/themes
   sphinx/cheatsheet

.. raw:: latex

    \appendix

.. toctree::
   :caption: Lists and References
   :titlesonly:
   :hidden:

   appendix
   glossary
   indexlol
   indexlot
   indexlof
   indexloe
   indexlod
   indexloi
   bibliography

.. only:: html or man or texinfo or text

   .. rubric:: Lists and References:

   * :doc:`/appendix`
   * :doc:`/glossary`
   * :doc:`/indexlol`
   * :doc:`/indexlot`
   * :doc:`/indexlof`
   * :doc:`/indexloe`
   * :doc:`/indexlod`
   * :doc:`/indexloi`
   * :doc:`/bibliography`
   * :ref:`genindex`
.. * :ref:`search`

.. ...........................................................................

.. only:: man or texinfo or text

   .. include:: doclegal.rsti

.. only:: html or man or texinfo or text

   .. include:: docversions.rsti

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
