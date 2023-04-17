def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():


    num1 = float(input("whats the first number"))


    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:

        operetaion_symbol = input("pick operation")
        num2 = float(input("whats the second number"))
        calculation_function = operations[operetaion_symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operetaion_symbol} {num2} = {answer}")
        if input(f"type y to continue calculating with {answer}, type n to start a new calculation") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()