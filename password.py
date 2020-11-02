import string
import random
chars=string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter the total length of password: "))

pwd =" "
while length < 6:
    length = int(input("Try again!! the lenght must be greater than 6: "))
else:
    letter = int(input("Enter the length letter: "))
    number = int(input("Enter the length number: "))
    for n in range(number):
        pwd += random.choice(string.digits)
    for l in range(letter):
        pwd += random.choice(string.ascii_letters)
        
    final_length= (length-letter-number)
    for i in range(final_length):
            pwd += random.choice(string.punctuation)
print(pwd)