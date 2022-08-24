# zip and enumerate
# items = ['banana','apple','mango']
# weights = [15,12,2]
# print(list(zip(items,weights)))
# print(zip(items,weights))
"""this wont work but the first would join the two
ZIP : it returns an iterator tha combines multiple iterable into one sequence of tuples. 
we can also use for loop .
you can also unzip a list using the asterisk sign"""
# for cargo in zip(items,weight):
#     print(cargo[0],cargo[1])
# for item,weight in zip(items,weights):
#     print(item,weight)
# manifest = [('banana', 15), ('apple', 12), ('mango', 2)]
# items,weight = zip(*manifest)
# print(items,weight)
# to get output of list with index
# items= ['banana','apple','mango']
# for i,item in zip(range(len(items)),items):
#     print(i,item)
#
# #scripts: a script is just a python code. we save it to a file and it will have .py at the end
# name = input('enter names separated by comma:').split(",")
# assignment = input('number of missing assignment separated by comma:').title().split(",")
# grades = input('enter current grades separated by comma:').split(",")
# message = 'hi {}, \n\n This is a reminder that you have {} assignments left to submit before you can graduate.\nYour\
#           'current grade is {} and can be increased to {} if you submit all assignments before the due date.\n\n'
# for nam,ass,grad in zip(name,assignment,grades):
#         p_grade = int(grad) + int(ass)*10
#         print(message.format(nam,ass,grad,p_grade))
# errors
import math
import statistics

"""we have syntax error and exception errors
syntax error: occur  when python cant understand our code,since we didnt follow the correct syntax
exception error: occurs when unexpected things happen during the execution of the code, eg, if u enter string for int,
you will get an exception error
types of exception error:
value error,name error:when u try to access a variable name u did not define from the beginning"""
# reading and writing files
# f = open('\Users\ tomfa\IdeaProjects\hellowroeld\udacity_script,py.py')
# import:i can acces femtech class code here using this
import femtechClass
import femtechClass as rf

# print(rf.multi_tuples)
# module is a file with python definition and statements
# you can import in different manners,use the main module name or an abbreviation
import math as mt

print(mt.log10(1000))
# or this any how you like
print(math.log10(1000))
print(mt.e)
expo = math.e
print(expo)
print(mt.pow(expo, 3))
# from random import * , this makes you access all object in a modules , it is not too good.
# instead use import random instead
print(pow(expo, 3))
print(math.exp(3))

import random

word_file = "sample.txt"
word_list = []
with open(word_file, "r") as words:
    for line in words:
        word = line.strip().lower()
        if 3 < len(word) < 8:
            word_list.append(word)
            AWprint(word_list)

# def generate_password():
    # return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)



