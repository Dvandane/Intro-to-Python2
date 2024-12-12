import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special):
    # Start with lowercase letters as the base - if they say no to uppercase, numbers and special characters it uses this
    characters = string.ascii_lowercase

    # Add character types based on what the user chooses
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # makes sure the password has at least 10 characters
    min_length = 10
    if length < min_length:
        length = min_length

    # joins the previous conditions and adds random choice
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# asks the user how long the password should be
def main():
    length = int(input("How long should the password be? "))

# asks the user what they want the password to include - uppercase, numbers, special characters
    print("Do you want the password to include:")
    use_uppercase = input("Uppercase letters? (yes/no): ") == "yes"
    use_numbers = input("Numbers? (yes/no): ") == "yes"
    use_special = input("Special characters? (yes/no): ") == "yes"
# generates and gives the user the password
    password = generate_password(length, use_uppercase, use_numbers, use_special)
    print("Here is your password:", password)

main()