def unique_num(numbers):
    unique = []
    for i in numbers:
        if numbers.count(i) == 1:
            unique.append(i)
    return unique

print(unique_num([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))