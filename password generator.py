import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_passwords(num_passwords, length):
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length)
        passwords.append(password)
    return passwords

def main():
    num_passwords = 100000
    password_length = 100000

    passwords = generate_passwords(num_passwords, password_length)

    for password in passwords:
        print(password)

if __name__ == '__main__':
    main()
