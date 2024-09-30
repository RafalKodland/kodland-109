import random

signs = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("Jak długie ma być hasło? "))
password = ""

for i in range(length):
    password += random.choice(signs)

print(password)