#while loop 1

age = 0 
while(age<18):
    print(f"your some boy. your just {age} year old")
    age += 1
print("--------------------------")

#while loop 2

num = int(input("Enter a number: "))
n = 0
while(n != num):
    print(n)
    n += 1
print("--------------------------")

#while loop 3

text = input("Enter txet to repeat: ")
num = int(input("Enter how many time: "))
n = 1
while(n != num+1):
    print(f"{n}. {text}")
    n += 1
print("--------------------------")

#while loop 4

import random
secret = random.randint(0,100)
gus = 0
a = 0
while(a != secret):
    a = int(input("Gusse the number: "))
    if a > secret:
        print("lower")
    elif a < secret:
        print("higher")
    gus += 1
else:
    print(f"you got the number {secret} in {gus} gusses")
print("--------------------------")

#while loop 5

table = int(input("Enter number of table: "))
z = 1
while (z != 11):
    print(f"{table} X {z} = {table * z}")
    z += 1