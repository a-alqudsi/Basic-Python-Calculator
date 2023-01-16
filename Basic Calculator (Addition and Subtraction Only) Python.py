def calculator(x, y, operation):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    else:
        return "Invalid operation"

print("Select operation.")
print("1. Add")
print("2. Subtract")

choice = input("Enter choice (add/subtract): ").lower()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = calculator(num1, num2, choice)

if result == "Invalid operation":
    print(result)
else:
    print("{} {} {} = {}".format(num1, choice, num2, result))
