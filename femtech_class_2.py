import png
import pyqrcode
# file handling(CRUD: Create, read, update, delete)
"""open function, it takes the file name and the modes(is always on read, ) ,that is READ,APPEND,CREATE.."""
# to READ
f = open("venv/script.txt", "r")
"use that when it isnt in the same directory but if its in the same , like in hellowreeld , you just call like," \
"f = open(script.txt, "r")"
# print(f.read())
# print(f.readline())  # first line
# print(f.read(7))  #first 5 characters
f.close()

# To Append
# f = open("venv/script.txt", "a")
# f.write('\nshe is a naughty girl')
# f.close()

# f = open("venv/script.txt", "r")
# print(f.read())
# f.close()

# f = open("venv/script.txt", "r")
# for i in f:
#     print(i)
# f.close()

# TO WRITE
# f = open("venv/script.txt", "w")
# f.write('\nshe is a naughty girl')
# f.close()

#to create, you cannot create two files of the same name
# c = open("create.txt",'x')
# c.write("creating new file with 'x' method ")
# c.close()


import os

# TO REMOVE , You need to import a module
#to check if it actually exist
if os.path.exists("create_sample.txt"):
    os.remove("create_sample.txt")  # removing directory , to remove a file
else:
    print("file does not exist")
#to delete
if os.path.exists("script.txt"):
    os.rmdir("thanks")  # removing directory , to remove a file
else:
    print("file does not exist")
# f = open("venv/script.txt", "a")
# f.write('\nshe is a naughty girl')
# f.close()
#
# f = open("venv/script.txt", "r")
# print(f.read())
# f.close()
g = open("sample.txt", "w")
g.write("faatihat")
g.close()

g = open("sample.txt", "r")
g.close()


# oop: object oriented programming: a programming paradigm that uses objects and classes in programing
# it helps to implement real word entities ,like inheritance, polymorphism,obstruction, encapsulation
# class: a blueprint or a templet for building objects in python
# bp is class and the house is the object
# instance :is an object that belongs to a class. the process of creating an instance is called instantiation.
# attributes or properties are variables that belong to an obj
# methds are those functions that are specific to an obj

# class - ball
# we have objects like plastic and leather ball
# the plastic can have attributes weight, color ,material and leather ball can also have attributes color and the likes
# the throwing and catching are like methods for each instances

class Ball:
    # the init is called the constructor it is also referred to as magic method, becasuse it runs behind scene. it
    # must take in at least one parameter called /self(plastic ball in this case)/ it references the obj being created
    def __init__(self):
        self.color = "red"
        self.weight = 2.1
        self.material = "plastic"


plastic_ball = Ball()
leather_ball = Ball()

print(plastic_ball.color)
print(leather_ball.color)


# print(plastic_ball)
# print(leather_ball)
# plastic_ball.weight = 2.1
# plastic_ball.color = "red"
# plastic_ball.material = "plastic"
# print(plastic_ball.weight)
# print(plastic_ball.material)
# print(plastic_ball.color)
# print(leather_ball.weight)


class Person:
    def __init__(self, name, age, location):  # param
        self.name = name
        self.age = age  # attributtes
        self.location = location


person_1 = Person("faatihat", 25, "ilorin")  # these ones are arguments
person_2 = Person("tomiwa", 25, "ibadan")

print(person_1.age)
print(person_2.age)
print(person_2.location)
print(person_2.name)
print(person_1.name)
person_2 = Person(name="tomiwa", age=25, location="ibadan")  # remember this is called kwrgs
person_1 = Person(name="faatihat", age=25, location="ilorin")


# design a python checkout system for a bookstore, use appopriate attributes to depict your bookstore

# class Book_store:
#     def __init__(self, entry_time, exist_time, price_of_books_bought):
#         self.entry_time = entry_time
#         self.exist_time = exist_time
#         self.price_of_books_bought = price_of_books_bought
#
# persn_1 = Book_store(input("enter your entry time:"), input('enter your exist time:'), input("enter total price "))
# persn_2 = Book_store(input("enter your entry time:"), input('enter your exist time:'), input("enter total price "))
# persn_3 = Book_store(input("enter your entry time:"), input('enter your exist time:'), input("enter total price "))
#
# print(persn_1.entry_time, persn_1.exist_time,persn_1.price_of_books_bought)
# print(persn_2.entry_time, persn_2.exist_time,persn_2.price_of_books_bought)
# print(persn_3.entry_time, persn_3.exist_time,persn_3.price_of_books_bought)



#correction
# class Book_store:
#     def __init__(self, book_title, book_author, book_price):
#         self.book_title = book_title
#         self.book_author = book_author
#         self.book_price = book_price
#
# book_1 = Book_store(book_title="harry porter", book_author="jk",book_price=100)
# book_2 = Book_store(book_title="harry ", book_author="kj",book_price=50)
# book_3 = Book_store(book_title="porter", book_author="jj",book_price=90)
#
# print(book_1.book_title,book_1.book_author,book_1.book_price)
# print(book_2.book_title,book_2.book_author,book_2.book_price)
# print(book_3.book_title,book_3.book_author,book_3.book_price)


#assuming there is a fixed price , it will just print the first thing in the params otherwise print the new argument

# class Book_store:
#     def __init__(self, book_title, book_author, book_price = 90):
#         self.book_title = book_title
#         self.book_author = book_author
#         self.book_price = book_price
#
# book_1 = Book_store(book_title="harry porter", book_author="jk",book_price=100)
# book_2 = Book_store(book_title="harry ", book_author="kj")
# book_3 = Book_store(book_title="porter", book_author="jj")
#
# print(book_1.book_title,book_1.book_author,book_1.book_price)
# print(book_2.book_title,book_2.book_author,book_2.book_price)
# print(book_3.book_title,book_3.book_author,book_3.book_price)

# a method wth function
class Book_store:
    def __init__(self, book_title, book_author, book_price = 100):
        self.book_title = book_title
        self.book_author = book_author
        self.book_price = book_price

    def descr(self):
        price = self.book_price * 100
        print(f"{self.book_author},the author of {self.book_title},sold 100 copies for {price}")


book_1 = Book_store(book_title="harry porter", book_author="jk",book_price=100)
book_2 = Book_store(book_title="harry ", book_author="kj")
book_3 = Book_store(book_title="porter", book_author="jj")
book_1.descr()
book_2.descr()
book_3.descr()

#do a bank shit
#write a python program that would extract a text from pdf

# print(book_1.book_title,book_1.book_author,book_1.book_price)
# print(book_2.book_title,book_2.book_author,book_2.book_price)
# print(book_3.book_title,book_3.book_author,book_3.book_price)

#inheritance
#a class


class Shop:
    def __init__(self):
        self.name = "fatihat"
        self.age = 30



class Teashop(Shop):  # child class
    pass


shop_1 = Teashop()

print(shop_1.name)
print(shop_1.age)

# print()

