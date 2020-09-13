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
representation.

Whenever possible, you should generate your graphics as |SVG|\ s rather than
converting to |SVG|\ s from another format. That avoids bitmap raster images
embedded in a |SVG| container. The goal of |SVG| usage is to hold vector
graphic as long as possible, from the editor up to the presentation.
:numref:`images-rast-vs-vect` demonstrats differences between bitmapped raster
and vector graphics. The bitmap raster is composed of a fixed set of pixels,
while the vector is composed of a fixed set of shapes.

.. figure:: images-rast-vs-vect.svg
   :name: images-rast-vs-vect
   :figclass: align-center
   :align: center
   :width: 320px

   Demonstration of differences between bitmapped raster and vector images.

In the picture, scaling the bitmap reveals the pixels while scaling the vector
image preserves the shapes.

If you have to start in another vector graphic format use lossless vector
formats whenever possible. These include |EPS/PS|, |AI|, |DXF|, |EMF/EMZ|,
|WMF/WMZ| or some special |XML| vector graphics schemes. In any case avoid
embedded bitmaps, as this is a lossy format for vector informations that
does not replicate scaling very well.

PNG Images only
***************

All still bitmap raster images or photos should be |PNG| files. This helps
us keep our image compression tooling simple, and generally results in
higher-quality screenshots. Animated |PNG| should also be possible, see
:numref:`images-animated`.

.. figure:: images-animated.png
   :name: images-animated
   :figclass: align-center
   :align: center
   :width: 160px

   Example of animated PNG

Whenever possible, you should generate your images as |PNG|\ s rather than
converting to |PNG|\ s from another format. If you have to start in another
format, use lossless formats whenever possible. These include |BMP/DIB|,
|GIF|, and |TIFF|. Avoid |JPEG/JFIF| if possible, as this is a lossy format
that does not replicate screenshots very well.

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

      .. literalinclude:: images-image-example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: images-image-example.rsti

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

      .. literalinclude:: images-figure-example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: images-figure-example.rsti

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
