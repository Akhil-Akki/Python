# Question 1 - Name, Age and City

print("\n--- Question 1 ---")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("\nYour Information")
print("Name:", name)
print("Age:", age)
print("City:", city)


# Question 2 - Sum of Two Numbers

print("\n--- Question 2 ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2

print("Sum:", sum_result)


# Question 3 - Arithmetic Operations

print("\n--- Question 3 ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)

if num2 != 0:
    division = num1 / num2
    print("Division:", division)
else:
    print("Division: Cannot divide by zero")


# Question 4 - Area of Rectangle

print("\n--- Question 4 ---")

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print("Area of the rectangle:", area)


# Question 5 - Simple Interest

print("\n--- Question 5 ---")

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)


# Question 6 - Age Next Year

print("\n--- Question 6 ---")

age = int(input("Enter your current age: "))

next_year_age = age + 1

print("Your age next year will be:", next_year_age)


# Question 7 - Celsius to Fahrenheit

print("\n--- Question 7 ---")

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)


# Question 8 - Total Bill

print("\n--- Question 8 ---")

price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total_bill = price * quantity

print("Total Bill:", total_bill)


# Question 9 - Average of Three Numbers

print("\n--- Question 9 ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average:", average)


# Question 10 - Total and Average Marks

print("\n--- Question 10 ---")

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("Total Marks:", total)
print("Average Marks:", average)