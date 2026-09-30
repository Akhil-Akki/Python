# 1. String Indexing

print("\n--- Question 1 ---")

text = "Python Programming"

print("First character:", text[0])
print("Last character:", text[-1])
print("5th character:", text[4])
print("Last 5 characters:", text[-5:])


# 2. String Slicing

print("\n--- Question 2 ---")

text = input("Enter a string: ")

print("First 5 characters:", text[:5])
print("Last 5 characters:", text[-5:])
print("Characters from index 2 to 7:", text[2:8])
print("String in reverse:", text[::-1])


# 3. Uppercase & Lowercase

print("\n--- Question 3 ---")

name = input("Enter your name: ")

print("Original name:", name)
print("Uppercase name:", name.upper())
print("Lowercase name:", name.lower())


# 4. Replace Text

print("\n--- Question 4 ---")

sentence = input("Enter a sentence containing the word 'Python': ")

new_sentence = sentence.replace("Python", "Programming")

print("Original sentence:", sentence)
print("Updated sentence:", new_sentence)


# 5. Split a Sentence

print("\n--- Question 5 ---")

sentence = input("Enter a sentence: ")

words = sentence.split()

print("Resulting list:", words)

print("Each word:")
for word in words:
    print(word)


# 6. Join Words

print("\n--- Question 6 ---")

words = ["Python", "is", "very", "easy"]

space_sentence = " ".join(words)
hyphen_sentence = "-".join(words)
comma_sentence = ",".join(words)

print("Separated by spaces:", space_sentence)
print("Separated by -:", hyphen_sentence)
print("Separated by commas:", comma_sentence)


# 7. Name Formatting

print("\n--- Question 7 ---")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

first_name = first_name.strip()
last_name = last_name.strip()

full_name = f"{first_name.title()} {last_name.title()}"

print("Full Name:", full_name)


# 8. F-String Bill

print("\n--- Question 8 ---")

product_name = input("Enter product name: ")
price = float(input("Enter price: ₹"))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("\n----- BILL -----")
print(f"Product: {product_name}")
print(f"Price: ₹{price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: ₹{total:.2f}")


# 9. Palindrome Checker

print("\n--- Question 9 ---")

word = input("Enter a word: ")

word = word.strip().lower()

if word == word[::-1]:
    print("Output: Palindrome")
else:
    print("Output: Not a Palindrome")


# 10. Word Counter

print("\n--- Question 10 ---")

sentence = input("Enter a sentence: ")

words = sentence.split()
word_count = len(words)

print(f"Number of words: {word_count}")


# 11. Character Counter

print("\n--- Question 11 ---")

text = input("Enter a string: ")

total_characters = len(text)
spaces = text.count(" ")

vowels = 0
consonants = 0

for character in text.lower():
    if character in "aeiou":
        vowels += 1
    elif character.isalpha():
        consonants += 1

print("Total characters:", total_characters)
print("Number of spaces:", spaces)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)


# 12. Vowel Counter

print("\n--- Question 12 ---")

text = input("Enter a string: ").lower()

a_count = text.count("a")
e_count = text.count("e")
i_count = text.count("i")
o_count = text.count("o")
u_count = text.count("u")

print("a =", a_count)
print("e =", e_count)
print("i =", i_count)
print("o =", o_count)
print("u =", u_count)


# 13. Remove Spaces

print("\n--- Question 13 ---")

sentence = input("Enter a sentence: ")

new_sentence = sentence.replace(" ", "")

print("Output:", new_sentence)


# 14. Reverse Each Word

print("\n--- Question 14 ---")

sentence = input("Enter a sentence: ")

words = sentence.split()

reversed_words = []

for word in words:
    reversed_words.append(word[::-1])

result = " ".join(reversed_words)

print("Output:", result)


# 15. String Analyzer

print("\n--- Question 15 ---")

sentence = input("Enter a sentence: ")

uppercase = sentence.upper()
lowercase = sentence.lower()
words = sentence.split()
number_of_words = len(words)
number_of_characters = len(sentence)

vowel_count = 0

for character in sentence.lower():
    if character in "aeiou":
        vowel_count += 1

reversed_sentence = sentence[::-1]

print("\n----- STRING ANALYZER -----")
print(f"Original sentence: {sentence}")
print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Number of words: {number_of_words}")
print(f"Number of characters: {number_of_characters}")
print(f"Number of vowels: {vowel_count}")
print(f"Reversed sentence: {reversed_sentence}")