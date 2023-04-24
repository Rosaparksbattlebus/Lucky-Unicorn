"""Component 4 - game mechanics and looping v1
Based on 05_token_generator_v4 but hard-wired to only allocate donkeys
Gives user feedback about number of rounds and maintains balance.
Test amount set to $5"""
import random

test = 5
balance = test
rounds_played = 0
play_again = ""

# Testing loop to generate 5 tokens
while play_again != "x":
    rounds_played += 1  # keep track of rounds
    percent = random.randint(6, 36)  # can only be a donkey

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
    print(f"Round {rounds_played}. Token: {token}, Balance: ${balance:.2f}")
    question = input("Press 'x' to exit or <enter> to continue: ")
    if question == "x":
        play_again = "x"
    if balance == 0:
        print()
        print("Sorry, you have run out of money")
        play_again = "x"

print()
print("Thanks for playing")
print(f"Starting balance = ${test:.2f}")
print(f"End balance = ${balance:.2f}")
