:topic: Domains

.. index::
   triple: Sphinx; Syntax; Domains

Domains
#######

A :term:`sphinx:domain` is a collection of :doc:`explicit <../explicit-markup>`
and :doc:`inline <../inline-markup>` markup (|reStructuredText|
:doc:`./directives` and :doc:`./roles`) to describe and link to objects
belonging together, e.g. elements of a programming language. Directive and role
names in a domain have names like ``domain:name``, e.g.
:rst:`.. c:function:: int main(int argc, char **argv, char **env)` or
:rst:`:c:func:`main``.

An :term:`sphinx:object` is the basic building block of |Sphinx| documentation.
Every "object directive" (e.g. function or object) creates such a block; and
most objects can be cross-referenced to.

:ref:`sphinx:domains-std` collects all markup that does not warrant a domain
of its own. Its directives and roles are not prefixed with a domain name.

There is a set of directives allowing documenting command-line programs:

.. tabularcolumns:: \X{30}{100}|\X{40}{100}\X{35}{100}
.. list-table:: Sphinx directives for command-line programs
   :name: appendix-howto-spx-dom-std-cmd
   :widths: 30, 40, 30
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - short description
     - directive (target)
     - role (reference)
   * - :rst:dir:`Following document options for the program. <sphinx:program>`
     - :rst:`.. program:: name`
     -
   * - :rst:dir:`Describes a command line argument or switch. <sphinx:option>`
     - :rst:`.. option:: name args, ...`
     - :rst:`:option:`name arg``
   * - :rst:dir:`Describes an environment variable. <sphinx:envvar>`
     - :rst:`.. envvar:: name`
     - :rst:`:envvar:`name``

There is also a very generic object description directive, which is not
tied to any domain. This directive produces the same formatting as the
specific ones provided by domains, but does not create index entries
or cross-referencing targets:

.. tabularcolumns:: \X{30}{100}|\X{40}{100}\X{30}{100}
.. list-table:: Sphinx directives for unspecific objects without referencing
   :name: appendix-howto-spx-dom-std-unspec
   :widths: 30, 40, 30
   :class: longtable
   :align: center
   :width: 80 %
   :header-rows: 1

   * - short description
     - directive (target)
     - role (reference)
   * - :rst:dir:`Describes an unspecific element. <sphinx:describe>`
     - :rst:`.. describe:: text`
     -
   * - :rst:dir:`Describes an unspecific object. <sphinx:object>`
     - :rst:`.. object:: text`
     -

Originally, |Sphinx| was conceived for a single project, the documentation of
the |Python| language. Shortly afterwards, it was made available for everyone as
a documentation tool, but the documentation of |Python| modules remained deeply
built in -- the most fundamental directives, like function, were designed for
|Python| objects.

Since |Sphinx| has become somewhat popular, interest developed in using it for
many different purposes: |C/C++| projects, |JavaScript|, or even
|reStructuredText| markup (like in this documentation). The following specific
domains are provided by |Sphinx| (without additional extensions):

* :ref:`sphinx:c-domain` (name **c**)
* :ref:`sphinx:cpp-domain` (name **cpp**)
* The |JavaScript| Domain (name **js**)
* :ref:`sphinx:math-domain` (name **math**)
* The |Python| Domain (name **py**)
* The |reStructuredText| Domain (name **rst**)

.. :ref:`sphinx:js-domain`
.. :ref:`sphinx:python-domain`
.. :ref:`sphinx:rst-domain`

.. seealso::

   * Refer to :doc:`sphinx:usage/restructuredtext/domains`
     for domains provided by |Sphinx|.

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
