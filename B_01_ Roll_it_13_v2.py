import random


# checking user enters yes / no (takes in a question)
def yes_no(question):
    response = input(question).lower()
    if response == "yes" or response == "y":
        return "yes"
    elif response == "no" or response == "n":
        return "no"
    else:
        print("Please enter yes / no")

    response = input(question).lower()
    # checks user response, question
    # repeats if users don't enter yes / no
    if response == "yes" or response == "y":
        return "yes"
    elif response == "no" or response == "n":
        return "no"
    else:
        print("Please enter yes / no")


def instructions():
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
    
''')


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


# checks that users enters an integer
# that is more than 13
def int_check(question):
    while True:

        error = "Please enter a integer that is 13 or more."

        try:
            response = int(input(question))

            # checks that the number is more than / equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# find the lowest, highest, and average score
def get_stats(stats_list):
    # sort the lists.
    stats_list.sort()

    # find lowest, highest and average scores
    lowest_score = stats_list[0]
    highest_score = stats_list[-1]
    average_score = sum(stats_list) / len(stats_list)

    return [lowest_score, highest_score, average_score]


# Main Routine goes here

# initialise user score and computer score
user_score = 0
comp_score = 0

num_rounds = 0

# create lists to hold user, computer score and round history
user_scores = []
comp_scores = []
game_history = []

# Program starts here (with a heading)
print()
print("🎲🎲 Roll it 13 🎲🎲")
print()

# Display instructions if user wants to see them.
want_instructions = yes_no("Do you want to read the instructions? ")


if want_instructions == "yes":
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
    
''')

# Get target score (must be an integer more than 13)
target_score = int_check("Enter a target score: ")
print(target_score)

# Loop game until we have a winner
while user_score < target_score and comp_score < target_score:

    # Add one to the number of rounds (for out heading)
    num_rounds += 1
    print(f"💿💿💿 Round {num_rounds} 💿💿💿")

    # Start of a single round

    # initialise 'pass' variables
    user_pass = "no"
    computer_pass = "no"
    user_move = ""
    computer_move = ""

    # start round...
    print("Press <enter> to begin this round:")
    input()

    # Get initial dice rolls for user
    user_first = two_rolls("User")
    user_points: int = user_first[0]
    double_points = user_first[1]

    if double_points == "yes":
        print("😁👍if you win this round you get double points!😁👍")

    else:
        print("no double points")

    # Tell the user if they are eligible for double points
    if double_points == "yes":
        print("If you win this round, you gain double points!")

    # Get initial dice rolls for computer
    computer_first = two_rolls("Computer")
    computer_points = computer_first[0]

    print(f"The computer rolled a total of  {computer_points}.")

    # Loop (while both user/computer have <= 13 points)
    while computer_points <= 13 and user_points <= 13:

        # ask user if they want to roll again, update
        # points/status
        print()

        # if user has 13 points, we can assume they don't want to roll again
        if user_points == 13:
            user_pass = "yes"

        if user_pass == "no":
            roll_again = yes_no("Do you want to roll the dice (type 'no' to pass:")
        else:
            roll_again = "no"

        if roll_again == "yes":
            user_move = roll_die()
            user_points += user_move

            if user_points > 13:
                print(f"💥💥💥Oops! You rolled a {user_move} so your total is {user_points}."
                      f"Which is over 13 points. 💥💥💥")

                # reset user points to zero so that when we update their
                # score at the end of the round it is correct.
                user_points = 0
                break


            else:
                print(f"You rolled a {user_move} and have a total score of {user_points}.")

        else:
            user_pass = "yes"

        if computer_points >= 10 and computer_points >= user_points:
            computer_pass = "yes"

        elif computer_pass == "yes":
            pass

        else:

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
        else:
            result = "it's currently a tie. "

        print(f"***Round Update****: {result} ")
        print(f"{result} \t User: {user_points} \t | \t Computer : {computer_points}")

        if computer_pass == "yes" and user_pass == "yes":
            break
        # Outside loop - double user points if they won and are eligible

        # Show rounds results
        # user loses (too few points)
    if user_points < computer_points:
        print(f"😢😢😢 Sorry, you lost this round and no points "
              f"have been added to your total score. The computer's score has "
              f"increased by {computer_points} points 😢😢😢 ")

        add_points = computer_points


    # user wins (more than the computer, less than / equal to 13)

    elif user_points > computer_points:
        # Double user points if they are eligible
        if double_points == "yes":
            user_points *= 2

        print(f" 😊😊😊 Yay! You won this round and {user_points} have "
              f"been added to your score 😊😊😊")

        add_points = user_points
    # it's a tie
    else:
        print(f"👔👔👔The result for this round is a tie. You and the computer "
              f"both have {user_points}👔👔👔")

        add_points = user_points

    # Record round result and add it to the game history
    round_result = f"Round {num_rounds} - User: {user_points} \t Computer: {computer_points}"
    game_history.append(round_result)
    # end of a single round

    # If the computer wins, and its points to its score
    if user_points < computer_points:
        comp_score += add_points

    elif user_points > computer_points:
        user_score += add_points
    else:
        comp_score += add_points
        user_score += add_points

    user_scores.append(user_points)
    comp_scores.append(computer_points)

    print()
    print(f"🎲🎲🎲 User: {user_score} points | Computer: {comp_score} points 🎲🎲🎲")
    print()

print(f"Final Scores: User ({user_score}) vs Computer ({comp_score})")
print()

# Display game history if user wants to see it
show_history = yes_no("Do you want to see the game history?")
if show_history == "yes":
    print("\n ⌛⌛⌛ Game History⌛⌛⌛")

    for item in game_history:
        print(item)

    print()

# calculate the lowest, highest and average
# score and display them.

user_stats = get_stats(user_scores)
comp_stats = get_stats(comp_scores)

user_stats = get_stats(user_scores)

print("📊📊📊 Game Statistics 📊📊📊")
print(f"User    - Lowest Score: {user_stats[0]}\t"
      f"Highest Score: {user_stats[1]}\t"
      f"Average Score: {user_stats[2]}\t")

print(f"Computer - Lowest Score: {comp_stats[0]}\t"
      f"Highest Score: {comp_stats[1]}\t"
      f"Average Score: {comp_stats[2]}\t")
