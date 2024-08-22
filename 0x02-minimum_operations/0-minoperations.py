#!/usr/bin/python3
"""Module for task 0
"""


def minOperations(n):
     """Calculates the fewest number of operations needed to result in
     exactly n H characters in the file.

     Args:
         n (int): The number of desired H characters.

     Returns:
         int: The number of minimal operations needed to get n H characters
               or 0 if it is impossible to achieve n.
     """
     if not isinstance(n, int) or n <= 1:
         return 0

     ops_count = 0
     divisor = 2

     while n > 1:
         while n % divisor == 0:
             ops_count += divisor
             n //= divisor
         divisor += 1

     return ops_count

