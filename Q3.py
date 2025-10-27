def list_operation(x, y, n):
    result = []
    for i in range(x, y+1):
        if i % n == 0:
            result.append(i)
    return result
    
print(list_operation(1,10,3))