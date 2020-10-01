:topic: Network Diagram

.. index::
   triple: Sphinx; Extension; Network Diagram

Network Diagram
###############

:doc:`bldiag:nwdiag/sphinxcontrib` is a |Sphinx| extension for embedding
network diagrams. You can embed network diagrams with the :rst:`.. nwdiag::`,
:rst:`.. rackdiag::` and :rst:`.. packetdiag::` directives.

:PyPI Package:   https://pypi.org/project/sphinxcontrib-nwdiag/
:Documentation:  http://blockdiag.com/en/nwdiag/sphinxcontrib.html
:Git Repository: https://github.com/blockdiag/sphinxcontrib-nwdiag

|Sphinx| extension for embedding network diagrams using
`nwdiag <https://github.com/blockdiag/nwdiag>`_.

:Features:

   1. Generate network-diagram from dot like text (basic feature).
   2. Multilingualism for node-label (utf-8 only).

:raw-latex:`\clearpage\phantomsection`

Directive Body Diagram
**********************

.. rst:directive:: nwdiag

   For more details, see :doc:`bldiag:nwdiag/sphinxcontrib` in the
   extension demonstration and the :file:`README.rst` in the extension
   Git repository.

   :the example:

      .. literalinclude:: nwdiag/directive-body/example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   :which gives:

      .. include:: nwdiag/directive-body/example.rsti

:raw-latex:`\clearpage\phantomsection`

Description Table
*****************

:the example:

   .. literalinclude:: nwdiag/description-table/example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

:raw-latex:`\clearpage\phantomsection`

:which gives:

   .. include:: nwdiag/description-table/example.rsti

:raw-latex:`\clearpage\phantomsection`

Include Diagram
***************

Network
=======

:the example:

   .. code-block:: rst
      :linenos:

      .. nwdiag:: nwdiag/example.diag
         :caption: Peer networks and grouping nodes (Network Diagram example)
         :align: center
         :scale: 75
         :width: 480

:which gives:

   .. nwdiag:: nwdiag/example.diag
      :caption: Peer networks and grouping nodes (Network Diagram example)
      :align: center
      :scale: 75
      :width: 480

:which needs:

   The example above comes from the original
   :ref:`bldiag:nwdiag-sample-diagrams`
   web page and processed the following file content:

   .. literalinclude:: nwdiag/example.diag
      :caption: Network Diagram example file (nwdiag/example.diag)
      :language: dot
      :linenos:

:raw-latex:`\clearpage\phantomsection`

Rack
====

.. rst:directive:: rack

   For more details, see :doc:`bldiag:nwdiag/sphinxcontrib` in the
   extension demonstration and the :file:`README.rst` in the extension
   Git repository.

   :the example:

      .. code-block:: rst
         :linenos:

         .. rackdiag:: rackdiag/example.diag
            :caption: Multiple racks with multiple and blocked units (Rack Diagram example)
            :align: center
            :height: 480

   :which gives:

      .. rackdiag:: rackdiag/example.diag
         :caption: Multiple racks with multiple and blocked units (Rack Diagram example)
         :align: center
         :height: 480

   :which needs:

      The example above comes from the original
      :ref:`bldiag:rackdiag-sample-diagrams`
      web page and processed the following file content:

      .. literalinclude:: rackdiag/example.diag
         :caption: Rack Diagram example file (rackdiag/example.diag)
         :language: bash
         :linenos:

      .. FIXME: :language: dot (Bash is being abused here)

:raw-latex:`\clearpage\phantomsection`

Packet
======

.. rst:directive:: packet

   For more details, see :doc:`bldiag:nwdiag/sphinxcontrib` in the
   extension demonstration and the :file:`README.rst` in the extension
   Git repository.

   :the example:

      .. code-block:: rst
         :linenos:

         .. packetdiag:: packetdiag/example.diag
            :caption: Structure of TCP Header (Packet Diagram example)
            :align: center
            :width: 480

   :which gives:

      .. packetdiag:: packetdiag/example.diag
         :caption: Structure of TCP Header (Packet Diagram example)
         :align: center
         :width: 480

   :which needs:

      The example above comes from the original
      :ref:`bldiag:packetdiag-sample-diagrams`
      web page and processed the following file content:

      .. literalinclude:: packetdiag/example.diag
         :caption: Packet Diagram example file (packetdiag/example.diag)
         :language: bash
         :linenos:

      .. FIXME: :language: dot (Bash is being abused here)

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
