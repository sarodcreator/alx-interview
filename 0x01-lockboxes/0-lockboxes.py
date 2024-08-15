def canUnlockAll(boxes):
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
