#!/usr/bin/python3
"""
Prime Game
"""


def prime_no(num):
    """
    Returns a list of prime numbers
    """
    primenum = []
    filternum = [True] * (num + 1)

    for prime in range(2, num + 1):
        if filternum[prime]:
            primenum.append(prime)
            for i in range(prime * prime, num + 1, prime):
                filternum[i] = False
    return primenum

def isWinner(x, nums):
    """
    Determines the winner of the game
    """
    if x == 0 or nums == []:
        return None
    Maria = 0
    Ben = 0

    for i in range(min(x, len(nums))):
        checkPrime = prime_no(nums[i])
        if len(checkPrime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    else:
        return None