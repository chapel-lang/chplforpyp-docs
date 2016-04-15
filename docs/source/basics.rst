Getting Started
===============

As a Python user, you are accustomed to running and having Python readily available on almost every machine you use. Chapel is equivalently portable (and more so). However, since Chapel is an emerging technology, it is not quite part of the standard software stack that comes bundled with your operating system. You therefore need to go ahead and download and install Chapel on your system.

If you are using a popular Linux-based operating system you will most likely be successful by running these commands:

.. code-block:: bash

    # Download and unpack
    cd /tmp
    curl -L -O http://sourceforge.net/projects/chapel/files/chapel/1.9.0/chapel-1.9.0.tar.gz
    tar xzf chapel-1.9.0.tar.gz
    mv /tmp/chapel-1.9.0 ~/chapel

    # Build Chapel
    cd ~/chapel
    make

    # Setup your environment, add this command to ~/.bashrc for permanent installation.
    source ~/chapel/util/setchplenv.bash

After doing the above you should be able to:

.. code-block:: bash

    # Compile an example program
    chpl -o hello ~/examples/hello.chpl
    # Run it
    ./hello

Running "./hello" should output::

    Hello, world!

If you are running MacOSX, Windows, or for some other the reason the above commands does not work for you then consult the official `quick start instructions`_.

.. _quick start instructions: http://chapel.cray.com/docs/master/usingchapel/QUICKSTART.html

Compiling
---------

What is that!? A binary! Ohh my...

Chapel is currently a compiled language. However, it lets you write and compile very simple programs. There is no annoying boiler-plate needed to get going.

+-----------------------------------------------+-+-------------------------------------------------+
| Python                                        | | Chapel                                          |
+===============================================+=+=================================================+
| .. literalinclude:: /examples/hw.py           | | .. literalinclude:: /examples/hw.chpl           |
|    :language: python                          | |    :language: chapel                            |
+-----------------------------------------------+-+-------------------------------------------------+

And if you like to structure your code, Chapel has neat means for doing so.

+-----------------------------------------------+-+-------------------------------------------------+
| Python                                        | | Chapel                                          |
+===============================================+=+=================================================+
| .. literalinclude:: /examples/hw.main.py      | | .. literalinclude:: /examples/hw.main.chpl      |
|    :language: python                          | |    :language: chapel                            |
+-----------------------------------------------+-+-------------------------------------------------+

All examples in this tutorial / reference guide are compilable. Which means that you can take any snippet and put it into a file like `exploring.chpl` and compile it::

    chpl -o exploring exploring.chpl

Which will create a binary named `exploring` to execute whatever you have written in exploring.chpl.


Language Basics
===============

This section provides an informal language reference. It takes you through the base language features of Python and provides an example of how an equivalent program would be expressed in Chapel.

Variables and Types
-------------------

In Python, variables are *implicitly* declared and their type determined when they are assigned to. In Chapel, variable declaration is *explicit*, but the type of the variable can be inferred from its use in a manner equivalent to that of Python.

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/vars_decl.py       | | .. literalinclude:: /examples/vars.decl.chpl       |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

Types in Python are dynamic, meaning that a variable can change type during its lifetime. The type of a variable in Chapel is static and inferred at compile-time, which means that a type is assigned and cannot be changed at runtime.

Comments
--------

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/comments.py        | | .. literalinclude:: /examples/comments.chpl        |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+


Literals
~~~~~~~~

These work in much the same way that you are used to. A brief overview is provided below.

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/literals.py        | | .. literalinclude:: /examples/literals.chpl        |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

Console input / output
----------------------

You can write to the console (standard output) using ``write`` and ``writeln``:

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/console.py         | | .. literalinclude:: /examples/console.chpl         |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

You can read input from the console (standard input) using ``read`` and ``readln``:

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/console.read.py    | | .. literalinclude:: /examples/console.read.chpl    |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

.. note::
    Notice that the interface for reading input is quite different, though equally simple. In Python you need to explicitly cast the input, whereas in Chapel the type of the input is provided to the ``read/readln`` functions directly.


Conditionals and Blocks
-----------------------

Python is famous for using an indentation guided block-structure, thereby arguably improving readability and increasing consistency of code-style. Chapel uses curly-brackets to denote the start and end of a block.

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/cond.if.py         | | .. literalinclude:: /examples/cond.if.chpl         |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

Switch / Case
~~~~~~~~~~~~~

Python does not support ``switch-statements`` and instead relies on chaining ``if-elif-else`` statements.

Chapel, on the other hand, does have ``switch-statements``, specifically ``select-when-otherwise`` statements:

+-----------------------------------------------+-+-------------------------------------------------+
| Python                                        | | Chapel                                          |
+===============================================+=+=================================================+
| .. literalinclude:: /examples/cond.switch.py  | | .. literalinclude:: /examples/cond.switch.chpl  |
|    :language: python                          | |    :language: chapel                            |
+-----------------------------------------------+-+-------------------------------------------------+

.. note::
    Notice that in both Python and Chapel these forms of ``switch-statements`` do not **fall through**, meaning that one and only one case will be executed. Coming from Python, this might not surpise you; however, if you have ever written a ``switch-statement`` in other languages then this may be slightly surprising.

Ranges
------

In Python ``range`` is a list-constructor often used for driving for-loops or list comprehensions. For lowered memory consumption, Python provides the generator equivalent of ``range`` namely ``xrange``.

In Chapel a **range** is a language construct which behaves and is used in much the same way as lists are used in Python. Where you would think about lists and slicing operations in Python, think of ranges in Chapel.

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/ranges.py          | | .. literalinclude:: /examples/ranges.chpl          |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

.. note:: Difference in bounds!

   - In Python, ``range`` return values in the interval ``[start, stop[``.
   - In Chapel a range-expression yields values the interval ``[start, stop]``.

For both languages the above is a shorthand of the wider form: ``start, stop, step``.

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/ranges_skip.py     | | .. literalinclude:: /examples/ranges.skip.chpl     |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

...

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/ranges_inf.py      | | .. literalinclude:: /examples/ranges.inf.chpl      |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

...

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/ranges_short.py    | | .. literalinclude:: /examples/ranges.short.chpl    |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+



Loops
-----

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/loops.for.py       | | .. literalinclude:: /examples/loops.for.chpl       |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/loops.enumerate.py | | .. literalinclude:: /examples/loops.enumerate.chpl |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/loops.while.py     | | .. literalinclude:: /examples/loops.while.chpl     |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

Functions and Types
-------------------

+-----------------------------------------------+-+----------------------------------------------+
| Python                                        | | Chapel                                       |
+===============================================+=+==============================================+
| .. literalinclude:: /examples/func_decl.py    | | .. literalinclude:: /examples/func.decl.chpl |
|    :language: python                          | |    :language: chapel                         |
+-----------------------------------------------+-+----------------------------------------------+

Variable arguments?
Argument unpacking?
Return values?
Return type declaration?

Lists, Arrays, Tuples, and Dicts
--------------------------------

In Python, lists are an essential built-in datastructure. You might be frightened to learn that lists are not particularly useful in Chapel. However, fear not. Many of the uses of lists in Python are handled by ranges, such as driving loops. So if that is your primary concern, then take another look at the description of ranges above.

If you need the ability to have elements of different types in a container such as::

    stuff = ['a string', 42, ['another', 'list', 'with', 'strings']]

Then take a look at tuples in the following section.

If you use lists for processing various forms of data of the same type, then what you need are Chapel arrays. Yes, that is correct, Chapel actually has arrays as first-class citizens in the language. Chapel is, to a great extent, all about arrays.

Tuples
~~~~~~

Tuples work in ways quite familiar to a Python programmer. Tuples are among other things useful for packing and unpacking return-values from functions and having sequences of varying types.

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/tuples.py          | | .. literalinclude:: /examples/tuples.chpl          |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

.. note:: Indexing scheme of tuples.

   - In Python, tuple-indexing is 0-based.
   - In Chapel, tuple-indexing is 1-based.

.. note:: Mutability of tuples.
  
   - In Python, tuples are immutable.
   - In Chapel, tuples are mutable.

Arrays
~~~~~~

This section only scratches the surface of Arrays in Chapel. The use of arrays and concepts related to them are described in greater detail in the section on data parallelism.

Since Python does not support arrays within the language, a comparison to the widespread and popular array-library NumPy is used as a reference instead. The first example below illustrates the creation and iteration over a ``10x10`` array containing 64-bit floating point numbers.

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/arrays.py          | | .. literalinclude:: /examples/arrays.chpl          |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

.. note:: ``Domains`` an unfamiliar concept!

    The array syntax and semantics should be easy to follow. The interesting thing to notice is the use of ``.domain`` when doing indexed iteration. A ``domain`` is a powerful concept and you will be very pleased with it once you get to know it. However, it does require an introduction.

    A ``domain`` defines a set of indexes. When iterating over the domain associated with an array, as in the example above, you effectively iterate over all the indexes of all elements in the array. You might be accustomed to ``0-based`` indexing from Python when using lists and tuples. With Chapel you can define whether you want your arrays to be ``0-based`` or ``1-based``.
    In the example above, the array is ``0-based`` since the indexes are defined by the range ``0..9``. If you would prefer ``1-based`` arrays you would define it using the range ``1..10`` instead.

    This is quite a powerful feature. When using arrays as abstractions for matrices, you might find it useful to use ``1-based`` indexing and in other situations a different indexing scheme. With Chapel you can define the index-set and scheme that is most convenient for the domain you are working within.

Initialization

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/arrays.init.py     | | .. literalinclude:: /examples/arrays.init.chpl     |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

Whole-array operations.

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/arrays_whole.py    | | .. literalinclude:: /examples/arrays.whole.chpl    |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

Reductions and scans

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/arrays.reduc.py    | | .. literalinclude:: /examples/arrays.reduc.chpl    |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

Function promotion

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/arrays.promo.py    | | .. literalinclude:: /examples/arrays.promo.chpl    |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+


Dictionaries (Associative Arrays)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dict-comprehension?

Classes and Objects
-------------------

In Python, everything is an object and all objects have a textual representation defined by the object.str(), etc. is there equivalent functionality in Chapel?

+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/classes.py         | | .. literalinclude:: /examples/classes.chpl         |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+


Organizing Code
---------------

Python names modules implicitly via the filename convention. Chapel allows you to use the filename, but also allows you to define it explicitly through the "module" directive.  You can also define and use submodules, or modules defined within the scope of another module.

+-----------------------------------------------+-+-------------------------------------------------+
| Python                                        | | Chapel                                          |
+===============================================+=+=================================================+
| .. literalinclude:: /examples/modules_main.py | | .. literalinclude:: /examples/modules.main.chpl |
|    :language: python                          | |    :language: chapel                            |
+-----------------------------------------------+-+-------------------------------------------------+


+--------------------------------------------------+-+----------------------------------------------------+
| Python                                           | | Chapel                                             |
+==================================================+=+====================================================+
| .. literalinclude:: /examples/modules_import.py  | | .. literalinclude:: /examples/modules.import.chpl  |
|    :language: python                             | |    :language: chapel                               |
+--------------------------------------------------+-+----------------------------------------------------+

