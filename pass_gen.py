import random
import string

# Take user input
length = int(input("Enter password length: "))

print("Choose character types:")
print("1. Uppercase letters")
print("2. Lowercase letters")
print("3. Numbers")
print("4. Symbols")

choices = input("Enter choices (e.g. 1234): ")

characters = ""

if '1' in choices:
    characters += string.ascii_uppercase
if '2' in choices:
    characters += string.ascii_lowercase
if '3' in choices:
    characters += string.digits
if '4' in choices:
    characters += string.punctuation

# Check if user selected at least one option
if characters == "":
    print("Please select at least one character type!")
else:
    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)
     

