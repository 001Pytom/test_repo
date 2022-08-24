from tkinter import *

# # graphical user interface. intermediate between human and machines
# # it is also the visual representation of functions
# # GUI frame works
# # - tkinter, kivy, pyQt5, Pygame
# # tkinter, commonly used ui liberties in python. it comes with python standard libray
#
#
# main_window = Tk()
# # labels: are types of widget(components) that are used to display an output to the end user
# # create a label
# # Label(main_window, text="HELLO WORLD!").pack()
# # .GRID allow us to arrange widgets in rows and columns
# # .pack
# # Label(main_window, text="This is tkinter").pack()
# Label(main_window, text="Enter Your Name: ").grid(row=0, column=0)
# Label(main_window, text="What is Your age:").grid(row=1, column=0)
#
# # text input, use enter class to capture any data from the other side
#
#
# my_name = Entry(main_window, width=50, borderwidth=5).grid(row=0, column=1)
#
# my_age = Entry(main_window, width=50, borderwidth=5).grid(row=1, column=1)
#
#
# # call back function to make it perform a task
# def on_click():
#     print(f"my name is {my_name} and my age is {my_age}")
#
#
# # button digit
# Button(main_window, text="login", command=on_click).grid(row=2, column=1)
# # you'll need a call back function, to make it perform  a task
#
#
# main_window.mainloop()

#CREATE A SIMPLE CALCULATOR
#CREATE A CLASS FIRST, root is the instance of the class
root = Tk()
#text input area
e = Entry(root, width= 35, borderwidth= 5)
e.grid(row= 0, column=0, columnspan=3, padx= 30, pady=30)
list_of_no = []
def number_input(number):
    current_value = e.get()
    e.delete(0,END)
    e.insert(0, str(current_value)+str(number))

def clear_values():
    list_of_no.clear()
    e.delete(0, END)

def sum_of_values():
    num1 = e.get()
    list_of_no.append(num1)
    e.delete(0, END)

def equals():
    num1 = e.get()
    list_of_no.append(int(num1))
    e.delete(0, END)


    SUM = 0
    for values in list_of_no:
        SUM += int(values)

    e.insert(0,str(SUM))


#buttons 9-0, add buttn: add, clear,equals
buttn9 = Button(root, text="9", padx=40, pady=20, command=lambda : number_input(9)).grid(row =1 , column=0)
buttn8 = Button(root, text="8", padx=40, pady=20, command=lambda : number_input(8)).grid(row = 1, column=1)
buttn7 = Button(root, text="7", padx=40, pady=20, command=lambda : number_input(7)).grid(row =1 , column=2)

buttn6 = Button(root, text="6", padx=40, pady=20, command=lambda : number_input(6)).grid(row=2 , column=0)
buttn5 = Button(root, text="5", padx=40, pady=20, command=lambda : number_input(5)).grid(row =2 , column=1)
buttn4 = Button(root, text="4", padx=40, pady=20, command=lambda : number_input(4)).grid(row =2 , column=2)

buttn3 = Button(root, text="3", padx=40, pady=20, command=lambda : number_input(3)).grid(row =3, column=0)
buttn2 = Button(root, text="2", padx=40, pady=20, command=lambda : number_input(2)).grid(row =3 , column=1)
buttn1 = Button(root, text="1", padx=40, pady=20, command=lambda : number_input(1)).grid(row =3, column=2)

buttn0 = Button(root, text="0", padx=40, pady=20, command=lambda : number_input(0)).grid(row =4 , column=0)

buttn_add = Button(root, text="+", padx=40, pady=20, command=sum_of_values).grid(row =4, column=1)
buttn_clear = Button(root, text="cls", padx=40, pady=20, command=clear_values).grid(row =5 , column=0)
buttn_equal = Button(root, text="=", padx=40, pady=20, command=equals).grid(row =5, column=1)
buttn_last = Button(root, text="FAATIHAT", padx=40, pady=20).grid(row=4 , column=2)
buttn_last2 = Button(root, text="CALC.", padx=40, pady=20).grid(row=5 , column=2)

root.mainloop()


root.mainloop()


