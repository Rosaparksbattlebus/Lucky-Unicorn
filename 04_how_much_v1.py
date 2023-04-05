"""Component 2 (How much) v1
Ask user how much they want to play for and check that the input is a valid
integer from 1 to 10. If it is, this amount becomes the balance in their
account"""


user_balance = int(input("How much do you want to play with? (must be an integer 1-10) $"))


#Keep asking until a valid amount is entered
while not 1 <= user_balance <= 10:
    print("Try again. Please enter a whole number from 1 to 10")
    user_balance = int(input("How much do you want to play with? $"))


print(f"You are playing with ${user_balance}")
