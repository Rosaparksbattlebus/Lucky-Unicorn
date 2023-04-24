"""Component 3 (random token) v3
Format currency
Ensure adds favour of the house - %10 chance of unicorn and %30 chance of each of the rest
"""

import random

STARTING_BALANCE = 100
balance = STARTING_BALANCE
tokens = ["unicorn", "horse", "donkey", "zebra", "horse", "donkey", "zebra", "horse", "donkey", "zebra"]

# testing loop to generate 100 tokens
for item in range(100):
    token = random.choice(tokens)


    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= 0.5

print(f"Starting balance = ${STARTING_BALANCE:.2f}")
print(f"End balance = ${balance:.2f}")



