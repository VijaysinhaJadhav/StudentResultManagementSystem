from tkinter import*
from tkinter import ttk, messagebox
#the above line is used to CREATE TABLE

import sqlite3
#the above line is used for database withour installing external software

class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x580+80+170") #dashboard geometry(width,height,leftmost,rightmost)
        self.root.config(bg="white")
        self.root.focus_force()
        #the above line is used so that the user need not click on the Course Details interface to make it responsive

        #TITLE
        title=Label(self.root,text="Manage Course Details",font=("times new roman",20,"bold"),bg="black",fg="red").place(x=10,y=15,width=1330,height=35)

        #VARIABLES --> these variables are used to store the data present in text fields of Course Details
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_fees=StringVar()
        
        #WIDGETS(LABEL)
        lbl_courseName=Label(self.root,text="Course Name",font=("times new roman",15,'bold'),bg='white',fg="red").place(x=10,y=60)
        lbl_duration=Label(self.root,text="Duration",font=("times new roman",15,'bold'),bg='white',fg="red").place(x=10,y=100)
        lbl_fees=Label(self.root,text="Fees",font=("times new roman",15,'bold'),bg='white',fg="red").place(x=10,y=140)
        lbl_description=Label(self.root,text="Description",font=("times new roman",15,'bold'),bg='white',fg="red").place(x=10,y=180)
        
        #ENTRY(TEXT) FIELDS
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("times new roman",15),bg='white',fg="black")
        self.txt_courseName.place(x=150,y=60,width=200)
        txt_duration=Entry(self.root,textvariable=self.var_duration,font=("times new roman",15),bg='white',fg="black").place(x=150,y=100,width=200)
        txt_fees=Entry(self.root,textvariable=self.var_fees,font=("times new roman",15),bg='white',fg="black").place(x=150,y=140,width=200)
        self.txt_description=Text(self.root,font=("times new roman",15),bg='white',fg="black")
        self.txt_description.place(x=150,y=180,width=500,height=130)
        #Entry allows you to input data into textfield but, you can not jump to next line
        #Text is same as Entry but, here you can jump into multiple lines 

        #BUTTONS
        self.btn_add=Button(self.root,text='Save',font=("times new roman",15,"bold"),bg="black",fg="red",cursor="hand2",command=self.add)
        #(command=self.add) is used to access the add()
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text='Update',font=("times new roman",15,"bold"),bg="black",fg="red",cursor="hand2",command=self.update)
        #(command=self.update) is used to access the update()
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text='Delete',font=("times new roman",15,"bold"),bg="black",fg="red",cursor="hand2",command=self.delete)
        #(command=self,delete) is used to access the delete()
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text='Clear',font=("times new roman",15,"bold"),bg="black",fg="red",cursor="hand2",command=self.clear)
        #(command=self.clear) is used to access the clear()
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        #SEARCH PANEL
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Search By Course",font=("times new roman",15),bg='white',fg="black").place(x=720,y=60)
        txt_search_courseName=Entry(self.root,textvariable=self.var_search,font=("times new roman",15),bg='white',fg="black").place(x=900,y=60,width=180)
        btn_search=Button(self.root,text='Search',font=("times new roman",15),bg="green",fg="black",cursor="hand2",command=self.search).place(x=1120,y=60,width=150,height=28)

        #FRAME OF SEARCH COURSE DETAILS
        self.C_Frame=Frame(self.root,bd=2,relief=RAISED)
        self.C_Frame.place(x=720,y=100,width=550,height=400)
        
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        #the above lines are used to get the SCROLL BARS

        #TABLE OF SEARCH COURSE DETAILS 
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","fees","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        #the above line creates the HEADING COLUMNS FOR THE TABLE with an ADDITIONAL COLUMN in the beginning

        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        #the above lines are used make the SCROLL BAR WORK

        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("fees",text="Fees")
        self.CourseTable.heading("description",text="Description")
        #the above five lines are used to input COLUMN NAMES AS HEADINGS

        self.CourseTable["show"]='headings'
        #the above line HIDES the ADDITIONAL COLUMN

        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("fees",width=100)
        self.CourseTable.column("description",width=150)
        #the above lines set the width of COLUMNS

        self.CourseTable.pack(fill=BOTH,expand=1)
        #the above line is used to create the TRABLE with same width and height as that of FRAME

        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        #the above line is used to get the data in the TEXT FIELD of the COURSE DETAILS from the DATABASE
        self.show()

    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_fees.set("")
        self.var_search.set("")
        #the above line is used to CLEAR the SEARCH TEXTFIELD

        self.txt_description.delete('1.0',END)  
        self.txt_courseName.config(state=NORMAL) 

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        #the above line is used to create an empty database

        cur=con.cursor()
        #the above line is used to execute the sql query

        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Please provide Course Name",parent=self.root)
                #the above line displays the ERROR in the ROOT WINDOW i.e., DASHBOARD

            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select the course from the List",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete it?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")        


    #FUCTION TO FETCH the data from DATABASE to the COURSE DETAILS TEXTFIELD
    def get_data(self,ev):
        self.txt_courseName.config(state='readonly')
        #the above line does not allow the user to UPDATE the COURSE NAME 
        self.txt_courseName
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_fees.set(row[3])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])


    #DISPLAY MESSAGE BOX based on the input given
    def add(self):
        con=sqlite3.connect(database="rms.db")
        #the above line is used to create an empty database

        cur=con.cursor()
        #the above line is used to execute the sql query

        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Please provide Course Name",parent=self.root)
                #the above line displays the ERROR in the ROOT WINDOW i.e., DASHBOARD

            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course Name already exists",parent=self.root)
                else:
                    cur.execute("insert into course (name,duration,fees,description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_fees.get(),
                        self.txt_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        #the above TRY AND EXCEPT structure is used to DISPLAY the ERROR in MESSAGE BOX

    def update(self):
        con=sqlite3.connect(database="rms.db")
        #the above line is used to create an empty database

        cur=con.cursor()
        #the above line is used to execute the sql query

        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Please provide Course Name",parent=self.root)
                #the above line displays the ERROR in the ROOT WINDOW i.e., DASHBOARD

            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Course from list",parent=self.root)
                else:
                    cur.execute("update course set duration=?,fees=?,description=? where name=?",(
                        self.var_duration.get(),
                        self.var_fees.get(),
                        self.txt_description.get("1.0",END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        #the above TRY AND EXCEPT structure is used to DISPLAY the ERROR in MESSAGE BOX    
    
    def show(self):
        con=sqlite3.connect(database="rms.db")
        #the above line is used to create an empty database

        cur=con.cursor()
        #the above line is used to execute the sql query

        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)     
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        #the above TRY AND EXCEPT structure is used to DISPLAY the ERROR in MESSAGE BOX

    def search(self):
        con=sqlite3.connect(database="rms.db")
        #the above line is used to create an empty database

        cur=con.cursor()
        #the above line is used to execute the sql query

        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)     
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        #the above TRY AND EXCEPT structure is used to DISPLAY the ERROR in MESSAGE BOX    
           

    

if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()


           

