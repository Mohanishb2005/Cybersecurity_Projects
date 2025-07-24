import random
import string

def password_generator(len=10):
    #define characters to use in password
    characters = string.ascii_letters + string.digits + string.punctuation
    #Generate password by randomly selecting the characters
    password = ''.join(random.choice(characters) for _ in range(len))

    return password

if __name__=="__main__":
    password_length = int(input("Enter the password length:"))
    if password_length < 8:
        print("Password length must be atleast 8 characters")

    else:
        generated_password = password_generator(password_length) 
        print("Generated Password:",generated_password)   