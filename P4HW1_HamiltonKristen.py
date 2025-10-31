# Kristen Hamilton
# 10/28/2025
# P4HW1
# A brief description of the project

# make the list
Scores = []
User_num = int(input("How many scores do you want to enter: "))
# loop User_num times
for count in range(User_num):
    # ask for a score
    print()
    Score1=int(input(f"Enter score #{count+1}: "))
    # make sure it's >=0
    while Score1 <0 or Score1 > 100:
        print("INVALID score enter!!!!")
        print("Score should be between 0 and 100")
        print("Enter score again: ")
        Score1=int(input(f"Enter score #{count+1}: "))
    # add it to the Scores list
    Scores.append(Score1)



high_score = max(Scores)
low_score = min(Scores)
score_average = sum(Scores)/len (Scores)
print()
print("--------------Results------------------")
print (f'{"Lowest score:":<20}{low_score:.1f}')
print (f'{"Modified list:":<20}{Scores}')
print (f'{"Score average:":<20}{score_average:.1f}')
if score_average >= 90:
    print('Grade: A')
elif score_average > 80:
    print('Grade: B')
elif score_average > 70:
    print('Grade: C')
elif score_average > 60:
    print('Grade: D')
else:
    print('Grade: F')
print("-------------------------------------")