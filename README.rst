=================================================================
vim-rst-tables-py3
=================================================================

*Original:* `<https://github.com/nvie/vim-rst-tables>`_


Installation
------------

1. Install the prerequisites::

      python3 setup.py install

      (or better yet, fetch it through a debian package or pip;
      in which case you might also be able to skip step 2 and 3)

2. Make the project::

      python3 build.py

3. Copy the file ``ftplugin/rst_tables.vim`` to your ``~/.vim/ftplugin``
   directory.

   **If your vim is not already configured to source scripts in this
   directory**, make sure to add the appropriate command to your
   ``.vimrc``::

      source "~/.vim/ftplugin/rst_tables.vim"

4. Optionally run tests::

      sudo apt-get install python3-mock  # or pip3 install mock
      PYTHONPATH=`pwd`/src python3 -m unittest discover

5. Optionally create debian-package for easy installation::

      dpkg-buildpackage -us -uc -sa


Usage
-----

Creating a new table
~~~~~~~~~~~~~~~~~~~~

1. Open a reStructuredText file
2. Create some kind of table outline::

      This is paragraph text *before* the table.

      Column 1  Column 2
      Foo  Put two (or more) spaces as a field separator.
      Bar  Even very very long lines like these are fine, as long as you do not put in line endings here.
      Qux  This is the last line.

      This is paragraph text *after* the table.

2. Put your cursor somewhere in the table.
3. To create the table, press :kbd:`,,c` (or :kbd:`\\c` if vim's
   :kbd:`&lt;Leader&gt;` is set to the default value; yes *double*
   backslash). The output will look something like this::

      This is paragraph text *before* the table.

      +----------+---------------------------------------------------------+
      | Column 1 | Column 2                                                |
      +==========+=========================================================+
      | Foo      | Put two (or more) spaces as a field separator.          |
      +----------+---------------------------------------------------------+
      | Bar      | Even very very long lines like these are fine, as long  |
      |          | as you do not put in line endings here.                 |
      +----------+---------------------------------------------------------+
      | Qux      | This is the last line.                                  |
      +----------+---------------------------------------------------------+

      This is paragraph text *after* the table.


Re-flowing an existing table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes, you may have a column that contains enough data that your
table is a little hard to work with.  To fix that kind of problem,
you can define the column width you would prefer, and re-flow your table.

1. Change the number of "---" signs in the top row of your table to match
   the column widths you would prefer.
2. Put your cursor somewhere in the table.
3. Press :kbd:`,,f` to re-flow the table (or :kbd:`\\f` if vim's
   :kbd:`&lt;Leader&gt;` is set to the default value; yes *double*
   backslash; see also the ``:map`` command).


Changes
-------

- Original code by Vincent Driessen (@nvie), lastly in 2015,
  probably BSD License.
- Updated for Python3 by Walter Doekes (@wdoekes) in 2017. Added vendor
  dependencies for easier install. Added debian packaging rules.
