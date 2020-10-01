:topic: Spelling Checker

.. index::
   triple: Sphinx; Extension; Spelling Checker

Spelling Checker
################

:PyPI Package:   https://pypi.org/project/sphinxcontrib-spelling/
:Documentation:  https://sphinxcontrib-spelling.readthedocs.io/
:Git Repository: https://github.com/sphinx-contrib/spelling

Spelling checker for |Sphinx|. It uses |PyEnchant| to produce a report showing
misspelled words.

:Features:

   1. Supports multiple source languages using the standard enchant
      dictionaries.
   2. Supports project-specific dictionaries for localized jargon and
      other terminology that may not appear in the global dictionaries.
   3. Suggests alternatives to words not found in the dictionary,
      when possible.

It consists:

* :doc:`scspelling:index`: spelling checker for |Sphinx|

Private Dictionaries
********************

For more details, see :doc:`scspelling:customize` section *Private Dictionaries*.

.. rst:directive:: spelling

   The :rst:`.. spelling::` directive can be used to create a list of words
   known to be spelled correctly within a single file. For example, if a
   document refers to a person or project by name, the name can be added
   to the list of known words for just that single document.

   When a more common list of words is needed, related to check multiple
   document at once, the :confval:`spelling_word_list_filename` variable
   should be set properly.

.. confval:: spelling_word_list_filename

   That is a list specifying files containing a list of words known to be
   spelled correctly but that do not appear in the referred language
   dictionary. The files should contain one word per line. Refer to the
   |PyEnchant| tutorial for details.

:raw-latex:`\clearpage\phantomsection`

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
