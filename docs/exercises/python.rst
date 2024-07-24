.. _exercises_python_basics:


Variables
=========

* Create two variables and put some numbers in them.

* Compute the sum of those two numbers, using variables and save it to the third variable.

* Do the same two operation, but use strings instead of numbers (you can concatenate strings with ``+``).

Functions
=========

* Print the results of the previous exercise to the console.

* Use sin and cos functions from ``math`` library (``from math import cos, sin, pi``) to
  compute sin and cos of the numbers from previous exercise.

* Print the results to the console.

Iterables
=========

* Create a list of numbers.

* Use **for** loop to iterate over the list and print the square root of each number.
  (``from math import sqrt``). Use ``len()`` function to compute length of the list.

* Convert the list to the numpy array. Use ``np.sqrt()`` to do the same but without the **for** loop.



.. dropdown:: Answer

  .. code-block:: python

    from math import sin, cos, sqrt
    import numpy as np

    # Exercise 1
    number_1 = 4
    number_2 = 9
    sum_of_numbers = number_1 + number_2

    string_1 = "I am "
    string_2 = "Quokka"
    sum_of_strings = string_1 + string_2

    # Exercise 2
    print(sum_of_numbers)
    print(sum_of_strings)

    square_root = sqrt(number_1)
    print(square_root)

    # Exercise 3 
    numbers = [1, 2, 3, 4, 5]

    # Iterate using an index as an iterator
    for i in range(len(numbers)):
      print(numbers[i])

    # Alternatively you can iterate directly over iterable
    for number in numbers:
      print(number)

    numbers = np.array(numbers)

    square_roots = np.sqrt(numbers)

    print(square_roots)
