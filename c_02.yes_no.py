# checking user enters yes / no (takes in a question)
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("You did not choose a valid response")


# Main Routine
print("🎲🎲 Roll it 13 🎲🎲")
while True:
    want_instructions = yes_no("Do you want to read the instructions? ")
    print(f"You chose {want_instructions}")


