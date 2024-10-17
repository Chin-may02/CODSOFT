import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the password lenngth (at least 6): "))
            if length < 6:
                print("Please choose at least 6 characters ")
            else:
                break
        except ValueError:
            print("Invalid number try again")

    password = generate_password(length)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
