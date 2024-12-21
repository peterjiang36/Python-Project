import art


# Helper function to do the calculations
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


# Dictionary that stores the operators and the helper functions
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    """
    Function that does the calculating
    :return: floating number as the calculation result
    """
    print(art.logo)

    first_num = float(input("What's the first number?: "))

    continue_calculate = True

    while continue_calculate:

        for symbol in operations:
            print(symbol)

        operators = input("Pick an operation: ")

        # Exception: in case the user enter invalid operation
        is_operator_in_operations = True
        while is_operator_in_operations:
            if operators not in operations:
                operators = input("Invalid input! Please choose a operation in '+', '-', '*' or '/': ")
            else:
                is_operator_in_operations = False

        second_num = float(input("What's the next number?: "))

        # Exception: in case the user choose divide operation and the denominator is 0
        if operators == "/" and second_num == 0:
            is_zero = True
            while is_zero:
                second_num = float(
                    input("Invalid input! The denominator cannot be 0! Please re-enter a non 0 number: "))
                if second_num != 0:
                    is_zero = False

        result = operations[operators](first_num, second_num)

        print(f"{first_num} {operators} {second_num} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if choice == "y":
            first_num = result
        else:
            continue_calculate = False
            print("\n" * 20)
            calculator()


calculator()