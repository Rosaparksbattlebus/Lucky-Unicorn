"""Component 3 (random token) v2
Calculate user balance based on random selection of tokens"""

import random

balance = 100

tokens = ["unicorn", "horse", "donkey", "zebra"]

# testing loop to generate 20 tokens
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')

    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= 0.5
    print(f"Token: {token}, Balance: {balance}")


