# find the lowest, highest, and average score
def get_stats (stats_list):

    # sort the lists.
    stats_list.sort()


# find lowest, highest and average scores
    lowest_score = stats_list[0]
    highest_score = stats_list[-1]
    average_score = sum(stats_list) / len(stats_list)

    return [lowest_score, highest_score, average_score]

# create lists to hold user and computer score
user_scores = [10, 0, 13, 7, 10, 11]
comp_scores = [10, 11, 0, 0, 10, 11]

# loop six times - for testing purposes, ask the user to enter the
# score for the user and the computer for each round
# for item in range (0, 6):
#     user_points = int(input("Enter the user score: "))
#     comp_points = int(input("Enter the computer score: "))
#
#     # add user score to list of user scores!
#     user_scores.append(user_points)
#     comp_scores.append(comp_points)


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
