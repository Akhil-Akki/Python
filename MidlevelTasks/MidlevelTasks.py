# TASK 1 — STUDENT RESULT MANAGEMENT

print("\n--- TASK 1: STUDENT RESULT MANAGEMENT ---")

name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)

total = sum(marks)
average = total / 5

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

passed_all = True

for mark in marks:
    if mark < 40:
        passed_all = False
        break

print("\n---------- STUDENT RESULT ----------")
print(f"Student Name : {name}")
print(f"Total Marks  : {total:.2f}")
print(f"Average      : {average:.2f}")
print(f"Grade        : {grade}")
print(f"Passed All   : {'Yes' if passed_all else 'No'}")


# TASK 2 — ATM SIMULATION

print("\n--- TASK 2: ATM SIMULATION ---")

balance = 10000

while True:
    print("\nCurrent Balance: ₹", balance)
    print("1. Withdraw")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"Withdrawal successful.")
            print(f"Remaining Balance: ₹{balance:.2f}")

    elif choice == "2":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please try again.")


# TASK 3 — NUMBER ANALYSIS PROGRAM

print("\n--- TASK 3: NUMBER ANALYSIS ---")

n = int(input("Enter a number N: "))

if n < 1:
    print("Please enter a positive number.")
else:
    total_sum = 0
    even_sum = 0
    odd_sum = 0
    divisible_by_3 = 0
    largest = 1

    print("\nNumbers from 1 to", n, ":")

    for number in range(1, n + 1):
        print(number, end=" ")

        total_sum += number

        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

        if number % 3 == 0:
            divisible_by_3 += 1

        if number > largest:
            largest = number

    print("\n\nSum of all numbers:", total_sum)
    print("Sum of even numbers:", even_sum)
    print("Sum of odd numbers:", odd_sum)
    print("Numbers divisible by 3:", divisible_by_3)
    print("Largest number:", largest)


# TASK 4 — MULTIPLICATION TABLE GENERATOR

print("\n--- TASK 4: MULTIPLICATION TABLE ---")

while True:
    number = int(input("\nEnter number: "))

    print(f"\nMultiplication Table of {number}")

    for i in range(1, 11):
        print(f"{number} × {i} = {number * i}")

    again = input("\nDo you want another table? (yes/no): ").lower()

    if again != "yes":
        print("Multiplication table program stopped.")
        break


# TASK 5 — LOGIN SYSTEM

print("\n--- TASK 5: LOGIN SYSTEM ---")

correct_username = "admin"
correct_password = "python123"

logged_in = False

for attempt in range(1, 4):
    username = input("\nEnter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful")
        logged_in = True
        break

    elif username != correct_username:
        print("Incorrect username.")

    elif password != correct_password:
        print("Incorrect password.")

    print(f"Attempts remaining: {3 - attempt}")

if not logged_in:
    print("Account locked")


# TASK 6 — NUMBER GUESSING GAME

print("\n--- TASK 6: NUMBER GUESSING GAME ---")

secret_number = 35
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess > secret_number:
        print("Too high")

    elif guess < secret_number:
        print("Too low")

    else:
        print("Correct!")
        print(f"Attempts: {attempts}")
        break


# TASK 7 — PRIME NUMBER ANALYZER

print("\n--- TASK 7: PRIME NUMBER ANALYZER ---")

n = int(input("Enter N: "))

prime_numbers = []

if n >= 2:

    for number in range(2, n + 1):
        is_prime = True

        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(number)

    print("\nPrime numbers:")

    for prime in prime_numbers:
        print(prime, end=" ")

    print(f"\n\nTotal prime numbers: {len(prime_numbers)}")

else:
    print("There are no prime numbers between 1 and", n)


# TASK 8 — SHOPPING BILL SYSTEM

print("\n--- TASK 8: SHOPPING BILL SYSTEM ---")

product_count = int(input("How many products do you want to purchase? "))

subtotal = 0

for i in range(1, product_count + 1):
    print(f"\nProduct {i}")

    product_name = input("Enter product name: ")
    price = float(input("Enter price: ₹"))
    quantity = int(input("Enter quantity: "))

    product_total = price * quantity
    subtotal += product_total

    print(f"{product_name} Total: ₹{product_total:.2f}")

if subtotal > 5000:
    discount = subtotal * 0.10
elif subtotal > 2000:
    discount = subtotal * 0.05
else:
    discount = 0

final_amount = subtotal - discount

print("\n---------- SHOPPING BILL ----------")
print(f"Subtotal     : ₹{subtotal:.2f}")
print(f"Discount     : ₹{discount:.2f}")
print(f"Final Amount : ₹{final_amount:.2f}")


# TASK 9 — STUDENT ATTENDANCE & ELIGIBILITY

print("\n--- TASK 9: ATTENDANCE & ELIGIBILITY ---")

student_name = input("Enter student name: ")

marks = []

for i in range(1, 4):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)

attendance = float(input("Enter attendance percentage: "))

total = sum(marks)
average = total / 3

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

passed_all = True

for mark in marks:
    if mark < 40:
        passed_all = False
        break

attendance_eligible = attendance >= 75

if passed_all and attendance_eligible:
    eligibility = "Eligible for Exam"
else:
    eligibility = "Not Eligible for Exam"

print("\n---------- FINAL RESULT ----------")
print(f"Student Name : {student_name}")
print(f"Total Marks  : {total:.2f}")
print(f"Average      : {average:.2f}")
print(f"Grade        : {grade}")
print(f"Passed All   : {'Yes' if passed_all else 'No'}")
print(f"Attendance   : {attendance:.2f}%")
print(f"Eligibility  : {eligibility}")


# TASK 10 — MINI BANKING SYSTEM

print("\n--- TASK 10: MINI BANKING SYSTEM ---")

balance = 10000

while True:

    print("\n--- BANK MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Current Balance: ₹{balance:.2f}")

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))

        if amount <= 0:
            print("Invalid amount. Deposit must be greater than zero.")
        else:
            balance += amount
            print(f"₹{amount:.2f} deposited successfully.")
            print(f"New Balance: ₹{balance:.2f}")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Invalid amount. Withdrawal must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")
            print(f"Remaining Balance: ₹{balance:.2f}")

    elif choice == "4":
        print("Thank you for using the banking system.")
        break

    else:
        print("Invalid choice. Please select 1 to 4.")

