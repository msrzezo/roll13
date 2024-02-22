# checking user enters yes / no (takes in a question)
def yes_no(question):
    def instructions():
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")

    response = input(question).lower()
        #checks user response, question
        # repeats if users don't enter yes / no
    if response == "yes" or response == "y":
            return "yes"
    elif response == "no" or response == "n":
            return "no"
    else:
            print("Please enter yes / no")




# Main Routine
print()
print("🎲🎲 Roll it 13 🎲🎲")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

# checks user enters yes (y) or no (n)
if want_instructions == "yes":
   want_instructions
   print('''
    
**** instructions ****

To begin, decide on a score goal (eg: The first one to get a score of 50 wins).
For each round of the game, you win points by rolling dice.
The winner of the round is the one who gets 13 (or slightly less).
If you win the round, then your score will increase by the number of points that you earned. 
If your first roll of two dice is a double (eg: both dice show a three), 
then your score will be DOUBLE the number of points.
If you lose the round, then you don't get any points.

If you and the computer tie (eg: you both get a score of 11, then you will have 11 points added to your score.

Good Luck!
    
''' )

print("Program Continues")
