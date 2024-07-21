.. _exercises_numpy_basics:

Arithmetic operations
=====================

* Create three arrays of random numbers with the same shape.

* Compute sum, of the first two. Print the result. Save the result to the variable.

* Make sure that the third one does not have zeros.
  Compute the division of the first array by the third one.
  Print the result.

  .. dropdown:: Hint

  Use an addition of the constant to achieve it.

* Use the variables from the second point to save the results to the text file.
  Extra: same the data in scientific notation with 5 meaningful digits.

  .. dropdown:: Hint

    Check the documentation for the |Numpy-savetxt|_

.. dropdown:: Answer

  .. code-block:: python

    import numpy as np

    array_1 = np.random.random((5,3))
    array_2 = np.random.random((5,3))
    array_3 = np.random.random((5,3))

    sum_12 = array_1 + array_2

    print(sum_12)

    array_3 = array_3 + 0.1 - array_3.min()

    print(array_1 / array_3)

    np.savetxt("filename.txt", sum_12)
    np.savetxt("filename-scientific.txt", sum_12, fmt="%.5e %.5e %.5e")

Reading an array
================

* Download :download:`sample array <basics-reading.txt>`.

* What is the shape of an array?

* What is the minimum and maximum value of an array?

* What is the arithmetic mean value of an array?

* Extra: What is the median number of an array?

  .. dropdown:: Hint

    Make an array one dimensional and sort it.

.. dropdown:: Answer

  .. code-block:: python

    import numpy as np

    array = np.loadtxt("basics-reading.txt")

    print(f"Array's shape is {array.shape}")
    print(f"Array's minimum value is {array.min()}")
    print(f"Array's maximum value is {array.max()}")
    print(f"Array's arithmetic mean value is {np.sum(array)/array.size}")

    sorted_array = np.sort(array.flatten())
    if sorted_array.size // 2 == 0:
        median = (sorted_array[sorted_array.size // 2] + sorted_array[sorted_array.size // 2 - 1])/2
    else:
        median = sorted_array[sorted_array.size // 2]

    print(f"Array's median value is {median}")






