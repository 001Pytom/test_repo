from tkinter import *

# Build a normal calc using GUI
# Note that all answers will be given in float

root = Tk()
root.title("My Simple calculator")


# define the button function for all number buttons
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# define the clear function
def button_clear():
    e.delete(0, END)


# define the add function
def button_add():
    first_number = e.get()
    global math
    global first_num
    math = "addition"
    first_num = float(first_number)
    e.delete(0, END)


# make the equal sine have different function
def button_eq():
    sec_number = e.get()
    e.delete(0, END)
    global sec_num
    sec_num = int(sec_number)
    if math == "addition":
        e.insert(0, float(sec_num + first_num))
    if math == "subtraction":
        e.insert(0, float(first_num - sec_num))
    if math == "multiplication":
        e.insert(0, float(sec_num) * first_num)
    if math == "division":
        e.insert(0, float(first_num / sec_num))


# define subtraction function
def button_subt():
    first_number = e.get()
    global math
    global first_num
    math = "subtraction"
    first_num = float(first_number)
    e.delete(0, END)


# define multiplication function
def button_mult():
    first_number = e.get()
    global math
    global first_num
    math = "multiplication"
    first_num = float(first_number)
    e.delete(0, END)


# define division function
def button_div():
    first_number = e.get()
    global math
    global first_num
    math = "division"
    first_num = float(first_number)
    e.delete(0, END)

# The main entry
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_ad = Button(root, text="+", padx=40, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_eq)
button_cls = Button(root, text="clear", padx=31, pady=20, command=button_clear)

button_sub = Button(root, text="-", padx=41, pady=20, command=button_subt)
button_mul = Button(root, text="X", padx=39, pady=20, command=button_mult)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_div)
button_dot = Button(root, text=".", padx=39, pady=20, command=lambda: button_click("."))

# but the button on the screen or call buttons

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_ad.grid(row=5, column=0)
button_cls.grid(row=5, column=1)
button_equal.grid(row=6, column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_divide.grid(row=4, column=1)
button_mul.grid(row=4, column=2)
button_dot.grid(row=5, column=2)

root.mainloop()
