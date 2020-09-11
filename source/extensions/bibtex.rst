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
command. It consists:

* :py:mod:`scbibtex:sphinxcontrib.bibtex`: Sphinx interface
* :py:mod:`scbibtex:sphinxcontrib.bibtex.roles`: Doctree roles
* :py:mod:`scbibtex:sphinxcontrib.bibtex.nodes`: Doctree nodes
* :py:mod:`scbibtex:sphinxcontrib.bibtex.directives`: Doctree directives
* :py:mod:`scbibtex:sphinxcontrib.bibtex.transforms`: Doctree transforms
* :py:mod:`scbibtex:sphinxcontrib.bibtex.cache`: Cached information

Create a citation to a bibliographic entry.

.. todo:: activate "BibTeX Citations" extension.

.. code-block:: rst

   .. rst:role:: cite

      For more details, see :rst:role:`scbibtex:cite` role.

      :the example:

         .. code-block:: rst
            :linenos:

            See :cite:`juh2014swdocwspx` for an introduction to Sphinx.

      :which gives:

         See :cite:`juh2014swdocwspx` for an introduction to Sphinx.

   For this sample you will need a corresponding bibliography for all cited
   references.

   .. rst:directive:: bibliography

      For more details, see :rst:dir:`scbibtex:bibliography` directive.

      :the example:

         .. code-block:: rst
            :linenos:

            .. bibliography:: bibliography.bibtex
               :style: kcsalpha
               :encoding: utf
               :all:

      :which gives:

         .. only:: html or man or texinfo or text

            .. rubric:: Documentation with Sphinx

         .. only:: latex

            All entries in the central document bibliography list, mostly on the
            end of the document.

         .. bibliography:: bibliography.bibtex
            :style: kcsalpha
            :encoding: utf
            :all:

      :which needs:

         The example above processed the following BibTeX file content:

         .. literalinclude:: bibliography.bibtex
            :caption: BibTeX example file (bibliography.bibtex)
            :language: bibtex
            :emphasize-lines: 1
            :start-at: @book
            :linenos:

   .. spelling::

      Hasecke

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
