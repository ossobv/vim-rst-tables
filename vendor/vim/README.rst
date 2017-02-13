==========
python-vim
==========

*Original:* `<https://github.com/hacosta/python-vim>`_


Want to quickly test the output of a function, so you open up your
trusty python REPL and start typing away.

After a while you need nested for loops, or want to save a copy of the
stuff you wrote. Or copy just a bit of code from your project.

Here's where python-vim comes in, it allows you to run a vim() session
inside your REPL env, after you save your code, it will get executed,
don't worry! you'll still have access to everything you defined inside
your vim session.


Usage
-----

.. code-block:: console

    $ python3
    >>> from vim import vim
    >>> vim()

Vim session opens, type your code here, save and exit.

.. code-block:: python

    foo = 'bar'
    for i in foo:
        print(i)

Output::

    >>> vim()
    ...
    b
    a
    r
    >>> foo
    'bar'


Pro Tip
-------

Add this to your .pythonrc file::

    from vim import vim


Changes
-------

- Original code by Hector Acosta (@hacosta) in 2014. BSD License.
- Updated for Python3 by Walter Doekes (@wdoekes) in 2017.
