# Question 1: Check whether a person is a minor or an adult

print("\n--- Question 1 ---")

age = int(input("Enter your age: "))

if age < 18:
    print("The person is a minor.")
else:
    print("The person is an adult.")
    

# Question 2: Check whether a number is positive, negative, or zero

print("\n--- Question 2 ---")

number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
    
# Question 3: Display grade based on marks 

print("\n--- Question 3 ---")

marks = float(input("Enter the student's marks: "))

if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
elif marks >= 0:
    print("Grade: F")
else:
    print("Invalid marks.")


# Question 4: Check whether a number is even or odd

print("\n--- Question 4 ---")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# Question 5: Check voting eligibility

print("\n--- Question 5 ---")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    

# Question 6: Check exam eligibility based on marks and attendance

print("\n--- Question 6 ---")

marks = float(input("Enter your marks: "))
attendance = float(input("Enter your attendance percentage: "))

if marks >= 40 and attendance >= 75:
    print("The student is eligible for the exam.")
else:
    print("The student is not eligible for the exam.")
    
    
# Question 7: Nested if - Age and valid ID

print("\n--- Question 7 ---")

age = int(input("Enter your age: "))

if age >= 18:
    id_status = input("Do you have a valid ID? (yes/no): ").lower()

    if id_status == "yes":
        print("You are 18 or older and have a valid ID.")
    else:
        print("You are 18 or older but do not have a valid ID.")
else:
    print("You are under 18.")
    
    
# Question 8: Validate username and password

print("\n--- Question 8 ---")

correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful.")
else:
    print("Invalid username or password.")
    
    
# Question 9: Find the largest of three numbers

print("\n--- Question 9 ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)
    
    
# Question 10: Simple ATM withdrawal

print("\n--- Question 10 ---")

balance = float(input("Enter your account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= 0:
    print("Invalid withdrawal amount. Amount must be positive.")
elif withdrawal > balance:
    print("Insufficient balance.")
else:
    balance = balance - withdrawal
    print("Withdrawal successful.")
    print("Remaining balance:", balance)