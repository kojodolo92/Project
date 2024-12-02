import random
import string

def generate_password(length=12, include_symbols=true):
    characters = string.ascii_letters # includes both uppercase and lowercase letters

    if include_symbols:
        characters += string.punctuation # add symbols
    if include_numbers:
        characters += string.digits # add digits

    password = ''.join(random.choice(characters)for i in range(length))  
    return password

def main():
    print("Welcome to the password Generator")

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the password length.")

    include_symbols = input("include symbles? (yes/no): ").strip().lower() == 'yes'
    include_numbers = input("include numbers? (yes/no): ").strip().lower() == 'yes'

    password = generate_password(length, include_symbols, include_numbers)
    print(f"Your generated password is: {password}")     

if __name__=="__main__":
    main()              