#!/usr/bin/python3
"""
Dynamics
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters in the file.
    
    Args:
        n: An integer representing the target number of characters.
        
    Returns:
        The fewest number of operations needed to achieve n H characters. If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    operations = [0] * (n + 1)

    for i in range(2, n + 1):
        operations[i] = i
        for j in range(i - 1, 1, -1):
            if i % j == 0:
                operations[i] = operations[j] + (i // j)
                break

    return operations[n]
