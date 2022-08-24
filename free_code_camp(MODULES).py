# IMPORTING PYTHON FILES THAT HAVE CLASSES IN THEM
# from filename import the class-name
# create a python class called birthday boy that takes in two variables
# - a string called name and an integer called age. don't forget to use the innit method
# within Birthdayboy create a method called birthday , and ensure it returns an increase in the age + 1
class BirthdayBoy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        increase = self.age + 1
        return increase
        # print( f"{self.name} age has increased to {increase}")


boy = BirthdayBoy("hayat", 22)

print(boy.birthday())


# new question


# class Salesperson:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.sales = 0
#
#
#
#
#     def makeSale(self, integer):
#         self.sales = self.sales + integer
#
#
#     def salesReport(self):
#         print("my total sales are {}.".format(self.sales))
#
#
#
# firstperson = Salesperson("Nick", "Mccullun")
# firstperson.makeSale(500)
# firstperson.salesReport()

# next quest
class Pet:
    def __init__(self):
        self.__name = "no name"
        self.__animal_type = "no type"
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def __str__(self):
        stringg = "{} is {} year old {}".format(self.__name, self.__age, self.__animal_type)
        return stringg


animal1 = Pet()
animal1.set_name("jerry")
animal1.set_animal_type("dog")
animal1.set_age(1)
animal1.get_animal_type()
animal1.get_age()
animal1.get_name()
print(animal1.__str__())


# quest3 an example of inheritance


class Parent:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def greeting(self):
        print("hello my name is {} {}.".format(self.firstname, self.lastname))


class Child(Parent):
    def __init__(self, firstname, lastname, school_year):
        super().__init__(firstname, lastname)
        self.school_year = school_year



    def something(self):
        print("she is my mother and i love her soo much.")


parent_instance = Parent("faatihat", "mohammed")
child_instance = Child("hayat", "mohammed", "class 2")


child_instance.greeting()
parent_instance.greeting()
child_instance.something()


