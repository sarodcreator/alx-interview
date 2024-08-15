#!/usr/bin/python3
"""Module to determine if a list of boxes contain keys to other boxes"""


def canUnlockAll(boxes):
    """Function to determine keys from list of boxes"""
    n = len(boxes)
    confirm = True

    for key in range(1, n - 1):
        visited = False
        
        for box in range(n):
            visited = key in boxes[box] and key != box
            if visited == confirm:
                break
        if visited is False:
            return visited
    return confirm
