results = [[]]*5

def create_multipliers():
    return [lambda x: i * x for i in range(5)]

for i in range(5):
    results[i].append(create_multipliers())

print(results)
