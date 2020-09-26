:topic: PGF/TikZ LaTeX Pictures

.. index::
   triple: Sphinx; Extension; PGF/TikZ LaTeX Pictures

PGF/TikZ LaTeX Pictures
#######################

.. pull-quote::

   .. attention::

      Only practicable and usable for |HTML| and |LaTeX| builder.

:PyPI Package:   https://pypi.org/project/sphinxcontrib-tikz/
:Documentation:  http://sphinxcontrib-tikz.readthedocs.io/
:Git Repository: https://bitbucket.org/philexander/tikz

|Sphinx| extension, which enables the use of the |PGF/TikZ| |LaTeX| package
to draw nice pictures.

This extension relies on two software packages being installed
on your computer:

1. ``latex`` with the ``tikz`` and the ``amsmath`` packages
2. A software package that is able to convert a |PDF| to an image.
   Currently, four different ways of doing this conversion are
   supported, called conversion "suites". Below is a list for
   each suite what must be installed on your computer. Only one
   such suite need to be installed:

   * *pdf2svg* suite: ``pdf2svg`` (preferred, default)
   * *Netpbm* suite: ``pdftoppm`` (part of the *Poppler* |PDF| library)
     and ``pnmtopng`` (part of the *Netpbm* package)
   * *ImageMagick* suite: ``pdftoppm`` (part of the *Poppler* |PDF| library)
     and ``convert`` (part of the *ImageMagick* package)
   * *GhostScript* suite: ``ghostscript``

See :ref:`sctikz:configuration` in the extension documentation for more details.

.. only:: html or latex

   :raw-latex:`\clearpage\phantomsection`

   .. rst:role:: tikz

      For more details, see :ref:`sctikz:usage` in the extension documentation.

      .. rubric:: inline content

      :the example:

         .. literalinclude:: tikz/inline/example.rsti
            :end-before: .. Local variables:
            :language: rst
            :linenos:

      :which gives:

         .. include:: tikz/inline/example.rsti

   .. rst:directive:: tikz

      For more details, see :ref:`sctikz:usage` in the extension documentation.

      .. rubric:: explicit markup

      :the example:

         .. literalinclude:: tikz/explicit/example.rsti
            :end-before: .. Local variables:
            :language: rst
            :linenos:

      :which gives:

         .. include:: tikz/explicit/example.rsti

      :raw-latex:`\clearpage\phantomsection`

      .. rubric:: from source file

      :the example:

         .. literalinclude:: tikz/srcfile/example.rsti
            :end-before: .. Local variables:
            :language: rst
            :linenos:

      :which gives:

         .. include:: tikz/srcfile/example.rsti

      :which needs:

         The example above comes from the `Control system principles`_
         web page and processed the following TikZ file content:

         .. literalinclude:: tikz/srcfile/ctrloop.tex
            :caption: TikZ example file (tikz/srcfile/ctrloop.tex)
            :end-before: %Local variables:
            :language: latex
            :linenos:

.. _`Control system principles`:
   http://www.texample.net/tikz/examples/control-system-principles

:raw-latex:`\clearpage\phantomsection`

Examples
********

PGF/TikZ
========

:CTAN Package:   https://ctan.org/pkg/pgf
:Documentation:  http://mirrors.ctan.org/graphics/pgf/base/doc/pgfmanual.pdf
:Documentation:  http://cremeronline.com/LaTeX/minimaltikz.pdf
:Git Repository: https://github.com/pgf-tikz/pgf

:CTAN Package:   https://ctan.org/pkg/visualtikz
:Documentation:  http://mirrors.ctan.org/info/visualtikz/VisualTikZ.pdf

.. only:: html or latex

   :the example: Shapes and symbols. [#]_

      .. rst-class:: centered
      .. tikz:: Shapes and symbols
         :include: tikz/pgftikz/shapesyms.tex
         :libs: arrows.meta,backgrounds,calc,fit,positioning,shapes.symbols

   :the example: Shapes absolut and in a matrix positioned. [#]_

      .. rst-class:: centered
      .. tikz:: Shapes absolut and in a matrix positioned
         :include: tikz/pgftikz/matrix.tex
         :libs: arrows.meta,shapes,positioning,matrix,fit,backgrounds

   :raw-latex:`\clearpage\phantomsection`

   :the tutorial: Creating Flowcharts. [#]_

      .. rst-class:: centered
      .. tikz:: Geometrical shapes in a flowchart
         :include: tikz/pgftikz/flowchart.tex
         :libs: arrows,calc,positioning,shapes.geometric,shapes.symbols,shapes.misc

      Live demo at `sharelatex
      <https://www.sharelatex.com/project/52205bbce77a8bec1415bf38>`_.

   :raw-latex:`\clearpage\phantomsection`

   :the example: Design of an eye in TikZ. [#]_

      .. rst-class:: centered
      .. tikz:: Constructive but realistic eye
         :include: tikz/pgftikz/fancyeye.tex
         :libs: calc,decorations.pathmorphing

   :the example:

      Time-frequency correspondence of the Fourier transform. [#]_

      .. rst-class:: centered
      .. tikz:: Fourier transformation illustrated
         :include: tikz/pgftikz/fourier.tex

   :the example:

      Show constructive interferences in the time domain. [#]_

      .. rst-class:: centered
      .. tikz:: Constructive interferences
         :include: tikz/pgftikz/interference.tex

   .. rubric:: Footnotes

   .. [#] Indication of provenance: :stackxtex:`a/518945`
          (user194703, Dec 2 '19 at 15:56)
   .. [#] Indication of provenance: :stackxtex:`a/435856`
          (:stackxtex:`J Leon V. <u/154390>`, BSD, MIT, Beerware licences)
   .. [#] Indication of provenance:
          `LaTeX Graphics using TikZ: A Tutorial for Beginners (Part 3)—Creating Flowcharts <https://de.overleaf.com/learn/latex/LaTeX_Graphics_using_TikZ:_A_Tutorial_for_Beginners_(Part_3)%E2%80%94Creating_Flowcharts>`_
          (Josh Cassidy, August 2013)
   .. [#] Indication of provenance: :stackxtex:`a/94087`
          (:stackxtex:`JLDiaz <u/12571>`)
   .. [#] Indication of provenance: :stackxtex:`a/127401`
          (:stackxtex:`Jake <u/2552>`)
   .. [#] Indication of provenance: :stackxtex:`a/162263`
          (:stackxtex:`Thomas <u/42660>`)

:raw-latex:`\clearpage\phantomsection`

CircuiTikZ
==========

:CTAN Package:   https://ctan.org/pkg/circuitikz
:Documentation:  http://mirrors.ctan.org/graphics/pgf/contrib/circuitikz/doc/circuitikzmanual.pdf
:Git Repository: https://github.com/circuitikz/circuitikz

.. only:: html or latex

   :the example: Full differential Op-Amp stabilization principles. [#]_

      .. rst-class:: centered
      .. tikz:: Full differential Op-Amp stabilization principles
         :include: tikz/circuitikz/opamp-fullstab.tex

   :the example: Inverting Op-Amp principles. [#]_

      .. rst-class:: centered
      .. tikz:: Inverting Op-Amp principles
         :include: tikz/circuitikz/opamp-inv.tex
         :libs: arrows.meta,decorations.markings

   :raw-latex:`\clearpage\phantomsection`

   :the example: Drawing MOSFET in TikZ. [#]_

      .. rst-class:: centered
      .. tikz:: General n-type MOSFET
         :include: tikz/circuitikz/nmos-fet.tex
         :libs: patterns

   :the example: NE555 timer as "Dee-Dah" siren. [#]_

      .. rst-class:: centered
      .. tikz:: NE555 timer as "Dee-Dah" siren
         :include: tikz/circuitikz/ne555-deedah.tex
         :libs: arrows.meta,decorations.markings

   :raw-latex:`\clearpage\phantomsection`

   :the example: Breadboard with aligned DIP chips. [#]_

      .. rst-class:: centered
      .. tikz:: Breadboard with NE555 timer as "Dee-Dah" siren
         :include: tikz/circuitikz/breadboard.tex
         :libs: arrows.meta,backgrounds,calc,decorations.pathmorphing

   :raw-latex:`\clearpage\phantomsection`

   :the example: 64 Lead Quad Flat Package. [#]_

      .. rst-class:: centered
      .. tikz:: LPC2144/2146/2148 pin assignment on LQFP64
         :include: tikz/circuitikz/lpc214x-lqfp64.tex

      .. pull-quote::

         .. attention::

            Native support only since CircuiTikZ V0.9 (Oct 2019).

            .. seealso::

	       `CircuiTikZ change log`_

   .. rubric:: Footnotes

   .. [#] Indication of provenance: :stackxtex:`q/82797`
          (:stackxtex:`Kit <u/791>`)
   .. [#] Indication of provenance: :stackxtex:`a/441787`
          (:stackxtex:`J Leon V. <u/154390>`, BSD, MIT, Beerware licences)
   .. [#] Indication of provenance:
          http://wesleythoneycutt.com/drawing-mosfet-in-tikz/
          (by Wesley T. Honeycutt)
   .. [#] Indication of provenance: :stackxtex:`a/435123`
          (:stackxtex:`J Leon V. <u/154390>`, BSD, MIT, Beerware licences)
   .. [#] Indication of provenance: :stackxtex:`q/493239`
          (:stackxtex:`Anshul Singhvi <u/162839>`)
   .. [#] Indication of provenance: :stackxtex:`a/202449`
          (:stackxtex:`John Kormylo <u/34505>`)

.. _`CircuiTikZ change log`:
   https://github.com/circuitikz/circuitikz/blob/master/CHANGELOG.md

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
