:topic: Email Obfuscate

.. index::
   triple: Sphinx; Extension; Email Obfuscate

Email Obfuscate
###############

.. attention::

   Only practicable and usable for |HTML| builder.

:PyPI Package:   https://pypi.org/project/sphinxcontrib-email/
:Documentation:  https://github.com/sphinx-contrib/email/blob/master/README.rst
:Git Repository: https://github.com/sphinx-contrib/email
:Python 3 Fixes: https://github.com/rexut/sphinxcontrib-email/tree/python3-fixes

.. todo:: activate "Email Obfuscate" extension.

To obfuscate an email address use something like:

   ::

      :email:`Name Surname <user@myplace.org>`
      :email:`Name Surname (user@myplace.org)`

   That renders as ``Name Surname`` with the appropriate mailto link.

   ::

      :email:`user@myplace.org`

   That renders as ``user@myplace.org`` with the appropriate mailto link.

.. rst:role:: email

   :the example:

      .. literalinclude:: email-example.rsti
         :end-before: .. Local variables:
         :language: rst
         :linenos:

   .. code-block:: rst

      :which gives:

         .. include:: email-example.rsti

.. Local variables:
   coding: utf-8
   mode: text
   mode: rst
   End:
   vim: fileencoding=utf-8 filetype=rst :
