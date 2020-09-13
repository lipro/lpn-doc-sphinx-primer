:topic: External References

.. index::
   triple: Sphinx; Syntax; External Referencing

External References
###################

|Sphinx| also includes a number of predefined references for external concepts.
Things like |PEP|'s and |RFC|'s. You can read more about this in the |Sphinx|
:doc:`./naming/roles` section.

.. rst:role:: pep
.. rst:role:: rfc

   For more details, see :rst:role:`sphinx:pep` and :rst:role:`sphinx:rfc` role.

   :the example:

      .. literalinclude:: external-referencing/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: external-referencing/example.rsti

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
