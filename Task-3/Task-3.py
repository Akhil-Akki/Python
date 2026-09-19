# Question 1: Arithmetic Operations

print("\n--- Question 1 ---")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)


# Question 2: Square and Cube

print("\n--- Question 2 ---")

num = float(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square:", square)
print("Cube:", cube)


# Question 3: Comparison with 100

print("\n--- Question 3 ---")

num = float(input("Enter a number: "))

if num > 100:
    print("The number is greater than 100.")
elif num < 100:
    print("The number is less than 100.")
else:
    print("The number is equal to 100.")
    
    
# Question 4: Equal or Not Equal

print("\n--- Question 4 ---")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")
    

# Question 5: Marks and Attendance

print("\n--- Question 5 ---")

marks = float(input("Enter student's marks: "))
attendance = float(input("Enter attendance percentage: "))

if marks >= 40 and attendance >= 75:
    print("The student satisfies both conditions.")
else:
    print("The student does not satisfy both conditions.")
    
    
# Question 6: Age Check

print("\n--- Question 6 ---")

age = int(input("Enter your age: "))

if age < 18 or age > 60:
    print("The person is either below 18 or above 60.")
else:
    print("The person is between 18 and 60.")
    
    
# Question 7: Reverse Boolean Value

print("\n--- Question 7 ---")

value = True

print("Original value:", value)
print("Reversed value:", not value)


# Question 8: Assignment Operators

print("\n--- Question 8 ---")

balance = 1000

print("Initial balance:", balance)

balance += 500
print("After adding 500:", balance)

balance -= 200
print("After subtracting 200:", balance)

balance *= 2
print("After multiplying by 2:", balance)


# Question 9: Operator Precedence

print("\n--- Question 9 ---")

result = 10 + 5 * 2 ** 2

print("Result:", result)


# Question 10: Multi-Operation Calculator

print("\n--- Question 10 ---")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\n--- Calculator Results ---")
print(f"Addition:       {num1 + num2}")
print(f"Subtraction:    {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division:       {num1 / num2}")
print(f"Modulus:        {num1 % num2}")
print(f"Power:          {num1 ** num2}")