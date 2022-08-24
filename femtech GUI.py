from tkinter import *

import pymysql
from tkinter import messagebox

root = Tk()

root.geometry("1000x1000")
root.configure(bg="silver")


# make the delete function work
def delete(id):
    x = messagebox.askquestion("wait", "delete user?")
    if x == "yes":
        con = pymysql.connect(host="localhost", user="root", password="", db="gui")
        mycursor = con.cursor()
        msg = "delete from users where id = {}"
        query = msg.format(id)
        mycursor.execute(query)
        con.commit()
        messagebox.showinfo("success", "user deleted successfully")
    else:
        messagebox.showinfo("failed", " details still intact")


# global editor


def edit(id):
    editor = Tk()
    # editor.geometry("1000X1000")
    editor.title("Update User")
    # connect to database
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="gui"

    )
    # create a cursor
    my_cursor = conn.cursor()
    query = "select * from users where id={}"
    text = query.format(id)
    my_cursor.execute(text)
    users = my_cursor.fetchall()
    print(users)

    def save():
        connect = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="gui"
        )
        my_cursor = connect.cursor()
        query = 'update users set firstname=%s, last_name= %s,middlename= %s, email= %s,pass_word= %s, where id =%s'
        firstname = lab_1.get()
        last_name = lab_2.get()
        middlename = lab_3.get()
        email = lab_4.get()
        pass_word = lab_0.get()
        id = lab_id.get()

        input = (firstname, last_name, middlename, email, pass_word, id)
        my_cursor.execute(query, input)
        connect.commit()
        editor.destroy()

    lab = Label(editor, text="UPDATE USER", font=("sans-serif", 20), fg="red")
    lab.place(x=100, y=20)
    lab_id = Entry(editor)
    lab_id.place(x=250, y=50)
    lab_id.insert(0, users[0][0])

    lab_0 = Entry(editor, show="*")
    lab_0.place(x=250, y=80)
    lab_0.insert(0, users[0][5])
    # entry 1

    lab_1 = Entry(editor)
    lab_1.place(x=250, y=130)
    lab_1.insert(0, users[0][1])
    # Entry 2

    lab_2 = Entry(editor)
    lab_2.place(x=250, y=180)
    lab_2.insert(0, users[0][2])

    # Entry 3
    lab_3 = Entry(editor)
    lab_3.place(x=250, y=230)
    lab_3.insert(0, users[0][3])

    # entry 4
    lab_4 = Entry(editor)
    lab_4.place(x=250, y=280)
    lab_4.insert(0, users[0][4])

    # text 5
    # lab_5 = Entry(editor)
    # lab_5.place(x=250, y=330)
    # lab_5.insert(0, users[0][0])

    label_id = Label(editor, text="id:", width=20, font=("bold", 10))
    label_id.place(x=80, y=50)

    label_1 = Label(editor, text="firstname:", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)

    label_2 = Label(editor, text="last_name:", width=20, font=("bold", 10))
    label_2.place(x=68, y=180)

    label_3 = Label(editor, text="middlename:", width=20, font=("bold", 10))
    label_3.place(x=70, y=230)

    label_4 = Label(editor, text="email:", width=20, font=("bold", 10))
    label_4.place(x=73, y=280)

    label_5 = Label(editor, text="password:", width=20, font=("bold", 10))
    label_5.place(x=80, y=80)

    sav = Button(editor, text="save", padx=10, pady=5, command=save, bg="blue", fg="white")
    sav.place(x=200, y=550)


def list_users():
    list_user = Tk()
    list_user.geometry("500x500")
    connect = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="gui"
    )
    # create a cursor
    my_cursor = connect.cursor()
    query = "select * from users"
    my_cursor.execute(query)
    users = my_cursor.fetchall()
    # create user heading

    id = Label(list_user, text="id", width=0, font=("bold", 10)).grid(row=0, column=0)
    firstname = Label(list_user, text="firstname", width=10, font=("bold", 10)).grid(row=0, column=1)
    lastname = Label(list_user, text="last_name", width=10, font=("bold", 10)).grid(row=0, column=2)
    middlename = Label(list_user, text="middlename", width=10, font=("bold", 10)).grid(row=0, column=3)
    email = Label(list_user, text="email", width=20, font=("bold", 10)).grid(row=0, column=4)
    password = Label(list_user, text="password", width=10, font=("bold", 10)).grid(row=0, column=5)
    edd = Label(list_user, text="edit", width=10, font=("bold", 10)).grid(row=0, column=6)
    dl = Label(list_user, text="delete", width=10, font=("bold", 10)).grid(row=0, column=7)

    row_count = 1
    column_count = 0
    # to iterate through each entry
    for i in users:
        id = Label(list_user, text=i[0], width=0, font=("bold", 10)).grid(row=row_count, column=column_count)
        firstname = Label(list_user, text=i[1], width=10, font=("bold", 10)).grid(row=row_count,
                                                                                  column=column_count + 1)
        lastname = Label(list_user, text=i[2], width=10, font=("bold", 10)).grid(row=row_count, column=column_count + 2)
        middlename = Label(list_user, text=i[3], width=10, font=("bold", 10)).grid(row=row_count,
                                                                                   column=column_count + 3)
        email = Label(list_user, text=i[4], width=20, font=("bold", 10)).grid(row=row_count, column=column_count + 4)
        password = Label(list_user, text=i[5], width=10, font=("bold", 10)).grid(row=row_count, column=column_count + 5)

        edd = Button(list_user, text="edit", width=10, font=("bold", 10), command=lambda id=i[0]: edit(id)).grid(
            row=row_count, column=column_count + 6)
        dl = Button(list_user, text="delete", width=10, font=("bold", 10), command=lambda id=i[0]: delete(id)).grid(
            row=row_count,
            column=column_count + 7)

        row_count += 1
        connect.commit()


def register():
    x = messagebox.askquestion("Register", " do you want to sign up")
    if x == "yes":
        first_name = Entry_box.get()
        last_name = Entry_box1.get()
        surname = Entry_box2.get()
        email = Entry_box3.get()
        password = Entry_box4.get()
        cpassword = Entry_box5.get()
        if first_name == "":
            messagebox.showerror("firstname", "enter firstname")
        elif last_name == "":
            messagebox.showerror("lastname", "enter lastname")
        elif surname == "":
            messagebox.showerror("middle_name:", "enter surname")
        elif email == "":
            messagebox.showerror("email:", "enter email")
        elif password == "":
            messagebox.showerror("password", "enter password")
        elif cpassword == "":
            messagebox.showerror("confirm_password", "enter the right password ")
        else:
            conn = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="gui"
            )
            my_cursor = conn.cursor()
            text = "INSERT INTO users VALUES('', '{}','{}','{}', '{}','{}' )"
            query = text.format(first_name, last_name, surname, email, password)
            my_cursor.execute(query)
            conn.commit()
            Entry_box.delete(0, END)
            Entry_box1.delete(0, END)
            Entry_box2.delete(0, END)
            Entry_box3.delete(0, END)
            Entry_box4.delete(0, END)
            Entry_box5.delete(0, END)
            messagebox.showinfo("success", "registration successful")
        # print("successful")

        ok_label = Label(root, text="you clicked yes")
        ok_label.place()


def button():
    name = Entry_box.get()

    print("Thank you for registering... {}".format(name))


# def register():
# root.geometry("500x500")
root.config(background="white")
btn = Button(root, text="Register", fg="white", bg="Black", command=register)
label = Label(root, text="Firstname: ")
label_1 = Label(root, text="last_name:")
label_2 = Label(root, text="middlename:")
label_3 = Label(root, text="Email:")
label_4 = Label(root, text="pass_word:")
label_5 = Label(root, text="confirm Pword")
Box = Label(root, text="about")
btn_6 = Button(root, text="List_users", bg="Black", fg="White", command=list_users)

Entry_box = Entry(root)
Entry_box1 = Entry(root)
Entry_box2 = Entry(root)
Entry_box3 = Entry(root)
Entry_box4 = Entry(root)
Entry_box5 = Entry(root)
box_entry = Entry(root)
Entry_box.pack()
btn.pack()

Entry_box = Entry(root)
# Entry_box.pack
#
btn.place(x=50, y=50)
label.place(x=50, y=100)
Entry_box.place(x=150, y=100)
label_1.place(x=50, y=150)
Entry_box1.place(x=150, y=150)
label_2.place(x=50, y=200)
Entry_box2.place(x=150, y=200)
label_3.place(x=50, y=250)
Entry_box3.place(x=150, y=250)
label_4.place(x=50, y=300)
Entry_box4.place(x=150, y=300)
label_5.place(x=50, y=350)
Entry_box5.place(x=150, y=350)
# Box.place(x=150, y=400)
# box_entry.place(x=150, y=400, width=100, height=50)
btn_6.place(x=50, y=400)
Entry_box.place(x=150, y=100)

root.mainloop()
