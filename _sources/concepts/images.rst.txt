:topic: Images and Figures

.. index::
   triple: Sphinx; Syntax; Images
   triple: Sphinx; Syntax; Figures

Images and Figures
##################

SVG Graphics only
*****************

All vector graphics or diagrams should be |SVG| files. This helps us keep our
graphic conversion tooling simple, and generally results in higher-quality
representation. |SVG| graphics with an parameterized opacity (transparency)
should be possible as well as an animated |SVG|, see
:numref:`images-transparent-vector` and :numref:`images-animated-vector`.

.. tabularcolumns:: CC
.. list-table::
   :widths: 50, 50
   :align: center

   * - .. figure:: images/transparent-vector.svg
          :name: images-transparent-vector
          :figclass: align-center
          :align: center
          :height: 200px

          Example of transparent SVG [#]_

     - .. figure:: images/animated-vector.svg
          :name: images-animated-vector
          :figclass: align-center
          :align: center
          :height: 200px

          Example of animated SVG [#]_

Whenever possible, you should generate your graphics as |SVG| rather than
converting to |SVG| from another format. That avoids bitmap raster images
embedded in a |SVG| container. The goal of |SVG| usage is to hold vector
graphic as long as possible, from the editor up to the presentation. If you
have to start in another vector graphic format **use lossless vector formats**
whenever possible. These include |EPS/PS|, |AI|, |DXF|, |EMF/EMZ|, |WMF/WMZ|
or some special |XML| vector graphics schemes. In any case avoid embedded
bitmaps, as this is a lossy format for vector informations that does not
replicate scaling very well.
:numref:`images-rast-vs-vect` demonstrates differences between bitmapped
raster and vector graphics. The bitmap raster is composed of a fixed set
of pixels, while the vector is composed of a fixed set of shapes. In the
picture, scaling the bitmap reveals the pixels while scaling the vector
image preserves the shapes.

:raw-latex:`\clearpage\phantomsection`

.. figure:: images/rast-vs-vect.svg
   :name: images-rast-vs-vect
   :figclass: align-center
   :align: center
   :width: 320px

   Demonstration of differences between bitmapped raster and
   vector images. [#]_

.. pull-quote::

   **Bitmap raster images are good for photographic images or screenshots
   but not for stencils, sketches, diagrams or graphs and often they do not
   support transparency.**

   —Superuser - :superuser:`JPEG vs. PNG vs. BMP vs. GIF vs. SVG <q/53600>`

   .. pull-quote::

      Raster graphics are resolution dependent, meaning they cannot scale
      up to an arbitrary resolution without loss of apparent quality. This
      property contrasts with the capabilities of vector graphics, which
      easily scale up to the quality of the device rendering them. Raster
      graphics deal more practically than vector graphics with photographs
      and photo-realistic images, while vector graphics often serve better
      for typesetting or for graphic design.

      —Wikipedia - :wikien:`Raster graphics <Raster_graphics#Resolution>`

      Vector graphics have the unique advantage over raster graphics in
      that the points, lines, and curves may be scaled up or down to any
      resolution with no aliasing.

      —Wikipedia - :wikien:`Vector graphics <Vector_graphics>`

.. rubric:: Footnotes

.. [#] Indication of provenance: :steamcoded:`atom1.svg`
       (public domain for teachers and students learning to code)
.. [#] Indication of provenance: :steamcoded:`atom.svg`
       (public domain for teachers and students learning to code)
.. [#] Indication of provenance: :wikimedia:`6/6b/Bitmap_VS_SVG.svg`
       (licensed under `CC-BY-SA-2.5`_)

:raw-latex:`\clearpage\phantomsection`

PNG Images only
***************

All still bitmap raster images or photos should be |PNG| files. This helps
us keep our image compression tooling simple, and generally results in
higher-quality screenshots. |PNG| images with an 8-bit transparency channel
should be possible as well as an animated |PNG|, see
:numref:`images-transparent-bitmap` and :numref:`images-animated-bitmap`.

.. tabularcolumns:: CC
.. list-table::
   :widths: 50, 50
   :align: center

   * - .. figure:: images/transparent-bitmap.png
          :name: images-transparent-bitmap
          :figclass: align-center
          :align: center
          :height: 200px

          Example of transparent PNG [#]_

     - .. figure:: images/animated-bitmap.png
          :name: images-animated-bitmap
          :figclass: align-center
          :align: center
          :height: 200px

          Example of animated PNG [#]_

Whenever possible, you should generate your images as |PNG| rather than
converting to |PNG| from another format. If you have to start in another
format, **use lossless formats** whenever possible. These include |BMP/DIB|,
|GIF|, and |TIFF|. Avoid |JPEG/JFIF| if possible, as this is a lossy format
that does not replicate screenshots very well.
:numref:`images-lossless-vs-lossy` comparing lossy compression in |JPEG| with
lossless compression in |PNG|: the |JPEG| artifacts can be easily visible in the
background of this kind of image data, where the |PNG| image has solid color.

:raw-latex:`\clearpage\phantomsection`

.. figure:: images/lossless-vs-lossy.png
   :name: images-lossless-vs-lossy
   :figclass: align-center
   :align: center
   :width: 320px

   Demonstration of differences between lossy encoding and
   lossless method. [#]_

.. pull-quote::

   **JPEG is good for photographic images but not for sharp transitions
   and does not support transparency.**

   —Wikipedia - :wikien:`PNG comparison with JPEG <Portable_Network_Graphics#JPEG>`

   .. pull-quote::

      The |JPEG| format can produce a smaller file than |PNG| for photographic
      (and photo-like) images, since |JPEG| uses a lossy encoding method
      specifically *designed for photographic image data*. Using |PNG| instead
      of a high-quality |JPEG| for such images would result in a large increase
      in file size with negligible gain in quality. In comparison, when storing
      images that contain text, line art, or graphics -- images with sharp
      transitions and large areas of solid color -- the |PNG| format can
      compress image data more than |JPEG| can. Additionally, |PNG| is lossless,
      while |JPEG| produces visual artifacts around high-contrast areas.

      |JPEG|'s lossy compression also suffers from generation loss, where
      repeatedly decoding and re-encoding an image to save it again causes
      a loss of information each time, degrading the image. This does not
      happen with repeated viewing or copying, but only if the file is edited
      and saved over again. Because |PNG| is lossless, it is suitable for
      storing images to be edited.

      Where an image contains both *sharp transitions* and *photographic parts*,
      a choice must be made between the two effects:

.. rubric:: Footnotes

.. [#] Indication of provenance:
       :wikimedia:`4/47/PNG_transparency_demonstration_1.png`
       (licensed under `CC-BY-SA-3.0`_)
.. [#] Indication of provenance:
       :wikimedia:`1/14/Animated_PNG_example_bouncing_beach_ball.png`
       (released into the public domain by its author, Holger Will)
.. [#] Indication of provenance:
       :superuser:`a/55706`, http://lbrandy.com/assets/jpg_vs_png2.png
       (licensed under `CC-BY-SA-3.0`_)

:raw-latex:`\clearpage\phantomsection`

Inserting
*********

To place an graphic or image in a document, use the :rst:`.. image::` directive
(see :dudir:`Image <image>`).

.. code-block:: rst

  .. image:: /img/{absolut-document-subdirectory}/{file}.svg
    :alt: Alt text. Every image should have descriptive alt text.

  .. image:: {relative-document-subdirectory}/{file}.*
    :alt: Alt text. Every image should have descriptive alt text.

Note the literal asterisk (``*``) at the end, in place of a file extension.
Use the asterisk, and omit the file extension
(see :doc:`sphinx:usage/restructuredtext/basics`, section *Images*).

.. rst:directive:: image

   :the example:

      .. literalinclude:: images/image/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: images/image/example.rsti

:raw-latex:`\clearpage\phantomsection`

Inserting with Captions
***********************

Use :rst:`.. figure::` directive to markup a graphic or image with a caption
(see :dudir:`Figure <figure>`).

.. code-block:: rst

  .. figure:: {file-with-directory-same-as-for image}.*
    :alt: Alt text. Every image should have descriptive alt text.

    The rest of the indented content will be the (optional) caption.
    This can be a short sentence or multiline paragraph.

Captions can contain any other complex |reStructuredText| markup. Further
paragraphs after the caption will be the (optional) legend which are
also arbitrary body elements.

.. rst:directive:: figure

   :the example:

      .. literalinclude:: images/figure/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: images/figure/example.rsti

Inserting Inline
****************

To information on creating inline images, see
:ref:`concepts/reuse/substitutions:Inline image`.

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
