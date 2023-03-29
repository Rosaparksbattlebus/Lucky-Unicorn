#Puts the code into a loop to make testing easier and more efficient.


show_instructions = ""
while show_instructions != "x":

    # Ask user if they have played before
    show_instructions = input("Have you played this game before? Enter 'yes' or 'no': ").lower()

    # If yes, print 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        print("Program continues")

    # If no, print 'Display instructions'
    elif show_instructions == "no" or show_instructions == "n":
        print("Display instructions")

    # Else, show error
    else:
        print("Please answer 'Yes' or 'No'")


    print(f"You entered '{show_instructions}'")
