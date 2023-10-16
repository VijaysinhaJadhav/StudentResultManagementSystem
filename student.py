from tkinter import*
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
# the above line is used to CREATE TABLE

import sqlite3
# the above line is used for database withour installing external software


class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        # dashboard geometry(width,height,leftmost,rightmost)
        self.root.geometry("1350x580+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        # the above line is used so that the user need not click on the Course Details interface to make it responsive

        # TITLE
        title = Label(self.root, text="Manage Student Details", font=(
            "times new roman", 20, "bold"), bg="black", fg="red").place(x=10, y=15, width=1330, height=35)

        # VARIABLES --> these variables are used to store the data present in text fields of Course Details
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        #self.var_dob = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        # WIDGETS(LABEL)
        lbl_roll = Label(self.root, text="Roll No.", font=("times new roman", 15, 'bold'), bg='white', fg="red").place(x=10, y=60)
        lbl_Name = Label(self.root, text="Name", font=("times new roman", 15, 'bold'), bg='white', fg="red").place(x=10, y=100)
        lbl_Email = Label(self.root, text="Email", font=("times new roman", 15, 'bold'), bg='white', fg="red").place(x=10, y=140)
        lbl_gender = Label(self.root, text="Gender", font=("times new roman", 15, 'bold'), bg='white', fg="red").place(x=10, y=180)

        lbl_state = Label(self.root, text="State", font=("times new roman", 15, 'bold'), bg='white', fg="red").place(x=10, y=220)
        txt_state = Entry(self.root, textvariable=self.var_state, font=("times new roman", 15), bg='white', fg="black").place(x=150, y=220, width=150)

        lbl_city = Label(self.root, text="City", font=("times new roman", 15, 'bold'), bg='white', fg="red").place(x=310, y=220)
        txt_city = Entry(self.root, textvariable=self.var_city, font=("times new roman", 15), bg='white', fg="black").place(x=380, y=220, width=100)

        lbl_pin = Label(self.root, text="Pin", font=("times new roman", 15, 'bold'), bg='white', fg="red").place(x=500, y=220)
        txt_pin = Entry(self.root, textvariable=self.var_pin, font=("times new roman", 15), bg='white', fg="black").place(x=560, y=220, width=120)

        lbl_address = Label(self.root, text="Address", font=("times new roman", 15, 'bold'), bg='white', fg="red").place(x=10, y=260)
        lbl_dob = Label(self.root, text="D.O.B", font=("times new roman", 15, 'bold'), bg='white', fg="red").place(x=360, y=60)
        lbl_contact = Label(self.root, text="Contact", font=("times new roman", 15, 'bold'), bg='white', fg="red").place(x=360, y=100)
        lbl_admission = Label(self.root, text="Admission Date", font=("times new roman", 15, 'bold'), bg='white', fg="red").place(x=360, y=140)
        lbl_course = Label(self.root, text="Course", font=("times new roman", 15, 'bold'), bg='white', fg="red").place(x=360, y=180)

        # ENTRY(TEXT) FIELDS
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("times new roman", 15), bg='white', fg="black")
        self.txt_roll.place(x=150, y=60, width=200)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("times new roman", 15), bg='white', fg="black").place(x=150, y=100, width=200)
        txt_email = Entry(self.root, textvariable=self.var_email, font=("times new roman", 15), bg='white', fg="black").place(x=150, y=140, width=200)
        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select","Male","Female","Other"), font=("times new roman", 15),state='readonly',justify=CENTER)
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)
        #the above line is used to get the SELECT option in the COMBO BOX of GENDER
        

        self.course_list=[]
        #the above line is the FUNCTION CALL to UPDATE the list in the COMBOBOX of COURSE
        self.fetch_course()
        #txt_dob = Entry(self.root, textvariable=self.var_dob, font=("times new roman", 15), bg='white', fg="black").place(x=480, y=60, width=200)
        txt_dob=DateEntry(self.root, textvariable=self.var_dob,selectmode='day',state='readonly',justify=CENTER).place(x=500, y=60, width=180)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("times new roman", 15), bg='white', fg="black").place(x=500, y=100, width=180)
        #txt_admission = Entry(self.root, textvariable=self.var_a_date, font=("times new roman", 15), bg='white', fg="black").place(x=500, y=140, width=180)
        txt_admission=DateEntry(self.root, textvariable=self.var_a_date,selectmode='day',state='readonly',justify=CENTER).place(x=500, y=140, width=180)
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course,values=self.course_list, font=("times new roman", 15),state='readonly',justify=CENTER)
        self.txt_course.place(x=500, y=180, width=180)
        self.txt_course.set("Select")
        #the above line is used to get the SELECT option in the COMBO BOX of COURSE



        self.txt_address = Text(self.root, font=("times new roman", 15), bg='white', fg="black")
        self.txt_address.place(x=150, y=260, width=540, height=100)
        # Entry allows you to input data into textfield but, you can not jump to next line
        # Text is same as Entry but, here you can jump into multiple lines

        # BUTTONS
        self.btn_add = Button(self.root, text='Save', font=(
            "times new roman", 15, "bold"), bg="black", fg="red", cursor="hand2", command=self.add)
        # (command=self.add) is used to access the add()
        self.btn_add.place(x=150, y=400, width=110, height=40)
        self.btn_update = Button(self.root, text='Update', font=(
            "times new roman", 15, "bold"), bg="black", fg="red", cursor="hand2", command=self.update)
        # (command=self.update) is used to access the update()
        self.btn_update.place(x=270, y=400, width=110, height=40)
        self.btn_delete = Button(self.root, text='Delete', font=(
            "times new roman", 15, "bold"), bg="black", fg="red", cursor="hand2", command=self.delete)
        # (command=self,delete) is used to access the delete()
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        self.btn_clear = Button(self.root, text='Clear', font=(
            "times new roman", 15, "bold"), bg="black", fg="red", cursor="hand2", command=self.clear)
        # (command=self.clear) is used to access the clear()
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # SEARCH PANEL
        self.var_search = StringVar()
        lbl_search_roll = Label(self.root, text="Search By Roll No.", font=(
            "times new roman", 15), bg='white', fg="black").place(x=720, y=60)
        txt_search_roll = Entry(self.root, textvariable=self.var_search, font=(
            "times new roman", 15), bg='white', fg="black").place(x=900, y=60, width=180)
        btn_search = Button(self.root, text='Search', font=("times new roman", 15), bg="green",
                            fg="black", cursor="hand2", command=self.search).place(x=1120, y=60, width=150, height=28)

        # FRAME OF SEARCH COURSE DETAILS
        self.C_Frame = Frame(self.root, bd=2, relief=RAISED)
        self.C_Frame.place(x=720, y=100, width=550, height=400)

        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)
        # the above lines are used to get the SCROLL BARS

        # TABLE OF SEARCH STUDENT DETAILS
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=(
            "roll", "name", "email", "gender", "dob", "contact", "admission", "course", "state", "city", "pin", "address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        # the above line creates the HEADING COLUMNS FOR THE TABLE with an ADDITIONAL COLUMN in the beginning

        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        # the above lines are used make the SCROLL BAR WORK

        self.CourseTable.heading("roll", text="Roll No.")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("gender", text="Gender")
        self.CourseTable.heading("dob", text="D.O.B")
        self.CourseTable.heading("contact", text="Contact")
        self.CourseTable.heading("admission", text="Admission")
        self.CourseTable.heading("course", text="Course")
        self.CourseTable.heading("state", text="State")
        self.CourseTable.heading("city", text="City")
        self.CourseTable.heading("pin", text="PIN")
        self.CourseTable.heading("address", text="Address")
        # the above five lines are used to input COLUMN NAMES AS HEADINGS

        self.CourseTable["show"] = 'headings'
        # the above line HIDES the ADDITIONAL COLUMN

        self.CourseTable.column("roll", width=100)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("email", width=100)
        self.CourseTable.column("gender", width=100)
        self.CourseTable.column("dob", width=100)
        self.CourseTable.column("contact", width=100)
        self.CourseTable.column("admission", width=100)
        self.CourseTable.column("course", width=100)
        self.CourseTable.column("state", width=100)
        self.CourseTable.column("city", width=100)
        self.CourseTable.column("pin", width=100)
        self.CourseTable.column("address", width=200)
        # the above lines set the width of COLUMNS

        self.CourseTable.pack(fill=BOTH, expand=1)
        # the above line is used to create the TRABLE with same width and height as that of FRAME

        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        # the above line is used to get the data in the TEXT FIELD of the COURSE DETAILS from the DATABASE
        self.show()

    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        #self.var_dob.set(""),
        self.var_dob.set(""),
        self.var_contact.set("Select"),
        self.var_a_date.set(""),
        self.var_course.set(""),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.txt_address.delete("1.0", END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        # the above line is used to create an empty database

        cur = con.cursor()
        # the above line is used to execute the sql query

        try:
            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Error", "Please provide Roll No.", parent=self.root)
                # the above line displays the ERROR in the ROOT WINDOW i.e., DASHBOARD

            else:
                cur.execute("select * from student where roll=?",
                            (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Please Select the student from the List", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you really want to delete it?", parent=self.root)
                    if op == True:
                        cur.execute("delete from student where roll=?",
                                    (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Student deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # FUCTION TO FETCH the data from DATABASE to the STUDENT TEXTFIELDS
    def get_data(self, ev):
        self.txt_roll.config(state='readonly')
        # the above line does not allow the user to UPDATE the ROLL NO.
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_a_date.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END,row[11])

    # DISPLAY MESSAGE BOX based on the input given
    def add(self):
        con = sqlite3.connect(database="rms.db")
        # the above line is used to create an empty database

        cur = con.cursor()
        # the above line is used to execute the sql query

        try:
            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Error", "Please provide Roll No.", parent=self.root)
                # the above line displays the ERROR in the ROOT WINDOW i.e., DASHBOARD
            else:
                cur.execute("select * from student where roll=?",
                            (self.var_roll.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "Roll No. already exists", parent=self.root)
                else:
                    cur.execute("insert into student (roll, name, email, gender, dob, contact, admission, course, state, city, pin, address) values(?,?,?,?,?,?,?,?,?,?,?,?)", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Student Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        # the above TRY AND EXCEPT structure is used to DISPLAY the ERROR in MESSAGE BOX

    def update(self):
        con = sqlite3.connect(database="rms.db")
        # the above line is used to create an empty database

        cur = con.cursor()
        # the above line is used to execute the sql query

        try:
            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Error", "Please provide Roll. No.", parent=self.root)
                # the above line displays the ERROR in the ROOT WINDOW i.e., DASHBOARD

            else:
                cur.execute("select * from student where roll=?",
                            (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Select Student  from list", parent=self.root)
                else:
                    cur.execute("update student set name=?, email=?, gender=?, dob=?, contact=?, admission=?, course=?, state=?, city=?, pin=?, address=? where roll=?", (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0", END),
                        self.var_roll.get(),
                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Student Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        # the above TRY AND EXCEPT structure is used to DISPLAY the ERROR in MESSAGE BOX

    def show(self):
        con = sqlite3.connect(database="rms.db")
        # the above line is used to create an empty database

        cur = con.cursor()
        # the above line is used to execute the sql query

        try:
            cur.execute("select * from student")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        # the above TRY AND EXCEPT structure is used to DISPLAY the ERROR in MESSAGE BOX

    #This fuction is used to get the courses in the COURSE COMBO BOX of STUDENT DETAILS
    def fetch_course(self):
        con = sqlite3.connect(database="rms.db")
        # the above line is used to create an empty database
        cur = con.cursor()
        # the above line is used to execute the sql query
        try:
            cur.execute("select name from course")
            rows = cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        # the above TRY AND EXCEPT structure is used to DISPLAY the ERROR in MESSAGE BOX    

    def search(self):
        con = sqlite3.connect(database="rms.db")
        # the above line is used to create an empty database

        cur = con.cursor()
        # the above line is used to execute the sql query

        try:
            cur.execute(
                "select * from student where roll=?",(self.var_search.get(),))
            row = cur.fetchone()
            if row!=None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        # the above TRY AND EXCEPT structure is used to DISPLAY the ERROR in MESSAGE BOX


if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()
