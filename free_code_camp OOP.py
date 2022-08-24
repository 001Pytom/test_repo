# import csv
# class Item:
#     #we also have what we call class attribute. it belongs to the class itself, though instances can access it too
#     # it is GLOBAL TO all the program
#     pay_rate = 0.8
#     all = []
#
#     def __init__(self, name: str, price: float, quantity):
#         # print("An instance created: {}".format(name))
#         #you can specify the type you want from the top . i.e. name: str
#         #if you never want to receive a negative number of price we use the asset statement
#         assert price >= 0
#         #you can also add your own exception messages
#         assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero"
#
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#         #actions to execute, call the class first
#         Item.all.append(self)
#
#
#
#     def calculate_total_price(self):
#         return self.price * self.quantity
#
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate
#
#     @classmethod
#     def instantiate_from_csv(cls):
#         with open("items.csv", "r") as f:
#             reader = csv.DictReader(f)
#             items = list(reader)
#
#         for item in items:
#             print(item)
#
#
#
# #if you use print(Item.all),it only prints the object notation.if you want it to print in a way you will
# understand, #use __rep__method
#
#
#     def __repr__(self):
#         return f"Item('{self.name}, {self.price}, {self.quantity}')"
#
#
#
# Item.instantiate_from_csv()
# item1 = Item("phone", 100, 1)
# item2 = Item("laptop", 1000, 3)
# item3 = Item("cable", 10, 5)
# item4 = Item("mouse", 50, 5)
# item5 = Item("mouse", 5, 5)
#
#
# # print(item2.name)
# # print(item1.name)
# # print(item2.calculate_total_price())
# # print(item1.calculate_total_price())
# # print(Item.pay_rate)
# # print(item2.pay_rate)
# # #if you want to see all the attribute for any level e.g. using magic method __dict__
# # print(Item.__dict__)
# # print(item1.__dict__)
# for instance in Item.all:
#     print(instance.name, end=",")
#     print(instance.price, end=",")
#     print(instance.quantity, end="\n")
#
# #it worked because of __repr__ method
# print(Item.all)
#
# # print(item1.calculate_total_price(item1.price, item1.quantity))
# # print(item2.calculate_total_price(item1.price, item1.quantity))
# #CSV, comma separated value, allows data to be stored in a table
#
# #encapsulation, here we use getters and setters
#
#
# class Car:
#     def __init__(self, speed, color):
#         self.__speed = speed
#         self.color = color
#
#
#     #using the private attribute inside the class
#     def public_method(self):
#         print("we can use the{}here since it is inside the class,but you cant access it outside".format(self.__speed))
#
#
#     #defining a private method now
#
#
#     def __private_method(self):
#         print("this is a private method")
#
#
#     def set_speed(self, value):
#         self.__speed = value
#
#     def get_speed(self):
#         return self.__speed
#
#
#
# ford = Car("speed", "red")
# print(ford.color)
# #this would print car has no object speed, to make it work, we will use the getter and setter method
# # print(ford.__speed)
# ford.set_speed(3000)
# print(ford.get_speed())
# ford.public_method()


#INHERITANCE, the subclass have access to both methods and instance of the super class
#supr class
class Polygon:
    #private member variables
    __width = None
    __height = None


    def set_values(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width


    def get_height(self):
        return self.__height


# subclass
class Rectangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height()

#subclass


class Triangle(Polygon):
    def area(self):
        return (self.get_width() * self.get_height()) / 2


rect = Rectangle()
tri = Triangle()
#this will work because we are inheriting from the parent or base class
rect.set_values(10, 5)
print(rect.area())
tri.set_values(5, 10)
print(tri.area())






