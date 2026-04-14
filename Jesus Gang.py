def calculator():
    print("Simple Python Calculator")
    print("Operations: +  -  *  /")

    while True:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero!")
                continue
        else:
            print("Invalid operator!")
            continue

        print("Result:", result)

        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break


calculator()
