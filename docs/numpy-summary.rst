.. _numpy-summary:

*****
NumPy
*****

For handling the numerical data de-facto standard for python is a |NumPy|_ library.

For the detailed and thorough introduction to the library we refer you to the
|Numpy-user-guide|_ and |Numpy-basics|_.

Central object for handling in numpy is an **array**. As an example consider 
four numbers: 1,2,3,4, that are arranged in a list:

.. code-block:: python

  # Import of numpy package
  import numpy as np

  list_example = [1, 2, 3, 4]
  # They can be converted to the one-dimensional numpy array:
  array_example = np.array(list_example)
    
Next consider same six numbers arranged in a 3x2 matrix:

.. code-block:: text

  ┌───┬───┐
  │ 1 │ 2 │
  ├───┼───┤
  │ 3 │ 4 │
  ├───┼───┤
  │ 5 │ 6 │
  └───┴───┘

This data structure represents two-dimensional numpy array with the size of first
dimension equal to 3 and second dimension of size 2:

.. code-block::

  import numpy as np

  array_example = np.array([[1, 2], [3, 4], [5, 6]])

  print(array.shape)
  # The output will be (3, 2)


Creation of an array
====================

* An array can be loaded from the text file with |Numpy-loadtxt|_ funtion:

  .. code-block:: python

    import numpy as np

    # Here we load the 2x2 matrix, skipping one row and loading
    # only first, third and fourth column.
    AFM_data = np.loadtxt("experiments/2024/07/23/trial_1.txt", skiprows=1, usecols=(0,2,3))
    # If there is 1000 line in the file, then shape of an array is (1000, 3)
    print(AFM_data.shape)

* An array can be created from a list

  .. code-block:: python

    import numpy as np

    list_example = [1, 2, 3, 4]

    array_from_list = np.array(list_example)

* An array can be initialized by some rule

  .. code-block:: python
    
    import numpy as np

    # Array of 100 random floats between 0 and 1
    random_array = np.random.random(100)
    # Linearly distributed 100 values between -2 and 10
    linear_array = np.linspace(-2, 10, 100)
    # Logarithmically distributed 100 values between -2 and 10
    log_array = np.logspace(-2, 10, 100)
    # two-dimensional array of 100 zeros
    zero_array = np.zeros((20, 5))
    # two-dimensional array of 100 ones
    one_array = np.ones((20, 5))

Properties of an array
======================

.. code-block:: python

  import numpy as np

  random_array = np.random.random((5,3))

  # Shape of an array
  print(random_array.shape)

  # minimum value
  print(random_array.min())

  # maximum value
  print(random_array.max())


Arithmetic operations
=====================

.. code-block:: python

  import numpy as np

  test_array = np.random.random((3,5,1))

  # Array can be multiplied/divided by a number
  print(test_array * 10)
  print(test_array / 10.2)

  # A number can be added/subtracted to the array
  print(test_array + 1)
  print(test_array - 0.5)

  # For the special operations one need to use the corresponding function from numpy library
  # Square root
  print(np.sqrt(test_array))
  # Logarithm
  print(np.log(test_array))
  # sin, note the argument is expected in radians
  print(np.sin(test_array))
  # To pass angles in degrees:
  print(np.sin(test_array / 180 * np.pi))

.. hint::
  See the full list of mathematical functions here: |Numpy-math|_

Matrix operations
=================

* Two arrays of the same shape can be summed, subtracted, multiplied, divided (element-wise):

  .. code-block:: python

    import numpy as np

    test_array_1 = np.random.random((3,5,1))
    test_array_2 = np.random.random((3,5,1))

    print(test_array_1 - test_array_2)
    print(test_array_1 + test_array_2)
    print(test_array_1 / test_array_2)
    print(test_array_1 * test_array_2)


Indexing and slicing
====================

Besides speed of operation, arrays offer an advanced slicing and indexing:

.. code-block:: python
  
  import numpy as np

  test_array = np.random.random((3,4))

  # horizontal slice
  print(test_array[1])
  # Vertical slice
  print(test_array[:,2])
  # Partial horizontal slice
  print(test_array[1, 1:3])



Saving an array
===============

One- or two-dimensional arrays can be save in a txt file with |Numpy-savetxt|_ function:

.. code-block:: python

    import numpy as np

    test_array = np.random.random((3,5,1))

    np.savetxt("filename", test_array)

