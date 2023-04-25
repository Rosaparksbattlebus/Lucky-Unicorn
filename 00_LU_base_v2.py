"""LU base component - based on 00_LU_base_v1
Components added after they have been created and tested
"""
import random

# Functions go here...
def yes_no(question_text):
    while True:
        # Ask user if they have played before
        answer = input(question_text).lower()

        # If yes, print 'program continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If no, print 'Display instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Else, show error
        else:
            print("Please answer 'Yes' or 'No'")


def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game will go here")
    print()


# number checker function
def num_check(question, low, high):
    error = "That was not valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    # Keep asking until a valid amount 1-10 is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check for number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


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


# Main routine go here...
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()

# ask the user how much they want to play with
starting_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${starting_balance}")


closing_balance = generate_token(starting_balance)
print()
print("Thanks for playing")
print(f"Starting balance = ${starting_balance:.2f}")
print(f"End balance = ${closing_balance:.2f}")