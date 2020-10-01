:topic: Admonitions

.. index::
   triple: Sphinx; Syntax; Admonitions

Admonitions
###########

.. index::
   triple: Sphinx; Admonitions; Generic

Generic Admonition
******************

The :duref:`Generic admonition <generic-admonition>` is a simple
titled admonition. The title may be anything the author desires.
The author-supplied title is also used as a "classes" attribute
value after being converted into a valid identifier form. As well
as this implicitly behavior the :rst:`:class:` option value can
set to any implemented specific type and overrides the computed
"classes" attribute value.

.. rst:directive:: admonition

   :the example:

      .. literalinclude:: admonition/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: admonition/example.rsti

.. index::
   triple: Sphinx; Admonitions; Specific

Specific Admonitions
********************

:duref:`Specific Admonitions <specific-admonitions>` are specially
marked "topics" that can appear anywhere an ordinary body element
can. Typically, an admonition is rendered as an offset block in a
document, sometimes outlined or shaded, with a title matching the
admonition type. The following admonition directives have been
implemented.

.. index::
   triple: Sphinx; Admonitions; Attention

Attention Admonition
====================

.. rst:directive:: attention

   :the example:

      .. literalinclude:: admonition/attention/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: admonition/attention/example.rsti

.. index::
   triple: Sphinx; Admonitions; Caution

Caution Admonition
==================

.. rst:directive:: caution

   :the example:

      .. literalinclude:: admonition/caution/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: admonition/caution/example.rsti

.. index::
   triple: Sphinx; Admonitions; Danger

Danger Admonition
=================

.. rst:directive:: danger

   :the example:

      .. literalinclude:: admonition/danger/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: admonition/danger/example.rsti

.. index::
   triple: Sphinx; Admonitions; Error

Error Admonition
================

.. rst:directive:: error

   :the example:

      .. literalinclude:: admonition/error/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: admonition/error/example.rsti

.. index::
   triple: Sphinx; Admonitions; Hint

Hint Admonition
===============

.. rst:directive:: hint

   :the example:

      .. literalinclude:: admonition/hint/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: admonition/hint/example.rsti

.. index::
   triple: Sphinx; Admonitions; Important

Important Admonition
====================

.. rst:directive:: important

   :the example:

      .. literalinclude:: admonition/important/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: admonition/important/example.rsti

.. index::
   triple: Sphinx; Admonitions; Note

Note Admonition
===============

.. rst:directive:: note

   For more details, see :rst:dir:`sphinx:note` directive.

   :the example:

      .. literalinclude:: admonition/note/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: admonition/note/example.rsti

.. index::
   triple: Sphinx; Admonitions; Tip

Tip Admonition
==============

.. rst:directive:: tip

   :the example:

      .. literalinclude:: admonition/tip/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: admonition/tip/example.rsti

.. index::
   triple: Sphinx; Admonitions; Warning

Warning Admonition
==================

.. rst:directive:: warning

   For more details, see :rst:dir:`sphinx:warning` directive.

   :the example:

      .. literalinclude:: admonition/warning/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: admonition/warning/example.rsti

.. index::
   triple: Sphinx; Admonitions; Additional

Sphinx Additional Admonitions
*****************************

.. index::
   triple: Sphinx; Admonitions; Seealso

Seealso Admonition
==================

.. rst:directive:: seealso

   Many sections include a list of references to module documentation
   or external documents. These lists are created using the
   :rst:dir:`sphinx:seealso` directive.

   :the example:

      .. literalinclude:: admonition/seealso/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: admonition/seealso/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. spelling::

   Neque
   porro
   quisquam
   Lorem
   ipsum
   dolor
   sit
   amet
   consectetur
   adipiscing
   elit
   Vivamus
   mattis
   commodo
   eros
   quis
   posuere
   enim
   lobortis
   quis
   Nullam
   ut
   tempus
   nibh

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
