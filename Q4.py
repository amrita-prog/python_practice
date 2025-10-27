def sum_even_odd(list):
    even = 0
    odd = 0
    for num in list:
        if num % 2 == 0:
            even += num
        else:
            odd += num
    return [even, odd]

print(sum_even_odd([1,2,3,4,5,6]))