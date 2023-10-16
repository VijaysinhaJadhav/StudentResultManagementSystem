from tkinter import*
from tkinter import ttk, messagebox
# the above line is used to CREATE TABLE

import sqlite3
# the above line is used for database withour installing external software


class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        # dashboard geometry(width,height,leftmost,rightmost)
        self.root.geometry("1350x580+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        # the above line is used so that the user need not click on the Course Details interface to make it responsive

        # TITLE
        title = Label(self.root, text="Add Student Results", font=(
            "times new roman", 20, "bold"), bg="black", fg="red").place(x=10, y=15, width=1330, height=35)
        
        #Variables
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list=[]
        self.fetch_roll()

        # label
        lbl_select=Label(self.root,text="Student Roll No.",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=375,y=100)
        lbl_name=Label(self.root,text="Name",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=375,y=160)
        lbl_course=Label(self.root,text="Course",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=375,y=220)
        lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=375,y=280)
        lbl_full_marks=Label(self.root,text="Max Marks",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=375,y=340)
        
        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll,values=self.roll_list, font=("times new roman", 15),state='readonly',justify=CENTER)
        self.txt_student.place(x=600, y=100, width=200)
        self.txt_student.set("Select")
        btn_search = Button(self.root, text='Search', font=("times new roman", 15), bg="green",
                            fg="black", cursor="hand2",command=self.search).place(x=820, y=100, width=100, height=28)

        txt_name = Entry(self.root, textvariable=self.var_name, font=(
            "times new roman", 20), bg='white', fg="black",state='readonly').place(x=600, y=160, width=320)
        txt_course = Entry(self.root, textvariable=self.var_course, font=(
            "times new roman", 20), bg='white', fg="black",state='readonly').place(x=600, y=220, width=320)
        txt_marks = Entry(self.root, textvariable=self.var_marks, font=(
            "times new roman", 20), bg='white', fg="black").place(x=600, y=280, width=320)
        txt_full_marks = Entry(self.root, textvariable=self.var_full_marks, font=(
            "times new roman", 20), bg='white', fg="black").place(x=600, y=340, width=320)  

        btn_add=Button(self.root,text="Submit",font=("times new roman",15),bg="black",fg="red",activebackground="black",cursor="hand2",command=self.add).place(x=620,y=420,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",font=("times new roman",15),bg="black",fg="red",activebackground="black",cursor="hand2",command=self.clear).place(x=750,y=420,width=120,height=35)
    
    #This fuction is used to get the courses in the COURSE COMBO BOX of STUDENT DETAILS
    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        # the above line is used to create an empty database
        cur = con.cursor()
        # the above line is used to execute the sql query
        try:
            cur.execute("select roll from student")
            rows = cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
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
                "select name, course from student where roll=?",(self.var_roll.get(),))
            row = cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
                
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        # the above TRY AND EXCEPT structure is used to DISPLAY the ERROR in MESSAGE BOX    

    #DISPLAY MESSAGE BOX based on the input given
    def add(self):
        con=sqlite3.connect(database="rms.db")
        #the above line is used to create an empty database

        cur=con.cursor()
        #the above line is used to execute the sql query

        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please search student record",parent=self.root)
                #the above line displays the ERROR in the ROOT WINDOW i.e., DASHBOARD

            else:
                per=(int(self.var_marks.get())*100)/int(self.var_full_marks.get())
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already exists",parent=self.root)
                else:
                    cur.execute("insert into result (roll,name,course,marks_ob,full_marks,per) values(?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result Added Successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        #the above TRY AND EXCEPT structure is used to DISPLAY the ERROR in MESSAGE BOX
    
    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")

if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()