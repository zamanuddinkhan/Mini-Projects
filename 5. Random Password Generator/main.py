import secrets
import string

chars = string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter password length: "))

password = ""

for a in range(length):
    password += secrets.choice(chars)

print("Your password:", password)