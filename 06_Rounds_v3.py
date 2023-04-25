"""Based on 06_rounds_v2
Converting v2 into a function
"""

import random


# Function to generate random token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    # Testing loop to generate 5 tokens
    while play_again != "x":
        rounds_played += 1  # keep track of rounds
        percent = random.randint(1, 100)  # can only be a donkey

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
        if balance < 1:
            print()
            print("Sorry, you have run out of money")
            play_again = "x"
    return balance

# Main routine


starting_balance = 5
closing_balance = generate_token(starting_balance)
print()
print("Thanks for playing")
print(f"Starting balance = ${starting_balance:.2f}")
print(f"End balance = ${closing_balance:.2f}")
