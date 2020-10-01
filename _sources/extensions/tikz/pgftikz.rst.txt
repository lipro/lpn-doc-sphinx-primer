:topic: PGF/TikZ Examples

.. index::
   triple: Sphinx; Extension; PGF/TikZ Examples

PGF/TikZ
########

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

.. only:: not html and not latex

   .. attention:: Not applicable for this type of Sphinx builder!

.. only:: html

   .. include:: /extensions/tikz/pgftikz-html.rsti

.. only:: latex

   .. include:: /extensions/tikz/pgftikz-latex.rsti

.. only:: html or latex

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

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
