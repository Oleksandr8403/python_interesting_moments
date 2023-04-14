import random
'''I've always wondered how probability theory works. In the case of a coin toss. But I don't have time to flip a coin 100,000 times.'''


# Define function to simulate coin tosses and calculate frequency of each result
def coin_random_case(amount):
    results = []

    # Simulate coin tosses and store the result
    for i in range(amount):
        case = random.randint(1, 2)
        results.append(case)

    # Calculate the frequency of each result
    events = (results.count(1)*100/amount, results.count(2)*100/amount)
    return events


# Define the list of experiment sizes to test
list_experiments = [10, 50, 100, 200, 300, 500, 1000, 10000, 100000, 1000000]

# Loop through each experiment size and test the function
for i in list_experiments:
    amount_cases = i
    x = coin_random_case(amount_cases)
    print(f'{amount_cases}: 1 - {x[0]}%, 2 - {x[1]}%')
