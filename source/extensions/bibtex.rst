:topic: BibTeX Citations

.. index::
   triple: Sphinx; Extension; BibTeX Citations

BibTeX Citations
################

:PyPI Package:   https://pypi.org/project/sphinxcontrib-bibtex/
:Documentation:  https://sphinxcontrib-bibtex.readthedocs.org/
:Git Repository: https://github.com/mcmtroffaes/sphinxcontrib-bibtex

Allowing |BibTeX| citations to be inserted into documentation via a
:rst:`.. bibliography::` directive, and a :rst:`:cite:` role, which work
similarly to |LaTeX|\ ’s :latex:`\begin{thebibliography} ...
\end{thebibliography}` environment and :latex:`\cite{cite_key}`
command. For formatting, the extension relies on |Pybtex|. It consists:

* :py:mod:`scbibtex:sphinxcontrib.bibtex`: |Sphinx| interface
* :py:mod:`scbibtex:sphinxcontrib.bibtex.roles`: Doctree roles
* :py:mod:`scbibtex:sphinxcontrib.bibtex.nodes`: Doctree nodes
* :py:mod:`scbibtex:sphinxcontrib.bibtex.directives`: Doctree directives
* :py:mod:`scbibtex:sphinxcontrib.bibtex.transforms`: Doctree transforms
* :py:mod:`scbibtex:sphinxcontrib.bibtex.cache`: Cached information

Create a citation to a bibliographic entry.

.. pull-quote::

   .. todo:: In the case of the |LaTeX|/|PDF| builder the usage of
             :rst:`:ref:`bibliography`` leads to an **invalid and
             unresolved reference**.

.. rst:role:: cite

   For more details, see :rst:role:`scbibtex:cite` role.

   :the example:

      .. code-block:: rst
         :linenos:

         See :cite:`sweigart2020automate` for an practical guide in Python.

   :which gives:

      See :cite:`sweigart2020automate` for an practical guide in Python.

For this sample you will need a corresponding bibliography for all cited
references.

.. rst:directive:: bibliography

   For more details, see :rst:dir:`scbibtex:bibliography` directive.

   :the example:

      .. code-block:: rst
         :linenos:

         .. bibliography:: bibtex/example.bib
            :style: ldspalpha
            :encoding: utf-8
            :all:

   :which gives:

      All entries are placed in the central document bibliography list,
      mostly on the end of the document.

      .. only:: html

         Here in |HTML| you got this list at :ref:`bibliography`.

   :which needs:

      The example above processed the following |BibTeX| file content:

      .. literalinclude:: bibtex/example.bib
         :caption: BibTeX example file (bibtex/example.bib)
         :language: bibtex
         :emphasize-lines: 1
         :start-at: @book
         :linenos:

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
