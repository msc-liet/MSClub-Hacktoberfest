def main():
    while True:
        operation = input("Choose operation (add, subtract, multiply, divide, exponentiate, modulus, sqrt, quit): ")
        if operation == "quit":
            break
        if operation in ["add", "subtract", "multiply", "divide", "exponentiate", "modulus"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if operation == "add":
                print(f"Result: {add(a, b)}")
            elif operation == "subtract":
                print(f"Result: {subtract(a, b)}")
            elif operation == "multiply":
                print(f"Result: {multiply(a, b)}")
            elif operation == "divide":
                print(f"Result: {divide(a, b)}")
            elif operation == "exponentiate":
                print(f"Result: {exponentiate(a, b)}")
            elif operation == "modulus":
                print(f"Result: {modulus(a, b)}")
        elif operation == "sqrt":
            a = float(input("Enter number: "))
            print(f"Result: {square_root(a)}")
        else:
            print("Invalid operation. Please try again.")
