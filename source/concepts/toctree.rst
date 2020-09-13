:topic: Table of Contents Tree

.. index::
   triple: Sphinx; Syntax; Table of Contents Tree

Table of Contents Tree
######################

Now would be a good time to introduce the :rst:`.. toctree::`. One of the
main concepts in |Sphinx| is that it allows multiple pages to be combined
into a cohesive hierarchy. Since |reStructuredText| does not have facilities
to interconnect several documents, or split documents into multiple output
files, |Sphinx| uses a custom directive to add relations between the single
files the documentation is made of, as well as tables of contents.

The :rst:`.. toctree::` directive is the central element and a fundamental
part of this structure. Consider this example:

.. rst:directive:: toctree

   For more details, see :rst:dir:`sphinx:toctree` directive.

   :the example:

      .. code-block:: rst
         :linenos:

         .. toctree::
            :maxdepth: 2

            install
            support
            (many more files listed here)

   :which gives:

         ::

            index
            ├── install
            ├── support
            ├── (many more files here)
                ├── (many more sub-files here)

The above directive example will output a :abbr:`TOC (Table of Contents)` in
the page where it occurs, using the individual TOCs (including "sub-TOC trees")
of the files given in the directive body. The :rst:`:maxdepth: 2` argument
tells |Sphinx| to include 2 levels of headers in it's output. It will output
the 2 top-level headers of the pages listed; by default, all levels are
included. This also tells |Sphinx| that the other pages are sub-pages
of the current page, creating a "tree" structure of the pages.

This accomplishes two things:

* Tables of contents from all those files are inserted, with a maximum depth
  of argument :rst:`:maxdepth:`, that means one nested heading.
  :rst:`.. toctree::` directives in those files are also taken into account.
* |Sphinx| knows that the relative order of the files :file:`install`,
  :file:`support` and so forth, and it knows that they are children of the
  shown file, the library index. From this information it generates
  "next chapter", "previous chapter" and "parent chapter" links.

In the end, all files included in the build process must occur in (only) one
:rst:`.. toctree::` directive; |Sphinx| will emit a warning if it finds a file
that is not included, because that means that this file will not be reachable
through standard navigation.

The special file :file:`index.rst` at the root of the source directory is the
"root" of the TOC tree hierarchy; from it the "Contents" page is generated.

.. pull-quote::

   .. note::

      The TOC Tree is also used for generating the navigation elements
      inside |Sphinx|. It is quite important, and one of the most powerful
      concepts in |Sphinx|.

Sidebar navigation menu
***********************

The :file:`index.rst` file serves as a front-page to the documentation and
contains the main tables of content, defined using :rst:`.. toctree::`
directives. These :rst:`.. toctree::` directives control the sidebar
navigation menu. To add a new document to a table of content, add the file
name (without the :file:`.rst` extension) to the relevant list of file
names in :file:`index.rst` or any other (but only one) "sub-TOC trees".

Secondary sub-TOC trees
***********************

Collections of documents are mostly given their own table of content on an
individual page (see, for example: :doc:`../appendix` and :doc:`../glossary`).
In these cases, the page containing the :rst:`.. toctree::` serves as a sort
of intro page for the collection. That intro must, itself, be included in the
:ref:`concepts/toctree:Sidebar navigation menu`. The contents of a
:rst:`.. toctree::` appear as section links in another :rst:`.. toctree::` it
is included in. That is, if a :rst:`.. toctree::` in :file:`index.rst` lists
:rst:`.. glossary::`, and :file:`glossary.rst` has a :rst:`.. toctree::`, then
the contents of that second :rst:`.. toctree::` will appear in the
:ref:`concepts/toctree:Sidebar navigation menu`, as sub-items to
:doc:`../glossary`.

Indeed, this is precisely the case in this |project| document currently.

How this document uses main and secondary TOC
*********************************************

* Major topics get a :rst:`.. toctree::` in :file:`index.rst`

  Major topics include things like:

  * Each major parts (:doc:`../extensions`, :doc:`../themes`, |...|\ )
  * Large, general categories like Releases, Contributing, or Building

  Major topic tables of content include both sub-collection intro pages
  and also individual pages that don't fit into a sub-collection.
  
  The :rst:`:caption:` attribute of the :rst:`.. toctree::`
  directive may but not must defines the section label in the
  :ref:`concepts/toctree:Sidebar navigation menu`.


* Within a large topic, documents are grouped into collections of related
  pages, defined by a :rst:`.. toctree::` on a topic intro page.

  Intro pages (pages that contain secondary :rst:`.. toctree::` directives)
  may include additional content, introducing the collection or providing
  contextual way-finding. However, this is not always necessary or desirable.
  Use your judgment, and avoid stating things just for the sake of having
  some text. ("Here are the pages in this collection.")

  We also (very occasionally) include :rst:`.. toctree::` directives in
  sub-collection pages, such as:
  
  * :doc:`../extensions/bibtex`,
  * :doc:`../extensions/spelling`,
  * |...|
  * :doc:`../themes/rtd`,
  * |...|

.. pull-quote::

   .. tip::

      If it not obvious where a new document should appear in the
      navigation, the best practice is to simply ask about it in
      the GitHub issue driving the new page.

   .. note::

      For way-finding purposes, we sometimes create an |ul| of page
      links rather than a :rst:`.. toctree::` directive (for example,
      see :file:`index.rst`). We do this when using a :rst:`.. toctree::`
      would create redundant links in the :ref:`concepts/toctree:Sidebar
      navigation menu`.

.. |ul| replace::
   :ref:`concepts/lists:Unordered (bullet) lists`

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
