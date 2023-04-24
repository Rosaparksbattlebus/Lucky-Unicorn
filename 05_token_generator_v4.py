"""Component 3 (random token) v4
Format currency
Ensure adds favour of the house - %5 chance of unicorn %30 donkey and %65 for horse/zebra
"""

import random

STARTING_BALANCE = 100
balance = STARTING_BALANCE

# Testing loop to generate 100 tokens
for item in range(10):
    percent = random.randint(1, 100)

    # if random number is between 1 and 5, token is unicorn +$4
    if 1 <= percent <= 5:
        token = "unicorn"
        balance += 4
    # if random number is between 6 and 36, token is donkey -$1
    elif 6 <= percent <= 36:
        token = "donkey"
        balance -= 1
    # otherwise the token is a horse or zebra -$0.5
    else:
        # if number is even, token is zebra
        if percent % 2 == 0:
            token = "zebra"
        # otherwise, token is horse
        else:
            token = "horse"
        balance -= 0.5
    print(f"Token: {token}, Balance: {balance:.2f}")

print()
print(f"Starting balance = ${STARTING_BALANCE:.2f}")
print(f"End balance = ${balance:.2f}")
