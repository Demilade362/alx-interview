def minOperations(n):
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