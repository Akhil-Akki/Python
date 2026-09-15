# ============================================================
# PYTHON TASKS
# ============================================================


# ============================================================
# Question 1
# Store name, age, height, and student status
# ============================================================

print("\n--- Question 1 ---")

name = "Akhil"
age = 22
height = 5.8
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)


# ============================================================
# Question 2
# Sum, difference, product, and division of two numbers
# ============================================================

print("\n--- Question 2 ---")

num1 = 20
num2 = 5

print("First Number:", num1)
print("Second Number:", num2)
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)


# ============================================================
# Question 3
# Display type before and after converting to int
# ============================================================

print("\n--- Question 3 ---")

number = input("Enter a number: ")

print("Data type before conversion:", type(number))

number = int(number)

print("Data type after conversion:", type(number))
print("Value:", number)


# ============================================================
# Question 4
# Age after 5 years
# ============================================================

print("\n--- Question 4 ---")

age_string = input("Enter your age: ")

age = int(age_string)

future_age = age + 5

print("Your age after 5 years will be:", future_age)


# ============================================================
# Question 5
# Product price with 2 decimal places
# ============================================================

print("\n--- Question 5 ---")

price_string = input("Enter the product price: ")

price = float(price_string)

print(f"Price: ₹{price:.2f}")


# ============================================================
# Question 6
# Display name and age using f-string
# ============================================================

print("\n--- Question 6 ---")

person_name = input("Enter your name: ")
person_age = input("Enter your age: ")

print(f"My name is {person_name} and I am {person_age} years old.")


# ============================================================
# Question 7
# Area of a circle
# ============================================================

print("\n--- Question 7 ---")

radius = float(input("Enter the radius of the circle: "))

pi = 3.14159

area = pi * radius * radius

print(f"Area of the circle: {area:.2f}")


# ============================================================
# Question 8
# Area and perimeter of a rectangle
# ============================================================

print("\n--- Question 8 ---")

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

rectangle_area = length * width
perimeter = 2 * (length + width)

print(f"Area of rectangle: {rectangle_area:.2f}")
print(f"Perimeter of rectangle: {perimeter:.2f}")


# ============================================================
# Question 9
# Total and average marks of five subjects
# ============================================================

print("\n--- Question 9 ---")

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))
mark4 = float(input("Enter marks for Subject 4: "))
mark5 = float(input("Enter marks for Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5

print("\n----- Marks Result -----")
print(f"Subject 1 : {mark1:.2f}")
print(f"Subject 2 : {mark2:.2f}")
print(f"Subject 3 : {mark3:.2f}")
print(f"Subject 4 : {mark4:.2f}")
print(f"Subject 5 : {mark5:.2f}")
print("------------------------")
print(f"Total     : {total:.2f}")
print(f"Average   : {average:.2f}")


# ============================================================
# Question 10 Formatted product bill
# ============================================================

print("\n--- Question 10 ---")

product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total_price = product_price * quantity

print("\n================================")
print("           PRODUCT BILL")
print("================================")
print(f"Product Name : {product_name}")
print(f"Quantity     : {quantity}")
print(f"Price        : ₹{product_price:.2f}")
print("--------------------------------")
print(f"Total Price  : ₹{total_price:.2f}")
print("================================")