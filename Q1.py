list = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]

def find_odd(list):
    for num in list:
        if list.count(num) % 2 != 0:
            return num
        
# def find_odd(list):
#     result = 0
#     for num in list:
#         result ^= num
#     return result
        
print(find_odd(list))

