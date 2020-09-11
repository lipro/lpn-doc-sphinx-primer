:topic: Images and Figures

.. index::
   triple: Sphinx; Syntax; Images
   triple: Sphinx; Syntax; Figures

Images and Figures
##################

SVG graphics only
*****************

All vector graphics or diagrams should be SVG files. This helps us keep our
graphic conversion tooling simple, and generally results in higher-quality
representation.

Whenever possible, you should generate your graphics as SVGs rather than
converting to SVGs from another format. That avoids bitmap images embedded
in a SVG container. The goal of SVG usage is to hold vector graphic as long
as possible, from the editor up to the presentation. If you have to start in
another vector graphic format use lossless vector formats whenever possible.
These include EPS/PS, AI, DXF, EMF/WMF, or some special XML vector graphics
schemes. In any case avoid embedded bitmaps, as this is a lossy format for
vector informations that does not replicate scaling very well.

PNG images only
***************

All still bitmap images or photos should be PNG files. This helps us keep our
image compression tooling simple, and generally results in higher-quality
screenshots.

Whenever possible, you should generate your images as PNGs rather than
converting to PNGs from another format. If you have to start in another
format, use lossless formats whenever possible. These include BMP, GIF,
and TIFF. Avoid JPG/JPEG if possible, as this is a lossy format that does
not replicate screenshots very well.

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

Inserting with captions
***********************

Use :rst:`.. figure::` directive to markup a graphic or image with a caption
(see :dudir:`Figure <figure>`).

.. code-block:: rst

  .. figure:: {file-with-directory-same-as-for image}.*
    :alt: Alt text. Every image should have descriptive alt text.

    The rest of the indented content will be the (optional) caption.
    This can be a short sentence or multiline paragraph.

Captions can contain any other complex reStructuredText markup. Further
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

Inserting inline
****************

To information on creating inline images, see
:ref:`concepts/reuse/substitutions:Inline image`.

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
