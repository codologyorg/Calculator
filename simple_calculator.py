# User interface

print(" Calculator ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Variables
choice = int(input("Enter the operation you want to perform\n"))
num1 = float(input("Enter in your first number\n"))
num2 = float(input("Enter in your second number\n"))


# If-else Statements

if choice == 1:
    print(num1, "+", num2, "=", (num1+num2))
elif choice == 2:
    print(num1, "-", num2, "=", (num1-num2))
elif choice == 3:
    print(num1, "*", num2, "=", (num1 * num2))
elif choice == 4:
    print(num1, "/", num2, "=", (num1/num2))
else:
    print("You may have entered something wrong, please try again.")
