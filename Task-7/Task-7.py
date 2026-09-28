# 1. Basic Function

print("\n--- Question 1 ---")


def greet():
    print("Welcome to Python!")

greet()
greet()
greet()


# 2. Function with Parameter

print("\n--- Question 2 ---")

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Akhil")


# 3. Addition Function

print("\n--- Question 3 ---")

def add(a, b):
    return a + b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = add(num1, num2)
print("Sum:", result)


# 4. Square Function

print("\n--- Question 4 ---")

def square(number):
    return number * number

number = float(input("Enter a number: "))
print("Square:", square(number))


# 5. Multiple Parameters

print("\n--- Question 5 ---")

def student_info(name, age, course):
    print("Student Name:", name)
    print("Age:", age)
    print("Course:", course)

student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_course = input("Enter course: ")

student_info(student_name, student_age, student_course)


# 6. Default Argument

print("\n--- Question 6 ---")

def greet(name="User"):
    print(f"Hello, {name}!")

name = input("Enter your name (press Enter for default): ")

if name.strip() == "":
    greet()
else:
    greet(name)


# 7. Keyword Arguments

print("\n--- Question 7 ---")

def employee(name, age, salary):
    print("Employee Name:", name)
    print("Age:", age)
    print("Salary:", salary)

employee(salary=100000, name="Akhil", age=25)


# 8. Return Multiple Values

print("\n--- Question 8 ---")

def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    if b != 0:
        division = a / b
    else:
        division = "Cannot divide by zero"

    return addition, subtraction, multiplication, division


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

addition, subtraction, multiplication, division = calculate(a, b)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)


# 9. Local vs Global Scope

print("\n--- Question 9 ---")

x = 100

def scope_example():
    x = 50
    print("Inside function:", x)

scope_example()

print("Outside function:", x)


# 10. Calculator Using Functions

print("\n--- Question 10 ---")

def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("Result:", add_numbers(num1, num2))

elif choice == "2":
    print("Result:", subtract_numbers(num1, num2))

elif choice == "3":
    print("Result:", multiply_numbers(num1, num2))

elif choice == "4":
    print("Result:", divide_numbers(num1, num2))

else:
    print("Invalid choice.")


# 11. Factorial Function

print("\n--- Question 11 ---")

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


number = int(input("Enter a number: "))
print("Factorial:", factorial(number))


# 12. Prime Function

print("\n--- Question 12 ---")

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")


# 13. Maximum of Three

print("\n--- Question 13 ---")

def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

print("Largest number:", maximum(a, b, c))


# 14. Student Grade Function

print("\n--- Question 14 ---")

def calculate_grade(marks):
    if marks >= 90 and marks <= 100:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    elif marks >= 0:
        return "F"
    else:
        return "Invalid marks"


marks = float(input("Enter student marks: "))

print("Grade:", calculate_grade(marks))


# 15. Mini Banking System

print("\n--- Question 15 ---")

balance = 100000


def check_balance():
    return balance


def deposit(amount):
    global balance

    if amount <= 0:
        return False

    balance += amount
    return True


def withdraw(amount):
    global balance

    if amount <= 0:
        return False

    if amount > balance:
        return False

    balance -= amount
    return True


while True:
    print("\n---- BANKING MENU ----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Current Balance: ₹", check_balance())

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))

        if deposit(amount):
            print("Deposit successful.")
            print("Current Balance: ₹", check_balance())
        else:
            print("Invalid deposit amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))

        if withdraw(amount):
            print("Withdrawal successful.")
            print("Current Balance: ₹", check_balance())
        else:
            print("Invalid amount or insufficient balance.")

    elif choice == "4":
        print("Thank you for using the banking system.")
        break

    else:
        print("Invalid choice. Please select 1-4.")