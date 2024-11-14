import random
import string
print("Welcome to the password generator!")
lenght = int(input("Enter the total number of characters in the password: "))
letters = int(input("Enter the number of letters in the password: "))
numbers = int(input("Enter the number of numbers in the password: "))
symbols = int(input("Enter the number of symbols in the password: "))
while lenght != numbers + letters + symbols:
  print("Sorry, the total number of characters must be equal the sum of the number of letters, numbers, and symbols.")
  lenght = int(input("Enter the total number of characters in the password: "))
  letters = int(input("Enter the number of letters in the password: "))
  numbers = int(input("Enter the number of numbers in the password: "))
  symbols = int(input("Enter the number of symbols in the password: "))
password_letters = random.choices(string.ascii_letters, k=letters)
password_numbers = random.choices(string.digits, k=numbers)
password_symbols = random.choices(string.punctuation, k=symbols)
password = (password_letters + password_numbers + password_symbols)
random.shuffle(password)
print("".join(password))