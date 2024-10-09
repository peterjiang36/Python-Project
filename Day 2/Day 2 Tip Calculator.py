"""
Tip calculator with the results round to decimal
"""

print("Welcome to the tip calculator!")

# bill might be floating point number
bill = float(input("What was the total bill? $"))

# tip percentage is usually integer number
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# number of people is always integer
numberOfPeople = int(input("How many people to split the bill? "))

# round to two decimal
payment = round((bill * (1 + tip / 100)) / numberOfPeople, 2)
print(f"Each person should pay: ${payment}")
