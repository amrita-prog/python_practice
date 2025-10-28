def electricity_bill(units):
    amount = 0
    if(units <= 100):
        amount = units * 1
    elif(units <= 200):
        amount = (100 * 1) + (units - 100) * 2
    elif(units <= 300):
        amount = (100 * 1) + (100 * 2) + (units - 200) * 3
    elif(units <= 500):
        amount = (100 * 1) + (100 * 2) + (100 * 3) + (units - 300) * 4
    else:
        amount = (100 * 1) + (100 * 2) + (100 * 3) + (200 * 4) + (units - 500) * 5

    tax = amount * 0.10
    total = amount + tax + 15

    return total

print(electricity_bill(225))
    