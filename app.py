#Learning Python
#https://youtu.be/rfscVS0vtbw

from math import *

character_name = "John"
character_age = "35"

print("There once was a man named " + character_name + ".")
print("He was " + character_age + " years old.")

character_age_int = 35
#This will fail because you can not concantenate int.
#print("He was " + character_age_number + " years old.")

#concatenation
phrase="Giraffe Academy"

#Sample functions for the string
print(phrase.lower())
print(phrase.isupper())
print(phrase.upper().isupper())

#Get the length of the string
print(len(phrase))

#Get the index of the string
print(phrase[0])
print(phrase.index("f"))
print(phrase.replace("Giraffe","Elephant"))

#Numbers

print(3 * 4.5)
print(34 * 3.2034030034)
print(10 % 3)

my_num = 5
print(str(my_num))
my_num = -5
print(str(my_num))
print(pow(5, 4))
print(abs(-5))
print(round(3.6))

print(sqrt(36))

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name.upper() + ", you are " + age)













