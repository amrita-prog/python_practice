# def get_budgets(people):
#     return sum(person['age'] for person in people)

def get_budgets(people):
    total = 0
    for person in people:
        total += person['budget']
    return total

print(get_budgets([
 { "name": "John", "age": 21, "budget": 23000 },
 { "name": "Steve",  "age": 32, "budget": 40000 },
 { "name": "Martin",  "age": 16, "budget": 2700 }
 ]))