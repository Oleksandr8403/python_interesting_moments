import random
'''I've always wondered how probability theory works. In the case of a coin toss. But I don't have time to flip a coin 100,000 times.'''


def coin_random_case(amount):
    results = []

    for i in range(amount):
        case = random.randint(1, 2)
        results.append(case)

    events = (results.count(1)*100/amount, results.count(2)*100/amount)
    return events


list_experiments = [10, 50, 100, 200, 300, 500, 1000, 10000, 100000, 1000000]

for i in list_experiments:
    amount_cases = i
    x = coin_random_case(amount_cases)
    print(f'{amount_cases}: 1 - {x[0]}%, 2 - {x[1]}%')
