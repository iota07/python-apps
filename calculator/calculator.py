from art import logo


def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:
        num2 = float(input("What's the next number?: "))

        for key in operations:
            print(f"Operation: {key}")
        chosen_operation = input("Pick the desired operation: ")

        calculation_function = operations[chosen_operation]
        answer = calculation_function(num1, num2)

        print(f"{num1} {chosen_operation} {num2} = {answer}")

        if (
            input(
                f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
            )
            == "y"
        ):
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
