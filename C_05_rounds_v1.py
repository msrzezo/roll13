import random

print("Press <enter> to begin this round:")


# generates  an integer between 0 and 6
# to simulate a roll of a die
def roll_die():
    roll_result = random.randint(1, 6)
    return roll_result


# rolls two dice  and returns total and whether we
# had a double roll
def two_rolls(who):
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points (so far)
    first_points = roll_1 + roll_2

    # show the user the results
    print(f"{who} : {roll_1} & {roll_2} - Total: {first_points} ")
    return first_points, double_score

    # Main Routine starts here
    print("Press <enter> to begin this round:")


input()

# Get initial dice rolls for user
user_first = two_rolls("User")
user_points = user_first[0]
double_points = user_first[1]

# Tell the user if they are eligible for double points
if double_points == "yes":
    print("If you win this round, you gain double points!")

# Get initial dice rolls for computer
computer_first = two_rolls("Computer")
computer_points = computer_first[0]

print(f"The computer rolled a total of  {computer_points}.")

# Loop (while both user/computer have <= 13 points)
while computer_points < 13 and user_points < 13:

    # ask user if they want to roll again, update
    # points/status
    print()
    roll_again = input("Do you want to roll the dice (type 'no' to pass:")
    if roll_again == "yes":
        user_move = roll_die()
        user_points += user_move

        if user_points > 13:
            print(f"💥💥💥Oops! You rolled a {user_move} so your total is {user_points}."
                  f"Which is over 13 points. 💥💥💥")

            # reset user points to zero so that when we update their
            # score at the end of the round it is correct

            user_points = 0

            break

        else:
            print(f"You rolled a {user_move} and have a total score of {user_points}  ")

    # Roll die for computer and update computer points
    computer_move = roll_die()
    computer_points += computer_move


    if computer_points > 13:
        print(f"💥💥💥The computer rolled a {computer_move},taking their points"
              f" to {computer_points}. This is over 13 points so the computer loses! 💥💥💥")
        computer_points = 0
        break
    else:
        print(f"The computer rolled a {computer_move}. The computer"
          f" now has {computer_points} points.")

    print()
    if user_points > computer_points:
        result = "🙂🙂🙂You are ahead!🙂🙂🙂"
    elif user_points < computer_points:
        result = "😳😳😳The computer is ahead!😳😳😳"


    print(f"***Round Update****: {result} ")
    print(f"User Score: {user_points} \t | \t Computer Score: {computer_points}")
 
# Outside loop - double user points if they won and are eligible

# Show rounds results
if user_points < computer_points:
    print(f"😢😢😢 Sorry, you lost this round and no points "
          f"have been added to your total score. The computer's score has "
          f"increased by {computer_points} points 😢😢😢 ")
else:
    # Double user points if they are eligible
    if double_points == "yes":
        user_points *= 2
    print(f" 😊😊😊 Yay! You won this round and {user_points} have "
          f"been added to your score 😊😊😊")
