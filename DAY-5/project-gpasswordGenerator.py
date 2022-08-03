'''
This is a password generator with unique letter symbols and characters
'''

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
lettersi = int(input("How many letters would you like in your password?"))
symbolsi = int(input("How many symbols would you like?"))
numbersi = int(input("Ho many numbers would you like?"))
password_list = []

for char in range(1,lettersi +1):
    password_list.append(random.choice(letters))
for sym in range(1,symbolsi + 1):
    password_list.append(random.choice(symbols))
for num in range(1,numbersi + 1):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Here is your password: {password}")

