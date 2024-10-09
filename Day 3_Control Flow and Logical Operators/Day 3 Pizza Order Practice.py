print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extrac cheese? Y or N: ")

bill = 0

# small pizza $15, medium pizza $20, and large pizza $25
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")

if pepperoni == "Y":
    # small size pizza adding pepperoni $2
    if size == "S":
        bill += 2
    # medium and large pizza adding pepperoni $3
    else:
        bill += 3
# all sizes pizza adding extra cheese $1
if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is ${bill}.")