import calc_art
print(calc_art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculation_operators = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
def calculator():
    n1 = float(input("what's the first number?:\n"))
    calculation = True
    while calculation:
        for symbol in calculation_operators:
            print(symbol)
        operator = input("pick an operation\n")
        n2 = float(input("what's the other number?:\n"))
        result = calculation_operators[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {result}")
        should_continue = input(f"Type 'y' to continue calculation with {result} and 'n' to start new calculation\n").lower()
        if should_continue == "y":
            n1 = result
        elif should_continue == "n":
            calculation = False
            print("\n"*20)
            calculator()
calculator()




