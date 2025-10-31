#Kristen Hamilton
#P4Lab2
#10/30/2025
# write code that displays information to users using loops

run_again = 'yes'

while run_again !='no':
    user_num = int(input("Enter an integer: "))
    if user_num > 0:
        for item in range(1,12):
            print(f"{ user_num } * {item} = {user_num * item}")
    else:
        print("This program does not handle negative numbers")
    run_again = input("Would you to run the program again? ")
#End of loop
print("program is ending....")
