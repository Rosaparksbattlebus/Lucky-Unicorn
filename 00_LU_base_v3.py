"""LU base component - based on 00_LU_base_v2
Adding instructions to instructions function and further text decoration
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
    print()
    print(formatter("*", "How to play"))
    print()
    print("Choose a starting amount to play with - must be between $1 and $10")
    print()
    print("Then press <enter> to play. You will get a random token which might"
          "be a horse, zebra, donkey, or unicorn.")
    print()
    print("It costs $1 to play each round but, depending on your prize, you "
          "could win some of your money back. These are the payout amounts:\n"
          "\tUnicorn: $5 (Balance increases by $4\n"
          "\tHorse: $0.50 (Balance decreases by $0.50\n"
          "\tZebra: $0.50 (Balance decreases by $0.50\n"
          "\tDonkey: $0 (Balance decreases by $1")
    print("\nSee if you can avoid donkeys, get the unicorns, and finish with" 
          "more money than you started with")

    print("*" * 50)
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
        print()
        print(f"...     Round {rounds_played}...\n")
        percent = random.randint(1, 100)  # can only be a donkey

        # if random number is between 1 and 5, token is unicorn +$4
        if 1 <= percent <= 5:
            balance += 4
            print()
            print(formatter("!", "Congratulations, you got a Unicorn"))
            print()
        # if random number is between 6 and 36, token is donkey -$1
        elif 6 <= percent <= 36:
            balance -= 1
            print()
            print(formatter("D", "Bad luck, you got a Donkey"))
            print()
        # otherwise the token is a horse or zebra -$0.5
        else:
            # if number is even, token is zebra
            if percent % 2 == 0:
                print()
                print(formatter("Z", "You got a Zebra"))
                print()
            # otherwise, token is horse
            else:
                print()
                print(formatter("H", "You got a Horse"))
                print()
            balance -= 0.5
        print()
        # output
        print(f"Your Balance is now ${balance:.2f}")
        question = input("Press 'x' to exit or <enter> to continue: ")
        if question == "x":
            play_again = "x"
        if balance < 1:
            print()
            print("Sorry, you have run out of money")
            play_again = "x"
    return balance


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine go here...
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()

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
print()
print(formatter("*", "Goodbye"))