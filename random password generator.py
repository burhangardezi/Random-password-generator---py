import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
length = ''
number = 2
length = input('Input password length')
length = int(length)

password = ''
for p in range(length):
    password += random.choice(chars)

print(password)