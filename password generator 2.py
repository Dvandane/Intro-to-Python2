import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    min_length = 10

    # Ensure the password length is at least the minimum length
    if length < min_length:
        length = min_length

    # Ensure at least one of each required character type
    password = [
        random.choice(string.ascii_uppercase),  # Adds at least one uppercase letter
        random.choice(string.digits),          # Adds at least one digit
        random.choice(string.punctuation)      # Adds at least one special character
    ]

    # subtracts the 3 guarenteed characters from the length that the user chooses 
    remaining_length = length - len(password)
    # Fill the rest of the password with random characters
    password += [random.choice(characters) for _ in range(remaining_length)]

    # Shuffle to ensure randomness - the guarenteed characters would always appear in the front if not
    random.shuffle(password)

    # Convert list to string and return
    return ''.join(password)

def main():
    length = int(input("How long should the password be? "))

    password = generate_password(length)
    print("Here is your password:", password)

main()
