.. _syntax:

******
Syntax
******

Before we move to the data handling with |NumPy|_ and plotting with |matplotlib|_ we
introduce basic concepts of Python syntax and script execution.

What is a script?
=================

**Python script** (or **script**) is a plain text file with some Python code inside and 
**.py** extension. Python script can be executed from the **terminal** by typing the
command

.. code-block::

  python my-script.py

and pressing "Enter". ``python`` is a command that tells the computer to use Python and
``my-script.py`` is a name of the script that Python should execute.

.. hint::
  Depending on your installation of Python you might need to use ``python3`` instead of
  ``python``.


Python script is executed line-by-line starting from the top.

Different blocks of text in the script are understood in a particular way by Python.
Below we cover blocks that are important for this workshop.

Comments
========

Comments are the sections of the script that are completely ignore during the run-time.

In Python in-line comments are written with ``#`` symbol:

.. code-block:: python

  # This is a comment
  print("Hello world") # This is a comment too (starting from the "#" symbol)

  # This is a comment
  # that is very very long
  # and covers a lot of lines

If the comments are removed from the above code snippet, then it would look like:

.. code-block:: python

  print("Hello world")

.. hint::
  In each line all symbols between the first ``#`` symbol and the end of the line are
  ignored. There are exceptions: If ``#`` symbol is a part of the **string**, then it
  does not indicate a comment:

  .. code-block:: python

    # This is a comment
    a = "# This is a string and not a comment"


Imports
=======

If you are using third-party libraries in your python scripts, then you need to import 
them in the **namespace** of the script:

.. code-block:: python

  # Next line import numpy package 
  import numpy
  # Next line import numpy package and
  # defines a shortcut that can be used in the script
  import numpy as np
  # Import one particular function from numpy library
  from numpy import loadtxt

Import section should be located before the first-time usage of corresponding third-part
package. It is a good practice to locate all your imports at the top of the script.

Code
====

Code itself is a set of commands that will be executed during run-time of your script.
Each line should contain a correct statement.


Numerical data-types
--------------------

.. code-block:: python

  3 # This is an integer
  3.0 # This is a float

Text data-types
---------------

Text data are represented with ``string`` data type and the syntax is the following
(Single `'` and double `"` quotes are equivalent, but can not be mixed)

.. code-block:: python

  # This is a string:
  "Quokka" 
  # This is a string:
  'Quokka'
  # This is a syntax error:
  "Quokka'
  # This is a correct string with the string being Quokka':
  "Quokka'"
  "3.0" # This a string and not a float

Iterables
---------

Iterables are collections of any objects that have a well defined order of elements.

.. code-block:: python

  # This is a list:
  [1, 2, 3, 4] 
  # This is a tuple:
  (1, 2, 3, 4) 
  # This is a dictionary:
  {"Quokka": "Animal", "Orange": "Fruit"}

.. hint::
  List is **mutable** and tuple is immutable data type. Meaning: elements of the list can
  be changed, while elements of the tuple are fixed:

  .. code-block:: python

    # Create a list and tuple and link it with some variables
    list_example = [1, 2, 3]
    tuple_example = (1, 2, 3)
    # Next line is correct and the list will be [10, 2, 3]
    list_example[0] = 10
    # Next line will cause an error
    tuple_example[0] = 10

Variables
---------

Variable is an object that have an **identifier** and linked with some data (of any type).
Variable names are case-sensitive. There is a list of |reserved-keywords|_ that can not
be used as a name for a variable.

.. code-block:: python

  # Variable with a name (identifier) "a" that have an integer value of 5.
  a = 5
  # Variable with the name "colors" that linked to the list of strings
  colors = ["tab:red", "tab:green", "tab:blue"]

Functions
---------

Functions are pre-defined pieces of code, that you can reuse multiple time in the script.
They can be coming from the standard library (as |Python-print|_ function),
from third-party libraries (as |Numpy-loadtxt|_ function of |NumPy|_ package) or defined
by you.

A call of the function consists of writing the **identifier** of a function,
then round parenthesis and putting positional arguments or keyword arguments inside the
parenthesis, separated by comma.

.. code-block:: python

  # Built-in function print() will output its first positional argument 
  # (a string "Hello, I am a Quokka") in the standard output stream (terminal)
  print("Hello, I am a Quokka.")
  # You can pass a keyword argument "end" to the print() function to control the symbols,
  # That will be printed after the first positional argument:
  print("Hello, I am a Quokka", end="\n\n\n")

Functions can return some data, that can be catch in a variable:

.. code-block:: python

  # Returned data is a numpy array (typically of floats),
  # that is read from input text file.
  data = np.loadtxt("filename")


If conditions
-------------

If conditions are used to diverge two possible scenarios of code execution.
The syntax is as follows

.. code-block::

  if <condition1>:
      print("Condition1 is True, so I go to sleep.")
  elif <condition2>:
      print("Condition2 is True, so I go to work")
  else:
      print("Neither of conditions is True, this never happened before...")

Note the indentation level, as it indicates the code block.


For loop
--------

**for** loop is useful for performing repetitive operations. For example if one want to 
compute square roots of a set of numbers:

.. code-block:: python

  # Import square root function from the math module of standard library
  from math import sqrt

  # Create an list of numbers:
  numbers = [1, 3, 5, 2.8, 10]

  # Use index and length of the list as an iterator
  for i in range(len(numbers))
      # Note the indentation level
      print(sqrt(numbers[i]))
  
  # Alternatively one can iterate over the list itself
  for number in numbers:
      print(sqrt(number))








