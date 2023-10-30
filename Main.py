# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

while True:
    print("Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "5":
        break

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result: ", add(num1, num2))
        elif choice == '2':
            print("Result: ", subtract(num1, num2))
        elif choice == '3':
            print("Result: ", multiply(num1, num2))
        elif choice == '4':
            print("Result: ", divide(num1, num2))
    else:
        print("Invalid choice. Please try again.")

3. **Password Generator - Python**:

```python
import random
import string

def generate_password(length, include_uppercase, include_digits, include_special_chars):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if len(characters) == 0:
        return "Error: No character set selected"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter password length: "))
include_uppercase = input("Include uppercase letters (yes/no): ").lower() == "yes"
include_digits = input("Include digits (yes/no): ").lower() == "yes"
include_special_chars = input("Include special characters (yes/no): ").lower() == "yes"

password = generate_password(length, include_uppercase, include_digits, include_special_chars)
print("Generated Password: " + password)
