:topic: Semantic Descriptions and References

.. index::
   triple: Sphinx; Syntax; Semantic Descriptions and Referencing

Semantic Descriptions and References
####################################

|Sphinx| also has much more powerful semantic referencing capabilities,
which knows all about software development concepts.

Say you're creating a |CLI| application. You can define the name of the
executable application :rst:dir:`sphinx:program` and its
:rst:dir:`sphinx:option` and :rst:dir:`sphinx:envvar` quite easily.

.. rst:directive:: program
.. rst:directive:: option
.. rst:directive:: envvar

   For more details, see :rst:dir:`sphinx:program`, :rst:dir:`sphinx:option`
   and :rst:dir:`sphinx:envvar` directive.

   :the example:

      .. literalinclude:: semantic-referencing/program/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: semantic-referencing/program/example.rsti

That can now also be referenced quite simply.

.. rst:role:: program
.. rst:role:: option
.. rst:role:: envvar

   For more details, see :rst:role:`sphinx:program`, :rst:role:`sphinx:option`
   and :rst:role:`sphinx:envvar` role.

   :the example:

      .. literalinclude:: semantic-referencing/options/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: semantic-referencing/options/example.rsti

|Sphinx| includes a large number of these semantic types, including:

* :ref:`sphinx:c-domain` (name **c**):
  :rst:dir:`sphinx:c:namespace`,
  :rst:dir:`sphinx:c:struct`,
  :rst:dir:`sphinx:c:var`,
  :rst:dir:`sphinx:c:function`,
  |...|
* :ref:`sphinx:cpp-domain` (name **cpp**):
  :rst:dir:`sphinx:cpp:namespace`,
  :rst:dir:`sphinx:cpp:class`,
  |...|
* The |JavaScript| Domain (name **js**):
  :rst:dir:`sphinx:js:module`,
  :rst:dir:`sphinx:js:class`,
  |...|
* The |Python| Domain (name **py**):
  :rst:dir:`sphinx:py:module`,
  :rst:dir:`sphinx:py:class`,
  |...|
* The |reStructuredText| Domain (name **rst**):
  :rst:dir:`sphinx:rst:directive`,
  :rst:dir:`sphinx:rst:role`,
  |...|

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
