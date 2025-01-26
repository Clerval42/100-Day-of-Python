import Art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
              }


def calculator():
    """A simple calculator for basic calculations (+, -, *, /)"""
    print(Art.logo)
    isCont = True
    num1 = float(input("What is first number?: "))
    while isCont:
        num2 = float(input("What is second number?: "))
        for x in operations:
            print(x)
        operation_symbol = input("Pick an operation from the line above: ")
        operation_function = operations[operation_symbol]
        answer = operation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        wantCont = input("Do you want to continue with this result? y or n :")
        if wantCont == "y":
            num1 = answer
        if wantCont == "n":
            isCont = False
            calculator()


calculator()
