# age = int(input('please enter your age:'))
# if age >= 18:
#     print('youre eligable')
# else:
#     print('please try again later')
#program to check whether the numbr enter by user is even or odd
# number = int(input('please enter a number:'))
# if number % 2 == 0:
#     print('the number is even')
# else:
#     print('the number is odd')
# def full_name(fname = input('enter your first name:'),lname = input('enter your last name:')):
#     return fname+' '+ lname
# print(full_name())

#check if a number is divisible by 7 or not
# num = int(input('please enter a number'))
# if num % 7 == 0:
#     print('it is divisible by 7')
# else:
# #     print('pick another number')
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
#write a program that diplays hello if a number is a multiple of 5
# num = int(input('please input a number'))
# if num % 5 == 0:
#     print('hello')
# else:
#     print('bye')
# to display the last digit of a number
# num = int(input('please input a number'))
# print( 'the last digit of a number is',num%10)
# num = int(input('please input a number:'))
# last_digit = num % 10
# if last_digit % 3 == 0:
#     print('YES last digit is divisible by 3')
# else:
#     print('last digit isnt divisible by 3')
# grade = int(input('please enter your grade:'))
# if grade > 90 :
#     print('A')
# elif grade > 80 and grade <= 90:
#     print('B')
# elif grade >= 60 and grade <=80:
#     print('C')
# elif grade < 60:
#     print('D')
# else:
#     print('please enter a valid number')
# num = input('please enter any number of your choice:')
# len_num = len(num)
# if len_num == 3:
#     print('you can proceed')
# else:
#     print('enter a valid number')
# prigram that asl user fpr salary and year if greater than 5 ro give bonus
# def salary_worker():
#     year = int(input('please enter your year of service:'))
#     if year >= 5:
#         salary = int(input('enter your salary:'))
#         print('Net bonus is',(0.05)*(salary))
#     else:
#         print('you cant apply for this yet')
#
# salary_worker()

# take values of ength and breath from user and check if it is a square or not
# length = int(input('please enter a  valid length:'))
# breadth = int(input('please enter a  valid breadth:'))
# if length == breadth:
#     print('it is a square')
# else:
#     print('it is a rectangle')
# to print greater nu,bers between given number
# num1 = int(input('please enter a  valid numb'))
# num2 = int(input('please enter a  valid numb:'))
# if num1> num2:
#     print('num1 is greater')
# elif num2 > num1:
#     print('num2 is greater')
# else:
# #     print('they are equal')
# i = 0
# while i <3:
#     number = 5
#     guess = int(input('guess a number:'))
#     if number == guess:
#         print('CONGRATULATIONS YOU WiN')
#         break
#     if i == 2:
#         print('sorry you lose')
#         break
#     else:
#         print('please try another number')
#         i+=1
#
# i = 0
# while i <3:
#     number = 5
#     guess = int(input('guess a number:'))
#     if number == guess:
#         print('CONGRATULATIONS YOU WiN')
#         break
#     # if i == 2:
#     #     print('sorry you lose')
#     #     break
#     else:
#         print('please try another number')
#         i+=1
# else:
#     print('you lose')
# i= 0
# while i < 21:
#     print(i)
#     i+=2

# i = 0
# print('numbers \tsquare')
# while i <11:
#     print(i,'\t\t\t',i**2)
#     # print(i**2)
#     i+=1
# i = 0
# while i <= 300:
#     print(i)
#     i+=10

#sum of 10 natural number
# i = 0
# while i < 10:
# num_sum = []
# num = int(input('enter a number:'))
# num_sum.append(num)
# while num_sum  >= 0:
#     num = int(input('enter a number:'))
#     if num < 0:
#         print(sum(num_sum))
#         break
#     num_sum.append(num)
# SUM OF FIRST 10 NATURAL NUMBER
# sum = 0
# i = 1
# while i <= 10:
#     sum = sum + i
#     i+=1
# print(sum)
#  A PROGRAM THAT CHECKS IF A YEAR IS A LEAP YEAR OR NOT
"""SOLUTION: A year is said to be a leap year if it is divisible by 4
and after every 4_4 years(2000,2004,2008,...2100,2200,2300,2400 etc),we fall into a century,
but every century we skip the count as a leap year,except that year is divisible by 400"""
# i = 1
# while i < 10:
#     number_of_years = int(input('enter a year of your choice: '))
#     if number_of_years % 100 == 0:  # if this works it has to be divisible by 400,then if the user enters another year
#     # which isn't a century,then it skips and go to else condition
#         if number_of_years % 400 == 0:
#             print('The year is a leap year')
#             break
#         else:
#             print('The year isn\'t a leap year')
#         continue
#     else:
#         if number_of_years % 4 == 0:
#             print('The year is a leap year')
#             break
#         else:
#             print('The year isn\'t a leap year')
# else:
#     print('try again')
#
#
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('fizz-buzz')
#     elif i % 5 == 0:
#         print('buzz')
#     elif i % 3 == 0:
#         print('fizz')
#     else:
#         print(i)
# x = -1
# print(abs(x))
#while loop
#
# numbers = 12345
# store = []
# if numbers % 10 != 0:
#     for i in range(5):
#         one = numbers % 10
#         new = numbers - one
#         store = new // 10
#         print(store)
#sum of 10 natural numbers
# i =1
# sum = 0
# while i <= 10:
#     sum = sum + i
#     i+=1
# print(sum) # it will do this when while is false
# #sum of first 10 even numbers
# i =2
# sum = 0
# while i <= 20:
#     sum = sum + i
#     i+=2
# print(sum)
#
# i =2
# sum = 0
# while i <= 20:
#     if i % 2 == 0:
#         sum = sum + i
#     i+=1
# print(sum)
# a user enters a number and it prints out a  the table
# number = int(input('enter a number of your choice:'))
# i = 1
# while i <= 10:
#     product = number * i
#     print('5 * {}={}'.format(i,product))
#     i+=1
# i = 2
# summ = 0
# while i <= 20:
#     summ = summ + i
#     i += 2
# print(summ)
#
# num = 2
# while num <= 20:
#     print(num)
#     num += 2

# def nameoffunction():
#     return 'this is a function'
#
# print(nameoffunction())
#
# def nameoffunction():
#     print('this is a function')
#
# nameoffunction()
# def user_info(name,age,cuntry):
#     return 'my name is {}. i am {} years old and i live in {} '.format(name,age,cuntry)
#
# print(user_info(input('enter your name'),input('age'),input('country')))

# def user_info():
#     user_name = input('enter your name')
#     user_age = input('enter your age')
#     user_country = input('enter your name')
#     return 'my name is {}. i am {} years old and i live in {} '.format(user_name,user_age,user_country)

# print(user_info())

# def user_info(name,age,cuntry):
#     user_name = input('enter your name')
#     user_age = input('enter your age')
#     user_country = input('enter your name')
#     return 'my name is {}. i am {} years old and i live in {} '.format(name,age,cuntry)
#
# print(user_info(input('enter your name'),input('age'),input('country')))

# SUM = 0
# for i in range(3):
#     num=int(input('enter number'))
#     SUM = SUM + num
# print(SUM)
#
# SUM = 0
# i=0
# while i < 3:
#     num=int(input('enter number'))
#     SUM = SUM + num
#     i+=1
# print(SUM)


"""questions on while loop"""
#first 10 even numbers
# i = 2
# summ = 0
# while i <= 20:
#     summ = summ + i
#     i+=2
# print(summ)
#
# #firs 10 odd numbers
# i = 1
# summ = 0
# while i <= 20:
#     # print(i)
#     summ = summ + i
#     i+=2
# print(summ)
#
# #first 10 natural numbers
# i = 0
# sum = 0
# while i <=10:
#     sum = sum + i
#     i+=1
# print(sum)
#
# #first 10 integers and their squares
# i = 0
# while i <=10:
#     i+=1
#     print('NUMBER \t SQUARE')
#     print('{} \t\t {}'.format(i,i**2))
#     # print('the number is {} and the square is {}'.format(i,i**2))
# #  loop that prints numbers like 1,2,3,4,5...
# i = 0
# while i <=300:
#     # print(i,end="_")
#     i+=10
# #print 105,98,91...7
# i = 112
# while i >=7:
#     print(i,end=",")
#     i-=7
#first 10 natural number in reverse order
# i = 1
# while i >= 1:
#     print(i)
#     i= i-1
# #sum of first 10 natural number
# i = 10
# sum = 0
# while i >= 1:
#     sum = sum + i
#     i= i-1
# print(sum)
# # print table of the number entered by a user
# i = 0
# number = int(input('enter a number:'))
# while i<= 10:
#     i+=1
#     product = number * i
#     print('{} * {} = {}'.format(number,i,product))
# #sum of he number entered by the user
# i = 0
# sum = 0
# while i <= 10:
#     numb = int(input('enter a number'))
#     sum = sum + numb
#     i+=1
# print(sum)
# sum of numbers entered by a user once eg 1234
# num1 = int(input('enter any number:'))
# r = 0
# s = 0
# while num1 !=0:
#     r = num1 % 10
#     s = s+r
#     num1 = num1 // 10
# print('sum of the digits are: ',s)
"""product of sequence of numbers"""
# user_number = [2, 4, 6]
# e_number = 1
# for each_number in user_number:
#     e_number = e_number * each_number
# print(e_number)
#
# i = 2
# product_no = 1
# while i<=6:
#     product_no = product_no * i
#     i+=2
# print(product_no)
"""sum of digits entered ny a user once"""
# user_number = int(input('enter numbers of your choice:'))
# lnum = 0
# sum_num = 0
# while user_number!=0:
#     lnum = user_number % 10
#     sum_num = sum_num + lnum
#     user_number = user_number // 10
# print('The total number equals',sum_num)

"""product of the digits of a number accepted from a user"""
# user_number = int(input('enter numbers of your choice:'))
# lnum = 1
# prod_num = 1
# while user_number > 0:
#     lnum = user_number % 10
#     prod_num = prod_num * lnum
#     user_number = user_number // 10
# print('The product of the numbers entered is',prod_num)
"""reverse number entered by a user"""
# user_number = int(input('enter numbers of your choice:'))
# r = 0
# reverse_num = 0
# while user_number !=0:
#     r = user_number % 10
#     reverse_num = reverse_num * 10+r
#     user_number = user_number // 10
# print(reverse_num)



def get_user(names):
    for name in names:
        print('hello',name)
usernames = ['hanna','nifa','faatiha']
get_user(usernames)

def get_user(*names):
    for name in names:
        print('hello',name)
# usernames = ['hanna','nifa','faatiha']
get_user('hanna','niffa','pita')
#
# number = 6
# current = 1
# product = 1
# while current < 6:
#     current+=1
#     product = product * current
# print(product)

# number = int(input('enter any number to get the factorial:'))
# current = 1
# product = 1
# while current < number:
#     current+=1
#     product = product * current
# print(product)

# number = int(input('enter any number to get the factorial:'))
# current = 1
# product = 1
# for current in range(1,number+1):
#     product = product * current
# print(product)
# 3fizbuzz game
# def fizz_buzz():
#     user_number = int(input('enter any number:'))
#     output = ""
#     if (user_number % 3 == 0) and (user_number % 5 == 0):
#         output = 'fizz_buzz'
#     elif user_number % 3 == 0:
#         output = 'fizz'
#     elif user_number % 5 == 0:
#         output = 'buzz'
#     else:
#         output = user_number
#     return output
#
# print(fizz_buzz())
# cities = ['abuja', 'ilorin','sango','tech']
# capitalized_cities = [city.title() for city in cities]
# print(capitalized_cities)
#
#
names = ['faatihat tom','mohammed ghhhhgf','tomiwa ghhhhgf','abdul ghhhhgf','fadil ghhhhgf','fathil ghhhhgf']
second_name = []
for name in names:
    # second_name.append(name.split())
    second_name.append(name.split()[1])
print(second_name)
"""to get the biggest """
# list = [1,2,3,4,5,6,7]
# for i in list:
#     max_numb = 0
#     min_numb = list[0]
#     if i > min_numb:
#         max_numb = max_numb + i
# print(max_numb)

"""to get the smallest numb"""
# list = [2,4,6,7,8,1]
# for i in list:
#     min_num = 0
#     max_num = list[0]
#     if i < max_num:
#         min_num = min_num + i
# print(min_num)

# """reverse the word entered by a user"""
# word = 'tell'
# for i in range(len(word)-1,-1,-1 ):
#     print(word[i])
#     #OR
# word = 'tell'
# for i in word:
#     n = word[::-1]
# print(n)
#
# lst = [1,2,3,4,5,6,7,8,9,10]
# print(lst[::2])
# print(lst[::-1])
#
# # word = 'i am python'
# # v = word[::-1]
# # print(v)
# word = input("enter a word:")
# n = word[::-1]
# print(n)

# for i in range(len(word)):
#
#     print(word[i])
# """FUNCTIONS"""
# def population_density(population,land_area):
#     return population / land_area
# test1 = population_density(10,1)
# expected_result1 = 10
# print('expected result : {},actual result {}.'.format(expected_result1,test1))
#
# def readable_timedelta(days):
#     week = days // 7
#     day = days % 7
#     return "{} weeks and {} days".format(week,day)
#
# print(readable_timedelta(10))
# def print_fn():
#     str1 = 'vaiable scope is an important concept'
#     print(str1)
#
# print_fn()
# #
# #
# numbers = [
#     [34,63,88,71,29],
#     [90,78,51,27,45],
#     [63,37,85,46,22],
#     [51,22,34,11,18]
# ]
# def mean(num_list):
#     return sum(num_list)/ len(num_list)
#
# averages = list(map(mean,numbers))
# print(averages)
from newww import helloworld

addd = helloworld.sum(2, 5)
print(addd)

from newww.helloworld import *
print(minus(5,2))


# import helloworld as hw
# print(hw.minus(5,1))
# for i in range(1,100):
#     word = input('enter a word:')
#     rev = word[::-1]
#     if word == rev :
#         print('palindrome')
#     else:
#         print('not palindrome')

# for i in range(1,100):
    # def palindrome(word):
    #     rev = word[::-1]
    #     result = ""
    #     if word == rev :
    #         result = "palindrome"
    #     else:
    #         result = "not palindrome"
    #     return result
    #
    #
    # print(palindrome(input('enter a word of your choice:')))


    
# from newww.helloworld import *
# print(minus(5,2))
#
# #file handling
# f = open('sample.txt', 'r')
# # print(f.read())
# # print(f.readline(3))
# # print(f.readlines())
# f.close()
#
# f = open('sample.txt', 'r')
# for words in f:
#     print(f.read())
# f.close()
#
# f = open('sample.txt', 'a')
# f.write("\nshe is now in university of ilorin")
# print(f.read())
# f.close()

# t = open('create_sample.txt','w')
# t.write("i just tried creating a file without opening")
# print(t.read())
# t.close()
# import os
# c = open("create.txt",'x')
# c.write("creating new file with 'x' method ")
# c.close()

import json

a = {
    "name": "max",
    "age": 22,
    "marks": [90,10,12],
    "pass": True

}

#to convert dict to json
print(json.dumps(a))
print(json.decoder)