#!/usr/bin/python3
"""A function to determine the fewest number of coins needed
   to meet a given amount total"""

def makeChange(coins, total):
    """sort the coins to descending order (greedy) """
    coins.sort(reverse=False)

    """storing the coins used """
    change = []
    """ getting the numberof items in the list """
    n = len(coins)

    """ check if total less than 0 """
    if (total <= 0):
        return 0

    i = n - 1
    while i >= 0:
        while (total >= coins[i]):
            total -= coins[i]
            """ append the coin used to the change list """
            change.append(coins[i])
        i -= 1

    """ check total cannot be met by any number of coins you have
        If after using the coins, total is not 0, return -1
    """
    if total != 0:
        return (-1)

    return (len(change))
