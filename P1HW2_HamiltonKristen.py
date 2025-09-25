#Kristen Hamilton
#9/23/2025
#Input and Output
'''
Pseudocode:
Get budget (int)
Get destination (str)
Get gas (int)
Get hotel (int)
Get food (int)
Add expenses
budget - expenses
Display results - use example
'''
print("This program caluclates and displays travel expeneses")
# Get budget from user
budget = int(input("Enter budget: "))
dest = input("Enter your destination: ")
gas = int(input("How much do you think you will spend on gas:"))
hotel = int(input("Approximately, how much will you need for accomodation/hotel:"))
food = int(input("Last, how much do you need for food:"))
expenses = gas + food + hotel
balance = budget- expenses
print()
print()
print("------------Travel Expenses------------")
print("Location: ",dest) 
print("initial budge:",budget)

print("Fuel:",gas)
print("Accomodation:",hotel)
print("Food:",food)
print("Ramaining balance:",balance)
print()
#Changes
