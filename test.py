import math
import time
import random
import os
import shutil
import messages
from messages import *

# print("hello world!")
# this is a comment

# input
# number1 = int(input("Enter number 1: "))
# number2 = int(input("Enter number 2: "))

# if else
# if number1 > number2:
#     print("Number 1 is greater than Number 2")
# else:
#     print("Number 2 is greater than Number 1")
# print(number1, number2)

# assigning 2 variables
# height, width = 100, 200
# print(height, width)
#
# name = input('your name: ')
# print('your name is ' + name)

# operators
# print(135 // 2)
# print(2**2)
# a = 5
# a

# string formating
# a = 100
# print('Value = ' + str(a))

# print(f'Formatted \n{5+4}')

# string functions
# name = "shashank"
# print(len(name))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.replace('s', 'r'))
# print(name.find('s'))
# print(name.count('s'))
# print(name*3)
# print(f'\n{name}')

# type casting
# print(type(name))
# print(type(4))

# num = 1.2
# num = int(num)
# print(num)
#
# print(str(num) * 3)

# math functions
# pi = 3.14
# print(round(pi))
# print(math.floor(pi))
# print(math.ceil(pi))
# print(abs(pi))
# print(pow(pi, 2))
# print(math.sqrt(pi))
# print(max(4,5,6))
# print(min(4,5,6))

# string slicing
# name = 'Shashank'
# print(name[0:5:2])
# reversed = name[::-1]
# print(reversed)
#
# slice = slice(1,-2)
# print(name[slice])

# branching
# age = 8
# if age >= 18:
#     print("Adult")
# elif age > 13:
#     print("Teenager")
# else:
#     print("Kid")
#
# temp = 26
# if temp >= 20 and temp <= 30:
#     print("its ideal")
# else:
#     print("its not ideal")


# if 20 >= temp >= 30:
#     print("its ideal")
# else:
#     print("its not ideal")
#
# if not(5 < 4):
#     print("false")

# while loop
# name = None
# while not name:
#     name = input('Enter your name: ')
#
# print(f'Your name is {name}')

# for loop
# for i in range(1, 10+1, 2):
#     print(i)
#
# for i in "hello world":
#     print(i)
#
# for i in range(5, 0, -1):
#     print(i)
#     time.sleep(1)

# sleeping in current thread
# time.sleep(2) # in seconds

# nested loops
# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol:")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end = '')
#     print()

# break
# while True:
#     name = input("Enter your name: ")
#     if name != '':
#         break

# continue
# for i in "123-456-7890":
#     if i == '-':
#         continue
#     print(i, end = '')

# pass- just a placeholder keyword
# for i in range(1, 20, 1):
#     if i == 13:
#         pass
#     else:
#         print(i)

# lists
# food = ["Pizza", "Burger", "Dosa"]
# print(food)
# print(food[0])
# print(food[1])
# print(food[5]) # error- index out of range

# print('\nLooping through..')
# food[0] = 'Noodles'
# food.append("Chilli Potato")
# food.pop()
# food.insert(1, "Cake")
# food.sort()
# food.clear()
# for i in food:
#     print(i)

# 2d lists
# drinks = ["Coffe", "Soda"]
# dinner = ["Pizza", "Burger", "Dosa"]
# dessert = ["Cake", "Ice-cream"]
#
# food = [drinks, dinner, dinner]
#
# for i in food:
#     for j in i:
#         print(j)
#
# print(food[1][2])

# tuples
# student = ("Bro", 1, "Code")
# print(student)
# print(student[1])
# print(student.count("Bro"))
# print(student.index("Bro"))
#
# if "Bro" in student:
#     print("Bro is here")

# sets
# utensils = {"fork", "spoon", "knife", "knife"}
# utensils.remove("fork")
# utensils.add("bowl")
# print(utensils)
# print(utensils)
# utensils.clear()
# print(utensils)

# utensils2 = {"Cup"}
# utensils2.update(utensils)
# print(utensils2)

# print(utensils.union(utensils2))
# print(utensils.difference(utensils2))
# print(utensils.intersection(utensils2))

# dictionaries
# dict = {'USA': 'Washington DC', 'India': 'New Delhi', 'China': 'Beijing', 'Russia': 'Moscow'}
# print(dict)
# print(dict['USA'])
# print(dict.get('abc'))
# print(dict.get('India'))
#
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# dict.update({'Germany': 'Berlin'})
# dict.pop('Germany')
#
# for key,value in dict.items():
#     print(key, value)
#
# # functions, arguments and parameters
# def hello(name):
#     print('Hello ' + name)
#
# hello("Shashank")
# hello("Dave")
# hello("Nish")
#
# def multiply(a, b):
#     return a*b
#
# value = multiply(2, 3)
# print(value)

# # keyword arguments or named parameters
# hello(name='Dave')
#
# # args parameter
# def add(*args):
#     sum = 0;
#     for i in args:
#         sum += i
#     return sum
#
# print(add(1,2,3,4,5,6,7,8,9,10))
#
# # **kwargs- keyword argument parameter // gives a dictionary instead of a list
# def greet(**kwargs):
#     print("Hello ", end='')
#     for key, value in kwargs.items():
#         print(value, end=' ')
#
# greet(title = "Mr.", first = "Shashank", last = "Nanda")
#
# # format() method
# print("Hello {}".format("Shashank"))
#
# # positional arguments in format() method
# print("Hello {1} & {0}".format("Krish", "Nish"))
#
# # padding
# print("Hello {:10} Bhai".format("Shashank"))
#
# # left & right align
# print("Hello {:<10} Bhai".format("Shashank"))
# print("Hello {:>10} Bhai".format("Shashank"))
#
# # formatting numbers
# pi = math.pi
# print("The number is {:.3f}".format(pi)) # rounding upto x decimals
# print("The number is {:,}".format(1000))
# print("The number is {:b}".format(1000))
# print("The number is {:o}".format(1000))
# print("The number is {:X}".format(1000))
# print("The number is {:E}".format(1000))
#
# # generating random numbers
# print(random.random())
# print(random.randint(1,10))
#
# mylist = ['First', 'Second', 'Third']
# print(random.choice(mylist))
# # or
# randindex = random.randint(0, 2)
# print(mylist[randindex])
#
# mynums = [1,2,3,4,5,6,7,8,9,10]
# random.shuffle(mynums)
# print(mynums)

# exception handling
# try:
#     num1 = int(input('Enter number 1: '))
#     num2 = int(input('Enter number 2: '))
#
#     num3 = num1 / num2
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# else:
#     print('No errors!')
# finally:
#     print('This will execute no matter what!')

# file handling
# checking if a path exists & whether it is a file or a directory
# path = "/Users/shashanknanda/Desktop/20240914022225_JBR68393.jpg"
# if os.path.exists(path):
#     print("Path exists")
#
#     if os.path.isfile(path) :
#         print("And its a file")
#     elif os.path.isdir(path):
#         print("And its a directory")
# else:
#     print("Path does not exist")
#
# # reading a file
# try:
#     with open('test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found")
#
# # writing & appending to a file
# try:
#     with open('test.txt', 'a') as file:
#         file.write("\nThis is some more more text")
# except:
#     print("Something went wrong")
#
# # copy a file
# try:
#     shutil.copyfile('test.txt', 'test2.txt')
# except:
#     print("Something went wrong")
#
# # move a file
# try:
#     os.replace("test.txt", "test3.txt")
# except:
#     print("Something went wrong")
#
# # remove a file
# try:
#     os.remove("test3.txt") # delete a file
#     os.rmdir("dir") # delete an empty directory
#     shutil.rmtree("dir") # delete an non-empty directory
# except:
#     print("Something went wrong")
#
# # modules
# help("modules")
#
# messages.hello()
# messages.bye()
# hello()
# bye()

# object oriented programming
class Animal:
    name = ''
    weight = 0

    def __init__(self, name):
        self.name = name

    def walk(self):
        print(self.name + " is walking and its weight is " + str(self.weight))

Animal.weight = 100

a1 = Animal('A1')
a1.weight = 200

a2 = Animal('A2')

a1.walk()
a2.walk()
