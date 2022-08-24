# #  A PROGRAM THAT CHECKS IF A YEAR IS A LEAP YEAR OR NOT(assignment)
# """SOLUTION: A year is said to be a leap year if it is divisible by 4
# and after every 4_4 years(2000,2004,2008,...2100,2200,2300,2400 etc),we fall into a century,
# but every century we skip the count as a leap year,except that year is divisible by 400"""
#
# number_of_years = int(input('enter a year of your choice: '))
# if number_of_years % 100 == 0:  # if this works it has to be divisible by 400,then if the user enters another year
#     # which isn't a century,then it skips and go to else condition
#     if number_of_years % 400 == 0:
#         print('The year {} is a leap year'.format(number_of_years))
#     else:
#         print('The year {} isn\'t a leap year'.format(number_of_years))
# else:
#     if number_of_years % 4 == 0:
#         print('The year {} is a leap year'.format(number_of_years))
#     else:
#         print('The year {} isn\'t a leap year'.format(number_of_years))
# print('programing: \npython \njava \nhtml')
# print(names.strip())
# print('fatihat mohammed said: \'you can make it,a far as you dont give up\'')
# age = str(12)
# print()
# name = 'faatihat'
# level =str(400)
# print('my name is'+' '+name+' '+'i am'+' '+age+' '+'years old.'+' '+'i am in'+' '+level)
# print('my name is {} and ia am {} years old.i am in {} level'.format(name,age,level))
# school_name = input('enter your school name')
# department = input('enter your department')
# print('the name of your school is',school_name,'and your department is',department )
# first_name = input('enter your first name:')
# last_name = input('enter your last name:')
# # full_name = first_name +' '+ last_name
# full_name = f"{first_name} {last_name}"
# print(full_name)
# assignment
# year_born = int(input('please enter your birth year:'))
# current_year = 2022
# difference = current_year - year_born
# print('i am {} years old'.format(difference))
# strings
# list
# names = ['faatihat', 'tomiwa', 'mavel']
# names = '  faatihat mohammed'
# print(names.title())   # first letter capital
# word = 'python programing'
# print(word[0:6])
# print(word[:-1])
# print(word[-10:])
# print(word[7:-3])
# print(word[::-1])
# # from 0 to 7 in terms of 2
# print(word[0:7:2])
# print(word.upper())
# print(word.title())
# print(word.capitalize())
# print(word.find("p"))
# print(word.index('p'))
# print(word.endswith('g'))
# print(word.startswith('f'))
# print(word.split(','))
# print(word.isnumeric())
# print(word.istitle())
# print(word.strip('p'))   #not working for all
# print('p' in word)
# x = 5
# y = 10
# print(x+y)
# print(x-y)
# print(x*y)
# print(x**y)
# print(x/y)
# print(x//y)
# print(x % y)   #even or an odd number
# print(19//2)
# print('my name is'+' '+ names.upper())
# word = 'python programing'
# print(word.isprintable())
# print(word.encode('ascii'))
# x = int(input('enter a number: '))
# y = int(input('enter a number: '))
# if x > 100 and x < 200:
#     print('Huge')
# elif x == 50:
#     print('Medium')
# elif x < 50:
#     print('Small')
# else:
#     print('i dont know')
# if x > 100 or x < 200:
#     print('Huge')
# elif x == 50:
#     print('Medium')
# elif x < 50:
#     print('Small')
# else:
#     print('i dont know')
# write a python program that checks the password length of a user.if the length of the password is less than 6
# characters, it should show password too short if it is reater than 12 characters, it should output password too
# long, if it is between 6 and 12 characters, it should accept it.
# password = input('please enter your password: ')
# if len(password) < 6:
#     print('password too short')
# elif len(password) > 12:
#     print('password too long')
# elif len(password) >6 and len(password) < 12:
#     print('accept it')


# password = input('please enter your password: ')
# if len(password) < 6 or len(password)>12:
#     print('password too short or too long')
# else:
#     print('password is correct')
"""write a python program that converts  kg to pounds . it should first as the user the unit of measurement. then
proceed to convert from kg to pounds """
# value = input('please enter a value:')
# unit = input('please enter a unit:')
# if unit == "kg":
#     answer = int(value) * 2.205
#     print(answer)
# elif unit == 'lbs':
#     answer = int(value)/2.205
#     print(answer)
# else:
#     print('enter a valid input')
# ASSIGNEMENT
# if unit == "kg" or unit == 'Kg' or unit == 'KG':
#     answer = int(value) * 2.205
#     print(answer)
# elif unit == 'lbs' or unit == 'Lbs' or unit == 'LBS' or unit == 'LBs' or unit == "lbS":
#     answer = int(value)/2.205
#     print(answer)
# else:
#     print('enter a valid input')
#
# print('KG'.lower())
#
# #alt
# value = input('please enter a value:')
# unit = str(input('please enter a unit:'))
# if unit == "kg".lower() or unit == 'kg'.upper() or unit == 'kg'.title():
#     answer = int(value) * 2.205
#     print(answer)
# elif unit == "lbs".lower() or unit == 'lbs'.upper() or unit == 'lbs'.title():
#     answer = int(value)/2.205
#     print(answer)
# else:
#     print('enter a valid input')
# loop
# cities = ['cairo','kaduna','ilorin','offa']
# citty_box =[]
# for city in cities:
#     citty_box.append(city.title())
#     print(citty_box)
#
# i = 1
# while i < 10:
#     name = input('please enter a name:')
#     print(name)
#     if name == 'END'.casefold():
#         print('i am done')
#         break
#     else:
#         print('Try another name')


# i = 1
# while i < 10:
#     number = int(input('please enter a number'))
#     if number < 0:
#         # sum= sum(number)
#         print('correct')
#         break

# for loop
# for loop is used to iterate through a sequence o characters or a collection of itemsmor range of numbers etc.
# loop through a string
# text = 'python programing'
# for i in text:
#     if i == " ":
#         break
#     print(i)
# loop through a sequence of number
# for i in range(11):
#     print(i)
# pass statement = null operator, does nothing
#
from win32com.client.gencache import __init__

for i in range(9):
    pass
# the 'in' key word checks for the existence of an item in a variable OR 'not in'
# #exercise FIZZ_BUZZ challenge
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('fizz-buzz')
#     elif i % 5 == 0:
#         print('buzz')
#     elif i % 3 == 0:
#         print('fizz')
#     else:
#         print(i)
#
# for i in range(1, 101):
#     if i  in range(1,10):
#         print('not in range')
#         if i % 3 == 0 and i % 5 == 0:
#             print('fizz-buzz')
#         elif i % 5 == 0:
#             print('buzz')
#         elif i % 3 == 0:
#             print('fizz')
#             if i not in range(1,10):
#                 print('not in range')
#             else:
#                 print(i)

# print('not in range') a user should enter a number if that nuber enter by the  is within the range given,
# return ou of range, other wise return fizz mul3, f numbe given is
# for i in range(1, 101):
#     number = int(input('enter a number within the range:'))
#     if number in range(1, 21):
#         if number % 3 == 0 and number % 5 == 0:
#             print('fizz-buzz')
#         elif number % 5 == 0:
#             print('buzz')
#         elif number % 3 == 0:
#             print('fizz')
#         elif number % 3 != 0 or number % 5 != 0:
#             print(i)
#     else:
#         if number not in range(1, 21):
#             print('out of range.'.upper())
#             break
# #assignment 2 sha
# name = input('enter your last name and your first name:')
# lst = name.split()
# last_name = lst[0]
# first_name = lst[1]
# print(last_name[0].upper()+"."+first_name[0].upper())
""" FUNCTIONS :  is a way to structure, maintain and avoid repetitions of code (DRY- Dn repeat your self) it also keep
your code neater. types include : built-in functions and user defined / custom functions
user defined: use the def key word  followed by the name of the function and then (). 
()-this may be empty or contain variables known as parameters
the body of a function
a function would nt get executed unless a call is made to that function"""
# a  function that would print hello word
# def greetings():
# # this is called declaring
#     print('hello world')

# greetings()  # function call, to call a function u must leave
# return statement,
# def sum_num():
#     return 3+3
# print(sum_num())
# parameters and arguments
"""parameters are variable declared in a function definition,, they act as placeholders to the actual value to be 
passed into the function, arguments == actual value passed into  a function when a call is made to that function
        TYPES OF ARGUMENT
POSITIONAL ARGUMENTS ARE WHEN YOUR ARGUMENTS ARE PLACED BASED ON YOUr parameters
KEYWORD ARGUMENTS OR KWARGS is when you have the parameter name followed by value.
  """
# def sum_num(x,y):
#     return x + y
# sum_num(2 ,3)
# print(sum_num(2 ,3))
#
#
# def minus(a,b):
#     return a - b
#
# print(sum_num(6,6))
# print(minus(6,2))
# def full_name(firstname,lastname):
#     return firstname+' '+lastname
# print(full_name('faatihat','mohammed'))
#
# def full_name():
#     fname = input('enter your first name:')
#     lname = input('enter your last name:')
#     return fname+' '+ lname
# print(full_name())
#
# # def showEmployee():
# #     salary = int(input('enter your salary '))
# #     if salary < 50000:
# #         return 'level = low'
# #     elif salary > 50000:
# #         return 'level = high'
# #     else:
# #         return 'Not a valid salary'
# # print(showEmployee())
#
# def showEmployee(salary):
#     if salary < 50000:
#         return 'level = low'
#     elif salary > 50000:
#         return 'level = high'
#     else:
#         return 'Not a valid salary'
#
# print(showEmployee(int(input('enter your salary '))))
#
# """CORRECTION"""
# def showEmployee(salary):
#     level = ''
#     if salary < 50000:
#         level = 'low'
#     elif salary > 50000:
#         level = 'high'
#     else:
#         level='Not a valid salary'
#     return level
# print(showEmployee(int(input('enter your salary'))))
# positional argument
# def full_name(fname,lname):
#     return fname+' '+lname
#
# print(full_name('faatihat','mohammed'))

# def full_name(fname,lname):
#     return fname+' '+lname
# fname=input('first name')
# lname=input('last name')
#
# print(full_name(fname,lname))
# def user_range():
#     first_number = int(input('enter first number'))
#     last_number = int(input('enter last number'))
#     number = int(input('enter a number '))
#     answer = ''
#     if number in range(first_number,last_number):
#         answer = 'in range'
#     else:
#         answer = 'not in range'
#     return answer
# print(user_range())
# funny class work that checks iif an input entered by a user has u.case and lower..cas
# def case_checker():
#     name = input('enter any sentence,ensure it has both Caps and sletter:\n')
#     No_of_upper = 0
#     No_of_lower = 0
#     for letter in name:
#         if letter.isupper():
#             No_of_upper +=1
#         elif letter.islower():
#             No_of_lower+= 1
#     return 'The total number of uppercase is {} and total number of lower case is {}'.format(No_of_upper,No_of_lower)
#
# print(case_checker())
#
# def check_range():
#     range_num = range(int(input('enter a range:')))
#     number = int(input('enter a number'))
#     text = ""
#     if number in range_num:
#         text = 'in range'
#     else:
#         text = 'not in range'
#     return text
# print(check_range())
"""PASSING FUNCTIONS AS ARGUMENT
Higher order function: is a function that takes in another function as an argument or as a return value"""
# create a su function and difference function
# def sum(x,y):
#     return x+y
#
# def minus(a,b):
#     return a-b
#
# print(sum(5,5))
# print(minus(b=10,a=20))
#
# def higher_order(func,z,p):
#     return func(z,p)
# print(higher_order(sum,2,2 ))

"""lambda functions or xpression : this is a simple anonymous fxn 
it can take any number of arguments but can only have a single expression
 the strengty of lambda fxn can be seen when used with higher order fxn"""

# lambda function
# lambda function is a simple anonymous function

# it can have any number of argument but can only have a single expression

# you can use it to execute very simple and concise functions
# def double(x):
#     return x * 2

# numbers = [
#                 [34,63,88,71,29],
#                 [90,78,51,27,45],
#                 [63,37,85,46,22],
#                 [51,22,34,11,18]
#             ]
# # def mean(num_list):
# #     return sum(num_list)/ len(num_list)
# #
# # averages = list(map(mean,numbers))
# # print(averages)
#
# mean = list(map(lambda x: sum(x)/len(x),numbers))
# print(mean)
# write a function that will return the sum of two numbers
# result = lambda x, y: x + y
# print(result(10, 10))
#
#
# def sum_result(result):
#     return


"""# nested function: having one function inside another func"""
# def outer_func():
#     def inner_func():
#         print('hello')
#     return inner_func
#
# func = outer_func()
# func()


"""decorators --- it is a branch of metaprogramming.it allows you to wrap your function in another function
it act as a wrapper for your original function"""

# def outer_func(func):
#     def inner_func():
#         print('i am a decorator')
#     return inner_func
# # @outer_func
# def ordinary():
#     print('i am ordinary')
# # outer_func('jh')
# # ordinary = outer_func(ordinary)
# ordinary()
#
# # # #ytube
# def say_hello(func):
#     def wrapper(*args, **kwargs):
#         print('hello')
#         return func(*args, **kwargs)
#     return wrapper
#
# @say_hello
# def summ(x, y):
#     return x + y
# print(summ(2,4))
# summ
# @say_hello
# def minus(p, o):
#     return p + o
# print(minus(5, 1))

# def decorator_function(original_fun):
#     def wrapper_func():
#         print("wrapper executed this before {}".format(original_fun.__name__))
#         return original_fun
#     return wrapper_func()
# @decorator_function
# def display_fun():
#     print('display function worked')
# decorated_func = decorator_function(display_fun)
# decorated_func()
# display_fun()
"""GENERATORS"""
"""list"""
# list3 = list((1,2,3,4))
# print(list3)
# d = 3 in list3
# print(d)
# f = 3 not in list3
# print(f)
# list3.append([5,6,7,8])
# print(list3)
# list3.extend([1,2,3,4,5])
# print(list3)
# #assignment
# list_1 = [1, 2, 3, 4, 5, 6,7,8,9,10]
# list_1.extend([11,12,13,14])
# print(list_1)
# list_1.clear()
# print(list_1)
# list_1.insert(12,0)#why do we have to insert 2 arguments
# print(list_1)
# list_1.reverse()
# print(list_1)
# list_1.sort()
# print(list_1)
# list_1.remove(7)
# print(list_1)
# list_1 = [1, 2, 3, 4, 5, 6,7,8,9,10]
# for i in list_1:
#     if i == 2:
#         continue
#     elif i == 7:
#         break
#     print(i)

# #concatenate 2 list
# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]
# # add = list1 + list2
# # print(add)
# for i in list2:
#     list1.append(i)
# print(list1)
#
#
# list_of_list = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in list_of_list:
#     sum = sum + i
# print('the sum of my list is {}'.format(sum))


# # average.
# list_of_list2= [1,2,3,4,5,6,7,8,9,10]
# summ = 0
# for i in list_of_list2:
#     summ = summ + i
#     average = summ / len(list_of_list2)
# print(average)
#
# list_of_list = [1,2,3,4,5,6,7,8,9,10]
# prod = 1
# for i in list_of_list:
#     prod = prod * i
# print('the prod of my list is {}'.format(prod))

# list_of_list = [6,3,5,20,7,8,2]
# max_num = list_of_list[0]
# for i in list_of_list:
#     if i > max_num:
#         max_num = i
# print(max_num)

"""list comprehension: create a loop with for loop with one step, you dont need to cuse aappend method"""
# cities = ['abuja', 'ilorin','sango','tech']
# capitalized_cities = [city.title() for city in cities]
# print(capitalized_cities)

# squares = [x**2 for x in range(9) if x % 2 == 0]
# print(squares)
# square = [x**2 if x % 2 == 0 else x+3 for x in range(9)]
# print(square)

# names = ['faatihat tom','mohammed','tomiwa','abdul','fadil','fathil']
# # cap_names = [name.upper() for name in names]
# # print(cap_names)
# names = ['faatihat tom','mohammed ghhhhgf','tomiwa ghhhhgf','abdul ghhhhgf','fadil ghhhhgf','fathil ghhhhgf']
# first_names = [name.split()[0].upper() for name in names]
# second_name = [name.split()[1].upper() for name in names]
# print(first_names)
# print(second_name)
#
# scores = {
#             'faatihat mohammed': 70,
#             'tomiwa mohammed':35,
#             'faith ugu': 82,
#             'jerry smith': 23,
#             'beth smith': 98
# }
# passed = [name for name, score in scores.items() if score >= 65]
# passs = [name for name, score in scores.items() ]
# print(passed)
# print(passs)
# passeds = [score for name, score in scores.items() if score >= 65]
# print(passeds)
# # use this or list comprehension
# list = []
# for i in range(1,21):
#     var = i * 3
#     list.append(var)
# print(list)
#
# multiple_3 = [x*3 for x in range(1,21)]
# print(multiple_3)

# write a program that keeps asking a user to enter a number till u enter a negtive number, at the end print the sum
# of all numbers
# number =
# list_number = []
# while number  > 0:
# TUPLE: this is a data structure,it is ordered and allows duplicate values. it cannit be modified like a list
# it is represented by round brackets . it can be homogeneous or heterogeneous
# items = (1,2,3,4)
# items_2 = (1,'we',True,2)
# # you can create using tuple constructor
# items_3 = tuple((1,'we',True,2))
# print(items_3)
# length = len(items_3)
# print(length)
# if 1 in items_3:
#     print('yes')
# v = items_3[0]
# print(v)
# f = items_3[:]
# print(f)
# unpacking
# this involves assigning tuple to variables. you store items to more than one variable
# x,y,z =('first','second','third')
# print(x) #first
# print(y)
# there would be a situation when a tuple would have many items to unpack
# x,y,z =('first','second','third','fourth')
# we can instead unpack some items as list
# x,y,*z =('first','second','third','fourth')
# print(z)
# some tuple use cases
# can be used as tag or categories
# tags = (
#     ('outdoor','indoors')
# )
# outdoor = ['x','y','z']
# outdoor = ['a','b','c']
# multi dimensional tuple: tuple within a tuple
# multi_tuples = (('first','second','third','fourth'),('outdoor','indoors'))
# print(multi_tuples[0])
# print(multi_tuples[0][0])
# print(multi_tuples[0][1])
# change = list((multi_tuples))
# print(change)
# change.append('flirt')
# print(change)
# print(tuple((change)))
# #dictionaries: it stores items in key value pairs denoted by curly braces. it does not allow duplicate value
# #it is similar to JSON(java script object notation ) .
# #create a dictionary
my_profile = {
    'name': 'faatihat',
    'age': 24,
    'city': 'ilorin'
}
# assignment, length of dict
# print(len(my_profile))
# print(my_profile)
# #you can access the value using bracket notation
# print(my_profile['name'])
# print(my_profile['age'])
# #looping
# for i in my_profile:
#     print(my_profile[i])
# print(my_profile.get('name'))
#
# #keys
# print(my_profile.keys())
# print(my_profile.values())
# print(my_profile.items())  #return the keys and value in tuple format
# print(my_profile.popitem())  #removes the last one
# # print(my_profile.pop())
# print(my_profile)
# my_profile_1 = {
#     'new_name' : 'hayat',
#     'new_age': 20,
#     'her': 'tomiwa'
#
# }
# my_profile.update(my_profile_1)
# v = my_profile.copy()
# print(v)
# print(my_profile)
# key = my_profile.keys()
# value = my_profile.values()
# for keys,values in zip(key,value):
#     print(keys,"\t",values)
# #nested dict: u can use it to store information about your student
# students = {
#     1:{'name':'faatihat',
#        'email':'fatihat@yahoo.com',
#        'password':'temitope'
#        },
#     2:{'name':'hayat',
#        'email':'hayat@yahoo.com',
#        'password':'faatihat'
#        },
#     4:{'name':'papa',
#        'email':'papa@yahoo.com',
#        'password':12345
#        }
# }
# print(students)
# print(students[1])
# print(students[2])
# print(students[4])
# keys = students[4].keys()
# values = students[4].values()
# # for key,value in zip(keys,values):
# #     print(key,value,"\n")
#
#
# for i in students[4]:
#     print(students[4][i]) ## getting the keys
# print('TESTING SOMETHING ELSE')
# print(students[4]['password'])
# print('TESTING SOMETHING ELSE')
# for i in students[4]:
#     print(students[4][i])
# print('printing just the password for dict 4')
# print(students[4]['password'])
# write a python script to print a dict where the keys are nubers between 1 and 15 and the values ar square of the kesy

# dic_numbers = {}
# k = dic_numbers.keys()
# v = dic_numbers.values()
# for i in range(1,16):
#     k, v = i, i**2
#     d = {k:v}
#     dict(d)
#     print(d)

dic_numbers = {}
k = dic_numbers.keys()
v = dic_numbers.values()
for i in range(1, 16):
    k, v = i, i ** 2
    dic_numbers.update({k: v})
print(dic_numbers)

# modules and packages
# the main thing is to brake down the code into different part, when you use the * you import everything in the module
# 3ass, code module ,  unittest
# python built_in modules: a way to organise and structure your codes
# packages == collection of modules, same as libraries
import math

print(math.pi)
print(math.ceil(4.5))  # rounds up automatically
print(math.floor(233.5))  # takes the number before the point
print(math.pow(2, 3))  # power of  a number, this is 2 raised to the power of 3
print(math.log10(100))
print(math.factorial(6))
import random

random.random()
import datetime

# the year born ,return its age after 3 years and the return the time
current_year = 2022
# your_age = int(input('enter your year:'))
# if current_year:
#     age = current_year-your_age
#     age_after_3years =age + 3
#     print(age_after_3years)
#     print(datetime.datetime(int(input('enter full'))))

from newww.calc import *

"#importing from another package"
print(gross(12, 12))

