# 1. Print numbers from 1 to 10 using a while loop

print("\n--- Question 1 ---")

i = 1

while i <= 10:
    print(i)
    i += 1


# 2. Print all even numbers from 1 to 50 using for loop and range()

print("\n--- Question 2 ---")

for i in range(2, 51, 2):
    print(i)


# 3. Multiplication table from 1 to 10

print("\n--- Question 3 ---")

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 4. Calculate the sum of numbers from 1 to N using while loop

print("\n--- Question 4 ---")

n = int(input("Enter N: "))

total = 0
i = 1

while i <= n:
    total += i
    i += 1

print("Sum =", total)


# 5. Calculate factorial using for loop

print("\n--- Question 5 ---")

number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial =", factorial)


# 6. Print star pattern using nested loops

print("\n--- Question 6 ---")

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()


# 7. Print number pattern using nested loops

print("\n--- Question 7 ---")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# 8. Print numbers from 1 to 20, skipping numbers divisible by 3

print("\n--- Question 8 ---")

for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)


# 9. Search for a given number using break

print("\n--- Question 9 ---")

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

search_number = int(input("Enter the number to search: "))

found = False

for number in numbers:
    if number == search_number:
        print("Number found:", search_number)
        found = True
        break

if not found:
    print("Number not found.")


# 10. Check whether a number is prime

print("\n--- Question 10 ---")

number = int(input("Enter a number: "))

if number <= 1:
    print(number, "is not a prime number.")
else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")