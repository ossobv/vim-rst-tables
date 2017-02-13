===================================
vim_bridge - a Python-to-Vim bridge
===================================

*Original:* `<https://github.com/nvie/vim_bridge>`_


What is it?
-----------

*vim_bridge* is a Python-to-Vim bridge decorator that allows transparent calls
to Python functions in native Vim scripts.


Usage
-----

In a Vim script, decorate your Python functions as follows to expose them as
native Vim callables.  Both arguments and return values are casted so it should
be transparent::

    python3 << endpython
    from vim_bridge import bridged

    @bridged
    def SayHello(first, last):
        return "Hello, %s %s!" % (first, last)

    endpython

    " Now call directly into the Python function!
    echo SayHello("John", "Doe")
    " prints "Hello, John Doe!"


Supported
---------

The following data types have proven to work:

* Strings
* Integers
* Lists
* Exceptions


More examples
-------------

Passing in a list::

    python3 << endpython
    from vim_bridge import bridged

    @bridged
    def GetLongest(list):
        return max(map(lambda s: len(s), list))

    endpython

    echo GetLongest(['one', 'two', 'three', 'four'])
                " returns 5 (because "three" is 5 chars long)

Catching exceptions::

    python3 << endpython
    from vim_bridge import bridged

    @bridged
    def WillCauseException():
        raise Exception("Oops")

    endpython

    " This will throw an error to the user...
    echo WillCauseException()

    " But here's how you can catch that in Vim
    try
        echo WillCauseException()
    catch
        echo "Something went wrong. Aborting."
    finally
        echo "Cleaning up."
    endtry

Using Python stdlib functions to do work that would be more difficult
using pure Vim scripting::

    python3 << endpython
    import os.path
    from vim_bridge import bridged

    @bridged
    def NormalizePath(path):
        return os.path.realpath(path)
    endpython

    echo NormalizePath("/this/../or/./.././that/is/./a/.//very/../obscure/..//././long/./../path/name")
    echo NormalizePath("..")

You can use the bridged function definitions within a Python block
itself, or from inside Vim, it does not matter.  In this example,
NormalizePath is called from both Python and Vim::

    python3 << endpython
    import os.path
    from vim_bridge import bridged

    @bridged
    def NormalizePath(path):
        return os.path.realpath(path)

    @bridged
    def RealPath(path):
        # It does not matter if you call NormalizePath from here...
        return NormalizePath(path)
    endpython

    " ...or from here
    echo NormalizePath("/this/../or/./.././that/is/./a/.//very/../obscure/..//././long/./../path/name")
    echo RealPath("..")

Since vim_bridge 0.4, the function name casing convention is
automatically converted to match Vim's conventions (and *requirement*
even, since function names **must** start with a capital letter).
Besides casing, prefixing the Python function with an underscore will
lead to the function being defined in the Vim context as a
``<SID>``-prefixed function (i.e. a "private" function that cannot be
called from outside the script)::

    python3 << endpython
    import os
    import vim
    from vim_bridge import bridged

    @bridged
    def public():
        return "I am public."

    @bridged
    def _private():
        return "I am private (available in the current script only)."

    @bridged
    def my_name_is_auto_converted():
        return "In Python, I'm called my_name_is_auto_converted, " + \
               "but in Vim, I'm called MyNameIsAutoConverted :)"

    @bridged
    def _long_private_name():
        return "I'm private, and my case is converted automatically."
    endpython

    echo Public()
    echo s:Private()
    echo MyNameIsAutoConverted()
    echo s:LongPrivateName()


Changes
-------

- Original code by Vincent Driessen (@nvie) in 2010. BSD License.
- Updated for Python3 by Walter Doekes (@wdoekes) in 2017.
