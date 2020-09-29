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

:Homepage:       `PGF/TikZ Home`_ (`VisualTikZ Home`_)
:CTAN Package:   `PGF/TikZ Package`_ (`VisualTikZ Package`_)
:Documentation:  `PGF/TikZ Manual`_ (`VisualTikZ Manual`_)
:Documentation:  `PGF/TikZ Introduction`_ by `Jacques Crémer`_
:Git Repository: `PGF/TikZ Master Branch`_

|PGF| is a macro package for creating graphics. It is platform- and
format-independent and works together with the most important |TeX|
backend drivers. It comes with a user-friendly syntax layer called
|TikZ|. Its usage is similar to `pstricks`_ and the standard picture
environment. |PGF| works with plain |TeX|, |LaTeX|, and ConTeXt. Unlike
`pstricks`_, it can produce either |PS| or |PDF| output.

.. _`Jacques Crémer`: https://www.tse-fr.eu/people/jacques-cremer
.. _`pstricks`: https://ctan.org/pkg/pstricks-base

.. only:: html or latex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   .. rubric:: |pgftikz.shapesyms.tit|

   |pgftikz.shapesyms.tex| [#]_, in |pgftikz.shapesyms.ref|.

   .. _tikz/pgftikz/shapesyms:
   .. rst-class:: centered
   .. tikz:: Shapes and symbols
      :include: /extensions/tikz/pgftikz/shapesyms.tex
      :libs: arrows.meta,backgrounds,calc,fit,positioning,shapes.symbols

   :raw-latex:`\FloatBarrier\vfill`

   ----

   :raw-latex:`\clearpage\phantomsection`

   .. rubric:: |pgftikz.matrix.tit|

   |pgftikz.matrix.tex| [#]_, in |pgftikz.matrix.ref|.

   .. _tikz/pgftikz/matrix:
   .. rst-class:: centered
   .. tikz:: Shapes absolut and in a matrix positioned
      :include: /extensions/tikz/pgftikz/matrix.tex
      :libs: arrows.meta,backgrounds,fit,matrix,positioning,shapes

   :raw-latex:`\FloatBarrier\vfill`

   ----

   .. rubric:: |pgftikz.fancyeye.tit|

   |pgftikz.fancyeye.tex| [#]_, in |pgftikz.fancyeye.ref|.

   .. _tikz/pgftikz/fancyeye:
   .. rst-class:: centered
   .. tikz:: Constructive but realistic eye
      :include: /extensions/tikz/pgftikz/fancyeye.tex
      :libs: calc,decorations.pathmorphing

   :raw-latex:`\FloatBarrier\vfill`

   ----

   :raw-latex:`\clearpage\phantomsection`

   .. rubric:: |pgftikz.fourier.tit|

   |pgftikz.fourier.tex| [#]_, in |pgftikz.fourier.ref|.

   .. _tikz/pgftikz/fourier:
   .. rst-class:: centered
   .. tikz:: Time-frequency correspondence of the Fourier transform
      :include: /extensions/tikz/pgftikz/fourier.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   .. rubric:: |pgftikz.interference.tit|

   |pgftikz.interference.tex| [#]_, in |pgftikz.interference.ref|.

   .. _tikz/pgftikz/interference:
   .. rst-class:: centered
   .. tikz:: Show constructive interferences in the time domain
      :include: /extensions/tikz/pgftikz/interference.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   :raw-latex:`\clearpage\phantomsection`

   .. rubric:: |pgftikz.modula-am.tit|

   |pgftikz.modula-am.tex| [#]_, in |pgftikz.modula-am.ref|.

   .. _tikz/pgftikz/modula-am:
   .. rst-class:: centered
   .. tikz:: Graphical derivation of an amplitude modulated signal
      :include: /extensions/tikz/pgftikz/modula-am.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   .. rubric:: |pgftikz.interference.tit|

   |pgftikz.interference.tex| [#]_, in |pgftikz.interference.ref|.

   .. _tikz/pgftikz/modula-fm:
   .. rst-class:: centered
   .. tikz:: Graphical derivation of a frequency modulated signal
      :include: /extensions/tikz/pgftikz/modula-fm.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   :raw-latex:`\clearpage\phantomsection`

   .. rubric:: |pgftikz.flowchart.tit|

   |pgftikz.flowchart.tex| [#]_, in |pgftikz.flowchart.ref|.

   .. _tikz/pgftikz/flowchart:
   .. rst-class:: centered
   .. tikz:: Geometrical shapes in a flowchart
      :include: /extensions/tikz/pgftikz/flowchart.tex
      :libs: arrows,calc,positioning,shapes.geometric,shapes.symbols,shapes.misc

   :raw-latex:`\FloatBarrier\vfill`

   ----

   .. rubric:: Footnotes

   .. [#] Indication of provenance: :stackxtex:`a/518945`
          (user194703, Dec 2 '19 at 15:56)
   .. [#] Indication of provenance: :stackxtex:`a/435856`
          (:stackxtex:`J Leon V. <u/154390>`, BSD, MIT, Beerware licences)
   .. [#] Indication of provenance: :stackxtex:`a/94087`
          (:stackxtex:`JLDiaz <u/12571>`)
   .. [#] Indication of provenance: :stackxtex:`a/127401`
          (:stackxtex:`Jake <u/2552>`)
   .. [#] Indication of provenance: :stackxtex:`a/162263`
          (:stackxtex:`Thomas <u/42660>`)
   .. [#] Indication of provenance:
          `Amplitude modulation (AM)`_ (Petar Veličković, July 2016)
   .. [#] Indication of provenance:
          `Frequency modulation (FM)`_ (Petar Veličković, July 2016)
   .. [#] Indication of provenance:
          `TikZ Tutorial for Beginners (Part 3)—Creating Flowcharts`_
          (Josh Cassidy, August 2013)

.. _`Amplitude modulation (AM)`:
   https://github.com/PetarV-/TikZ/tree/master/Amplitude%20modulation
.. _`Frequency modulation (FM)`:
   https://github.com/PetarV-/TikZ/tree/master/Frequency%20modulation
.. _`TikZ Tutorial for Beginners (Part 3)—Creating Flowcharts`:
   https://de.overleaf.com/learn/latex/LaTeX_Graphics_using_TikZ:_A_Tutorial_for_Beginners_(Part_3)%E2%80%94Creating_Flowcharts

:raw-latex:`\clearpage\phantomsection`

CircuiTikZ
==========

:Homepage:       `CircuiTikZ Home`_
:CTAN Package:   `CircuiTikZ Package`_
:Documentation:  `CircuiTikZ Manual`_
:Git Repository: `CircuiTikZ Master Branch`_

|CircuiTikZ| provides a set of macros for naturally typesetting electrical
and electronic networks, designed as a tool that is easy to use by native
to a lean |LaTeX| syntax. It has therefore been based on the very impressive
|PGF/TikZ| package.

.. only:: html or latex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   .. rubric:: |circuitikz.opamp-fullstab.tit|

   |circuitikz.opamp-fullstab.tex| [#]_, in |circuitikz.opamp-fullstab.ref|.

   .. _tikz/circuitikz/opamp-fullstab:
   .. rst-class:: centered
   .. tikz:: Full differential Op-Amp stabilization principles
      :include: /extensions/tikz/circuitikz/opamp-fullstab.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   :raw-latex:`\clearpage\phantomsection`

   .. rubric:: |circuitikz.opamp-inv.tit|

   |circuitikz.opamp-inv.tex| [#]_, in |circuitikz.opamp-inv.ref|.

   .. _tikz/circuitikz/opamp-inv:
   .. rst-class:: centered
   .. tikz:: Detailed description of inverting Op-Amp principles
      :include: /extensions/tikz/circuitikz/opamp-inv.tex
      :libs: arrows.meta,decorations.markings

   :raw-latex:`\FloatBarrier\vfill`

   ----

   .. rubric:: |circuitikz.nmos-fet.tit|

   |circuitikz.nmos-fet.tex| [#]_, in |circuitikz.nmos-fet.ref|.

   .. _tikz/circuitikz/nmos-fet:
   .. rst-class:: centered
   .. tikz:: Drawing MOSFET chip structure in TikZ
      :include: /extensions/tikz/circuitikz/nmos-fet.tex
      :libs: patterns

   :raw-latex:`\FloatBarrier\vfill`

   ----

   :raw-latex:`\clearpage\phantomsection`

   .. rubric:: |circuitikz.ne555-deedah.tit|

   |circuitikz.ne555-deedah.tex| [#]_, in |circuitikz.ne555-deedah.ref|.

   .. _tikz/circuitikz/ne555-deedah:
   .. rst-class:: centered
   .. tikz:: NE555 timer as "Dee-Dah" siren
      :include: /extensions/tikz/circuitikz/ne555-deedah.tex
      :libs: arrows.meta,decorations.markings

   :raw-latex:`\FloatBarrier\vfill`

   ----

   :raw-latex:`\clearpage\phantomsection`

   .. rubric:: |circuitikz.breadboard.tit|

   |circuitikz.breadboard.tex| [#]_, in |circuitikz.breadboard.ref|.

   .. _tikz/circuitikz/breadboard:
   .. rst-class:: centered
   .. tikz:: Breadboard with NE555 timer as "Dee-Dah" siren
      :include: /extensions/tikz/circuitikz/breadboard.tex
      :libs: arrows.meta,backgrounds,calc,decorations.pathmorphing

   :raw-latex:`\FloatBarrier\vfill`

   ----

   :raw-latex:`\clearpage\phantomsection`

   .. rubric:: |circuitikz.lpc214x-lqfp64.tit|

   |circuitikz.lpc214x-lqfp64.tex| [#]_, in |circuitikz.lpc214x-lqfp64.ref|.

   Native support only since CircuiTikZ V0.9 (Oct 2019).
   **See also:** `CircuiTikZ change log`_

   .. _tikz/circuitikz/lpc214x-lqfp64:
   .. rst-class:: centered
   .. tikz:: LPC2144/2146/2148 pin assignment on LQFP64
      :include: /extensions/tikz/circuitikz/lpc214x-lqfp64.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

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

TikZ-Timing
===========

:CTAN Package:   `TikZ-Timing Package`_
:Documentation:  `TikZ-Timing User Guide`_
:Git Repository: `TikZ-Timing Master Branch`_

|TikZ-Timing| is a |TikZ| extension with macros and an environment to generate
timing diagrams (digital waveforms) without much effort.

.. only:: html or latex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   .. rubric:: |tikztiming.pcinst-tick.tit|

   |tikztiming.pcinst-tick.tex| [#]_, in |tikztiming.pcinst-tick.ref|.

   .. _tikz/tikztiming/pcinst-tick:
   .. rst-class:: centered
   .. tikz:: Program counter and instruction tick
      :include: /extensions/tikz/tikztiming/pcinst-tick.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   .. rubric:: |tikztiming.divider-line.tit|

   |tikztiming.divider-line.tex| [#]_, in |tikztiming.divider-line.ref|.

   .. _tikz/tikztiming/divider-line:
   .. rst-class:: centered
   .. tikz:: Signal interconnections and dividers
      :include: /extensions/tikz/tikztiming/divider-line.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   :raw-latex:`\clearpage\phantomsection`

   .. rubric:: |tikztiming.colored-cells.tit|

   |tikztiming.colored-cells.tex| [#]_, in |tikztiming.colored-cells.ref|.

   .. _tikz/tikztiming/colored-cells:
   .. rst-class:: centered
   .. tikz:: SPI vs. UART with arbitrary colored data cells
      :include: /extensions/tikz/tikztiming/colored-cells.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   .. rubric:: |tikztiming.spi-opmodes.tit|

   |tikztiming.spi-opmodes.tex| [#]_, in |tikztiming.spi-opmodes.ref|.

   .. _tikz/tikztiming/spi-opmodes:
   .. rst-class:: centered
   .. tikz:: Serial Peripheral Interface operating modes
      :include: /extensions/tikz/tikztiming/spi-opmodes.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   :raw-latex:`\clearpage\phantomsection`

   .. rubric:: |tikztiming.pci-read-irqack.tit|

   |tikztiming.pci-read-irqack.tex|, in |tikztiming.pci-read-irqack.ref|.

   PCI timing diagrams with reference to version 2.2 of the
   PCI specification [#]_.

   .. _tikz/tikztiming/pci-read-irqack:
   .. rst-class:: centered
   .. tikz:: PCI Read and Interrupt Acknowledge
      :include: /extensions/tikz/tikztiming/pci-read-irqack.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   .. rubric:: |tikztiming.gn4124-pdwreq.tit|

   |tikztiming.gn4124-pdwreq.tex|, in |tikztiming.gn4124-pdwreq.ref|.

   Packet decoder timing diagram with reference to the
   Gennum GN4124 to Wishbone bridge user guide [#]_.

   .. _tikz/tikztiming/gn4124-pdwreq:
   .. rst-class:: centered
   .. tikz:: GN4124 Packet Decoder Write Request
      :include: /extensions/tikz/tikztiming/gn4124-pdwreq.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   .. rubric:: Footnotes

   .. [#] Indication of provenance: :stackxtex:`a/30906`
          (:stackxtex:`sdaau <u/2595>` and :stackxtex:`Count Zero <u/7417>`)
   .. [#] Indication of provenance: :stackxtex:`a/236091`
          (:stackxtex:`Symbol 1 <u/51022>`)
   .. [#] Indication of provenance: :stackxtex:`a/255027`
          (:stackxtex:`Gonzalo Medina <u/3954>`)
   .. [#] Indication of provenance: :stackxtex:`a/290027`
          (:stackxtex:`Habi <u/828>`)
   .. [#] Indication of provenance:
          https://nathantypanski.com/blog/2014-10-29-tikz-timing.html
   .. [#] Indication of provenance:
          https://github.com/terpstra/gn4124-core/

:raw-latex:`\clearpage\phantomsection`

TikZ-UML
========

:Homepage:       `TikZ-UML Project`_
:Documentation:  `TikZ-UML User Guide`_

|TikZ-UML| is a |TikZ| extension to manage common |UML| diagrams. The primary
goal was to propose an alternative to the `pst-uml`_ package, as |TikZ| is an
alternative itself to PSTricks.

.. _`pst-uml`: https://ctan.org/pkg/pst-uml

.. only:: html or latex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   .. rubric:: |tikzuml.usecasediag.tit|

   |tikzuml.usecasediag.tex|, in |tikzuml.usecasediag.ref|.

   .. _tikz/tikzuml/usecasediag:
   .. rst-class:: centered
   .. tikz:: Use case diagram example
      :include: /extensions/tikz/tikzuml/usecasediag.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   :raw-latex:`\clearpage\phantomsection`

   .. rubric:: |tikzuml.classdiag.tit|

   |tikzuml.classdiag.tex|, in |tikzuml.classdiag.ref|.

   .. _tikz/tikzuml/classdiag:
   .. rst-class:: centered
   .. tikz:: Class diagram example
      :include: /extensions/tikz/tikzuml/classdiag.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   :raw-latex:`\clearpage\phantomsection`

   .. rubric:: |tikzuml.statediag.tit|

   |tikzuml.statediag.tex|, in |tikzuml.statediag.ref|.

   .. _tikz/tikzuml/statediag:
   .. rst-class:: centered
   .. tikz:: State-machine diagram example
      :include: /extensions/tikz/tikzuml/statediag.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   :raw-latex:`\clearpage\phantomsection`

   .. rubric:: |tikzuml.seqdiag.tit|

   |tikzuml.seqdiag.tex|, in |tikzuml.seqdiag.ref|.

   .. _tikz/tikzuml/seqdiag:
   .. rst-class:: centered
   .. tikz:: Sequence diagram example
      :include: /extensions/tikz/tikzuml/seqdiag.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

   :raw-latex:`\clearpage\phantomsection`

   .. rubric:: |tikzuml.componentdiag.tit|

   |tikzuml.componentdiag.tex|, in |tikzuml.componentdiag.ref|.

   .. _tikz/tikzuml/componentdiag:
   .. rst-class:: centered
   .. tikz:: Component diagram example
      :include: /extensions/tikz/tikzuml/componentdiag.tex

   :raw-latex:`\FloatBarrier\vfill`

   ----

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
