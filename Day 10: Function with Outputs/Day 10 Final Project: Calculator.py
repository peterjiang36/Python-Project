import art

print(art.logo)

first_num = float(input("What's the first number?: "))

operation = input("+\n-\n*\n/\nPick an operation: ")
# Exception control: in case the user enter invalid operation
if operation != "+" and "-" and "*" and "/":
    operation = input("Invalid input! Please choose a operation in '+, -, * and /: ")

second_num = float(input("What's the next number?: "))

if operation == "+":
    result = first_num + second_num
elif operation == "-":
    result = first_num - second_num
elif operation == "*":
    result = first_num * second_num
elif operation == "/":
    if second_num == 0:
        second_num = float(input("Invalid input! The denominator cannot be 0! Please re-enter a non 0 number: "))
        result = first_num / second_num
    else:
        result = first_num / second_num

print(f"{first_num} {operation} {second_num} = {result}")



# while continue_calcualte:
#     result = None
#     input("Wh")
