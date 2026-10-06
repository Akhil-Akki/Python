# 1. CREATE A FILE

print("\n--- Question 1 ---")

with open("welcome.txt", "w") as file:
    file.write("Welcome to Python\n")
    file.write("I am learning File Handling\n")

print("welcome.txt created successfully.")


# 2. WRITE STUDENT DATA

print("\n--- Question 2 ---")

name = input("Enter student name: ")
age = input("Enter student age: ")
course = input("Enter course: ")
marks = input("Enter marks: ")

with open("student.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Course: {course}\n")
    file.write(f"Marks: {marks}\n")

print("Student data saved successfully.")


# 3. READ A FILE

print("\n--- Question 3 ---")

with open("student_names.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Priya\n")
    file.write("Arun\n")
    file.write("Sneha\n")
    file.write("Kiran\n")

with open("student_names.txt", "r") as file:
    names = file.read()

print("Student names:")
print(names)


# 4. READ LINE BY LINE

print("\n--- Question 4 ---")

with open("text_lines.txt", "w") as file:
    file.write("Python is easy to learn.\n")
    file.write("Python supports file handling.\n")
    file.write("Python supports functions.\n")
    file.write("Python supports exception handling.\n")
    file.write("Python is widely used.\n")

with open("text_lines.txt", "r") as file:
    for line in file:
        print(line.strip())


# 5. APPEND DATA

print("\n--- Question 5 ---")

with open("students.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Priya\n")
    file.write("Arun\n")

new_student = input("Enter another student name: ")

with open("students.txt", "a") as file:
    file.write(new_student + "\n")

print("New student added successfully.")

print("Updated student list:")

with open("students.txt", "r") as file:
    print(file.read())


# 6. COUNT LINES

print("\n--- Question 6 ---")

try:
    with open("text_lines.txt", "r") as file:
        lines = file.readlines()

    print("Total lines:", len(lines))

except FileNotFoundError:
    print("File not found.")


# 7. COUNT WORDS IN A FILE

print("\n--- Question 7 ---")

try:
    with open("text_lines.txt", "r") as file:
        content = file.read()

    words = content.split()

    print("Total words:", len(words))

except FileNotFoundError:
    print("File not found.")


# 8. HANDLE FILE NOT FOUND

print("\n--- Question 8 ---")

filename = input("Enter a filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    print("File content:")
    print(content)

except FileNotFoundError:
    print("File not found.")


# 9. HANDLE INVALID INPUT

print("\n--- Question 9 ---")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ValueError:
    print("Invalid numeric input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# 10. USE FINALLY

print("\n--- Question 10 ---")

try:
    number = float(input("Enter a number: "))

    square = number ** 2

    print("Square:", square)

except ValueError:
    print("Invalid input. Please enter a number.")

finally:
    print("Program completed.")


# 11. STUDENT DATA MANAGEMENT

print("\n--- Question 11 ---")


def add_student():
    try:
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        course = input("Enter course: ")
        marks = input("Enter marks: ")

        with open("students_management.txt", "a") as file:
            file.write(
                f"Name: {name}, Age: {age}, Course: {course}, Marks: {marks}\n"
            )

        print("Student added successfully.")

    except ValueError:
        print("Invalid input.")

    except Exception as error:
        print("Error:", error)


def view_students():
    try:
        with open("students_management.txt", "r") as file:
            content = file.read()

        if content:
            print("\nStudent Records:")
            print(content)
        else:
            print("No students found.")

    except FileNotFoundError:
        print("No student file found.")


while True:
    print("\n--- Student Data Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Exiting Student Data Management.")
        break

    else:
        print("Invalid choice.")


# 12. STUDENT MARKS VALIDATION

print("\n--- Question 12 ---")

try:
    name = input("Enter student name: ")

    try:
        age = int(input("Enter student age: "))
    except ValueError:
        print("Age must be an integer.")
        age = None

    try:
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Marks must be a number.")
        marks = None

    if age is not None and marks is not None:

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")

        else:
            with open("valid_students.txt", "a") as file:
                file.write(
                    f"Name: {name}, Age: {age}, Marks: {marks}\n"
                )

            print("Valid student data stored successfully.")

except Exception as error:
    print("Error:", error)


# 13. SEARCH STUDENT

print("\n--- Question 13 ---")

with open("student_search.txt", "w") as file:
    file.write("Akhil - 85\n")
    file.write("Priya - 92\n")
    file.write("Abhinaya - 78\n")
    file.write("Manisha - 95\n")
    file.write("Meghana - 88\n")

search_name = input("Enter student name to search: ")

try:
    found = False

    with open("student_search.txt", "r") as file:
        for line in file:
            student_name = line.split("-")[0].strip()

            if student_name.lower() == search_name.lower():
                found = True
                break

    if found:
        print("Student found")
    else:
        print("Student not found")

except FileNotFoundError:
    print("File not found.")


# 14. STUDENT RECORD SYSTEM

print("\n--- Question 14 ---")


def add_record():
    try:
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        course = input("Enter course: ")
        marks = float(input("Enter marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        with open("student_records.txt", "a") as file:
            file.write(
                f"{name}|{age}|{course}|{marks}\n"
            )

        print("Student record added successfully.")

    except ValueError:
        print("Invalid input. Age must be an integer and marks must be a number.")

    except Exception as error:
        print("Error:", error)

def view_records():
    try:
        with open("student_records.txt", "r") as file:
            records = file.readlines()

        if not records:
            print("No student records found.")
            return

        print("\n--- Student Records ---")

        for record in records:
            data = record.strip().split("|")

            if len(data) == 4:
                print("Name:", data[0])
                print("Age:", data[1])
                print("Course:", data[2])
                print("Marks:", data[3])
                print("----------------------")

    except FileNotFoundError:
        print("Student record file not found.")

    except Exception as error:
        print("Error:", error)


def search_record():
    try:
        search_name = input("Enter student name to search: ")
        found = False

        with open("student_records.txt", "r") as file:
            for record in file:
                data = record.strip().split("|")

                if len(data) == 4 and data[0].lower() == search_name.lower():
                    print("\nStudent found")
                    print("Name:", data[0])
                    print("Age:", data[1])
                    print("Course:", data[2])
                    print("Marks:", data[3])

                    found = True
                    break

        if not found:
            print("Student not found.")

    except FileNotFoundError:
        print("Student record file not found.")

    except Exception as error:
        print("Error:", error)


while True:
    print("\n--- Student Record System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_record()

    elif choice == "2":
        view_records()

    elif choice == "3":
        search_record()

    elif choice == "4":
        print("Exiting Student Record System.")
        break

    else:
        print("Invalid choice.")


# 15. MINI FILE-BASED STUDENT MANAGEMENT SYSTEM

print("\n--- Question 15 ---")


def add_student_final():
    try:
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        course = input("Enter course: ")
        marks = float(input("Enter marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        # "a" mode adds new data without deleting existing data.
        with open("students.txt", "a") as file:
            file.write(
                f"{name}|{age}|{course}|{marks}\n"
            )

        print("Student added successfully.")

    except ValueError:
        print("Invalid input. Please enter valid age and marks.")

    finally:
        print("Add Student operation completed.")


def view_all_students():
    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

        if not records:
            print("No student records found.")
            return

        print("\n--- All Students ---")

        for record in records:
            data = record.strip().split("|")

            if len(data) == 4:
                print("Name:", data[0])
                print("Age:", data[1])
                print("Course:", data[2])
                print("Marks:", data[3])
                print("-------------------------")

    except FileNotFoundError:
        print("File not found.")

    finally:
        print("View operation completed.")


def search_student_final():
    try:
        search_name = input("Enter student name to search: ")
        found = False

        with open("students.txt", "r") as file:
            for record in file:
                data = record.strip().split("|")

                if len(data) == 4:
                    if data[0].lower() == search_name.lower():
                        print("\nStudent found")
                        print("Name:", data[0])
                        print("Age:", data[1])
                        print("Course:", data[2])
                        print("Marks:", data[3])

                        found = True
                        break

        if not found:
            print("Student not found")

    except FileNotFoundError:
        print("File not found.")

    finally:
        print("Search operation completed.")


while True:
    print("\n--- Mini Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Add More Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student_final()

    elif choice == "2":
        view_all_students()

    elif choice == "3":
        search_student_final()

    elif choice == "4":
        add_student_final()

    elif choice == "5":
        print("Thank you for using Student Management System.")
        break

    else:
        print("Invalid choice. Please select 1 to 5.")