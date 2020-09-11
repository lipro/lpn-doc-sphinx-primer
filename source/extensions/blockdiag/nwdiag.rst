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

.. todo:: activate "Network Diagram" extension.

Directive Body Diagram
**********************

.. rst:directive:: nwdiag

   For more details, see :doc:`bldiag:nwdiag/sphinxcontrib` in the
   extension demonstration and the :file:`README.rst` in the extension
   Git repository.

   :the example:

      .. literalinclude:: nwdiag-directive-body-example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   .. code-block:: rst

      :which gives:

         .. include:: nwdiag-directive-body-example.rsti

Description Table
*****************

:the example:

   .. literalinclude:: nwdiag-description-table-example.rsti
      :end-before: .. Local variables:
      :language: rst
      :linenos:

.. code-block:: rst

   :which gives:

      .. include:: nwdiag-description-table-example.rsti

Include Diagram
***************

Network
=======

:the example:

   .. code-block:: rst
      :linenos:

      .. nwdiag:: nw.diag
         :caption: Peer networks and grouping nodes (Network Diagram example)
         :align: center
         :scale: 75
         :width: 640

.. code-block:: rst

   :which gives:

      .. nwdiag:: nw.diag
         :caption: Peer networks and grouping nodes (Network Diagram example)
         :align: center
         :scale: 75
         :width: 640

:which needs:

   The example above comes from the original
   :ref:`bldiag:nwdiag-sample-diagrams`
   web page and processed the following file content:

   .. literalinclude:: nw.diag
      :caption: Network Diagram example file (nw.diag)
      :language: dot
      :linenos:

Rack
====

.. rst:directive:: rack

   For more details, see :doc:`bldiag:nwdiag/sphinxcontrib` in the
   extension demonstration and the :file:`README.rst` in the extension
   Git repository.

   :the example:

      .. code-block:: rst
         :linenos:

         .. rackdiag:: rack.diag
            :caption: Multiple racks with multiple and blocked units (Rack Diagram example)
            :align: center
            :height: 480

   .. code-block:: rst

      :which gives:

         .. rackdiag:: rack.diag
            :caption: Multiple racks with multiple and blocked units (Rack Diagram example)
            :align: center
            :height: 480

   :which needs:

      The example above comes from the original
      :ref:`bldiag:rackdiag-sample-diagrams`
      web page and processed the following file content:

      .. literalinclude:: rack.diag
         :caption: Rack Diagram example file (rack.diag)
         :language: bash
         :linenos:

      .. FIXME: :language: dot (Bash is being abused here)

Packet
======

.. rst:directive:: packet

   For more details, see :doc:`bldiag:nwdiag/sphinxcontrib` in the
   extension demonstration and the :file:`README.rst` in the extension
   Git repository.

   :the example:

      .. code-block:: rst
         :linenos:

         .. packetdiag:: packet.diag
            :caption: Structure of TCP Header (Packet Diagram example)
            :align: center
            :width: 640

   .. code-block:: rst

      :which gives:

         .. packetdiag:: packet.diag
            :caption: Structure of TCP Header (Packet Diagram example)
            :align: center
            :width: 640

   :which needs:

      The example above comes from the original
      :ref:`bldiag:packetdiag-sample-diagrams`
      web page and processed the following file content:

      .. literalinclude:: packet.diag
         :caption: Packet Diagram example file (packet.diag)
         :language: bash
         :linenos:

      .. FIXME: :language: dot (Bash is being abused here)

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
