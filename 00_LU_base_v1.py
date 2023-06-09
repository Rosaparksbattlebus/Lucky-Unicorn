"""LU base component
Components added after they have been created and tested
"""


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


# Main routine go here...
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()

# ask the user how much they want to play with
user_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${user_balance}")
