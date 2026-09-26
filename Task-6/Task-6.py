# 1. Create a list of 10 student names

print("\n--- Question 1 ---")

students = [
    "Akhil",
    "Mahathi",
    "Priya",
    "Kajal",
    "Sneha",
    "Divya",
    "Manisha",
    "Shiva",
    "Ananya",
    "Raju"
]

print("First student:", students[0])
print("Last student:", students[-1])
print("Students from index 2 to 6:", students[2:7])


# 2. List operations using append(), insert(), and remove()

print("\n--- Question 2 ---")

numbers = [10, 20, 30, 40, 50]

numbers.append(60)

numbers.insert(2, 25)

numbers.remove(40)

print("Final list:", numbers)


# 3. Remove duplicate values using a set

print("\n--- Question 3 ---")

numbers = [10, 20, 10, 30, 20, 40, 30, 50, 40]

print("Original list:", numbers)

unique_numbers = set(numbers)

print("Set without duplicates:", unique_numbers)


# 4. Set operations for Python and Java students

print("\n--- Question 4 ---")

python_students = {"Akhil", "Mahathi", "Priya", "Divya", "Sneha"}
java_students = {"Kajal", "Manisha", "Shiva", "Ananya", "Raju"}

both_courses = python_students.intersection(java_students)

only_python = python_students.difference(java_students)

all_students = python_students.union(java_students)

print("Students enrolled in both courses:", both_courses)
print("Students enrolled only in Python:", only_python)
print("All unique students:", all_students)


# 5. Tuple indexing and slicing

print("\n--- Question 5 ---")

days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

print("First day:", days[0])
print("Last day:", days[-1])
print("Middle days:", days[2:5])


# 7. Student dictionary

print("\n--- Question 7 ---")

student = {
    "Name": "Akhil",
    "Age": 24,
    "City": "Hyderabad",
    "Course": "Python",
    "Marks": 99
}

print("Name:", student["Name"])
print("Age:", student["Age"])
print("City:", student["City"])
print("Course:", student["Course"])
print("Marks:", student["Marks"])


# 8. Product dictionary and total price

print("\n--- Question 8 ---")

product = {
    "Name": "Laptop",
    "Price": 50000,
    "Quantity": 2,
    "Category": "Electronics"
}

total_price = product["Price"] * product["Quantity"]

print("Product Name:", product["Name"])
print("Price:", product["Price"])
print("Quantity:", product["Quantity"])
print("Category:", product["Category"])
print("Total Price:", total_price)


# 9. List of dictionaries containing 5 students

print("\n--- Question 9 ---")

students = [
    {"Name": "Akhil", "Age": 22, "Marks": 99},
    {"Name": "Raju", "Age": 21, "Marks": 78},
    {"Name": "Priya", "Age": 22, "Marks": 92},
    {"Name": "Mahathi", "Age": 20, "Marks": 84},
    {"Name": "Divya", "Age": 21, "Marks": 88}
]

for student in students:
    print("Name:", student["Name"])
    print("Age:", student["Age"])
    print("Marks:", student["Marks"])
    print("--------------------")
    
    
# 10. Student Record Management

print("\n--- Question 10 ---")

students = []


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = float(input("Enter student marks: "))

    student = {
        "Name": name,
        "Age": age,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully.")


def display_students():
    if not students:
        print("No student records found.")
        return

    print("\nStudent Records:")

    for student in students:
        print("Name:", student["Name"])
        print("Age:", student["Age"])
        print("Marks:", student["Marks"])
        print("--------------------")


def search_student():
    name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["Name"].lower() == name.lower():
            print("\nStudent found:")
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Marks:", student["Marks"])
            found = True
            break

    if not found:
        print("Student not found.")


def update_marks():
    name = input("Enter student name to update marks: ")

    for student in students:
        if student["Name"].lower() == name.lower():
            new_marks = float(input("Enter new marks: "))
            student["Marks"] = new_marks
            print("Marks updated successfully.")
            return

    print("Student not found.")


def remove_student():
    name = input("Enter student name to remove: ")

    for student in students:
        if student["Name"].lower() == name.lower():
            students.remove(student)
            print("Student removed successfully.")
            return

    print("Student not found.")


def highest_marks():
    if not students:
        print("No student records found.")
        return

    highest_student = max(students, key=lambda student: student["Marks"])

    print("\nStudent with the highest marks:")
    print("Name:", highest_student["Name"])
    print("Age:", highest_student["Age"])
    print("Marks:", highest_student["Marks"])

while True:
    print("\n===== Student Record Management =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Remove Student")
    print("6. Display Student with Highest Marks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        remove_student()

    elif choice == "6":
        highest_marks()

    elif choice == "7":
        print("Thank you for using Student Record Management.")
        break

    else:
        print("Invalid choice. Please try again.")
        
        
# 6. Trying to modify a tuple

print("\n--- Question 6 ---")

numbers = (10, 20, 30, 40, 50)

print("Original tuple:", numbers)

numbers[1] = 25

print("Modified tuple:", numbers)