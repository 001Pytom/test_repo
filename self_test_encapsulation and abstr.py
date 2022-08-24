# ENCAPSULATION
# THIS MEANS HIDING OF DATA IMPLEMENTATION. That is the instance variables are kept private.
# you can only access it inside the class, i.e. using the indentation
# there is only one (accessors) method from the outside
#we can access it using getters and setters, you won't be able to access it from the outside using se.__salary or so
class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        #  if we want the salary or any to be private. u use __ to make it very private , most people use _
        #_x is called protected attribute and __x is called private attribute
        self.__salary = None
        self.__num_bugs_solves = 0




    #getters
    def get_salary(self):
        return self.__salary
    #setters

    def set_salary(self, value):




        # check value, enforce constrain
        # if value < 1000:
        #     self.__salary = 1000
        # if value > 20000:
        #     self.__salary = 20000
        # self.__salary = value


se = SoftwareEngineer("faatihat", 25)
print(se.age, se.name)
se.set_salary(100)
print(se.get_salary())