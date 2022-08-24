# classes are used for more complex data structures. they contain functions that describe the
# behaviour of our class. it is basically a blueprint

# class
class SoftwareEngineer:
    # class attribute
    alias = "keyboard magician"

    # special kind of method, you can add your arguments,but it must have self first
    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # INSTANCE METHOD
    def code(self):
        print("{} is writing code".format(self.name))

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    # def information(self):
    #     information = f"name = {self.name}, age = {self.age}, level = {self.level}"
    #     return information

    # Special methods are the d_under methods
    # this will be executed whenever our obj is converted to a string. it will print se1 without adding .information
    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information
        # instance

    # here we compare two objects,we get true here because it is now comparing what we see not the memory address.
    def __eq__(self, other):
        return self.name == other.name

    @staticmethod  # A static method does not receive an implicit first argument.To declare a static method,usethisidiom
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


# se1 = SoftwareEngineer("faatihat", 20, "junior", 5000)
# se2 = SoftwareEngineer("tomiwa", 25, "senior", 7000)
# se3 = SoftwareEngineer("tomiwa", 25, "senior", 7000)
# print(se1.name)
# print(se1.age)
# print(se1.alias)
# print(se2.alias)
# print(SoftwareEngineer.alias)
# se1.code()  # *
# se2.code()
# se1.code_in_language("python")
# se2.code_in_language("c++")
# # print(se1.information())
# print(se1)
# print(se2 == se3)
# # it is false because it is comparing its memory address
# print(se1.entry_salary(24))
# print(SoftwareEngineer.entry_salary(27))


# FUNCTIONS IN CLASSES , NOTE THAT FOR EVERY INSTANCE METHOD YOU NEED TO WRITE \SELF
# INHERITANCE
# THIS IS THE PROCESS BY WHICH ONE CLASS TAKES ON THE ATTRIBUTE AND METHODS OF ANOTHER CLASS
# we will have base class and child class
# #so here our base class is employee and child class or subclass is softengineer


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")

# THOUGH THE SUBCLASS CAN ALSO HAVE ITS OWN METHODS AND ATTRIBUTES


class SoftEngineer(Employee):
    def __init__(self, name, age, salary, level):
        #you don't need to type self.name ..again instead you call the initializer of its parent class
        super().__init__(name, age, salary)
        self.level = level


    #we can also override this like we did when we use the super()__init__
    #overriding means having two methods with the same name but doing diff task


    def work(self):
        print(f"{self.name} is coding...")

    # this one is a new fxn, so we are just extending not over-riding
    def debug(self):
        print(f"{self.name} is debugging...")


class Designer(Employee):



    def work(self):
        print(f"{self.name} is designing...")

    def draw(self):
        print(f"{self.name} is drawing...")


# se = SoftEngineer("faatihat", 20, 6000, "junior")
# print(se.name, se.age, se.level)
# se.work()
# print(se.level)
# se.debug()
# se.work()
#
#
#
# d = Designer("tomiwa", 22, 7000)
# print(d.name, d.age)
# d.work()
# d.draw()
#you have over-ridden the fxn
# d.work()


#POLYMORPHISM
#THIS IS GREEK AND IT MEANS MANY SHAPES
#Polymorphism simply means a way to use a class like its parents,
# still the child class keeps its own methods as they are.

# employees = [SoftEngineer("faatihat", 20, 5000, "junior"),
#              SoftEngineer("tom", 25, 9000, "senior"),
#              Designer("tomiwa", 22, 7000)]
#
#
#
# def motivate_employee(employees):
#     for employee in employees:
#         employee.work()
#
#
# motivate_employee(employees)


#polymorphism 2
