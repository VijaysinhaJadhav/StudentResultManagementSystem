from tkinter import*
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1500x800+0+0") #dashboard geometry(width,height,leftmost,rightmost)
        self.root.config(bg="white")

        #TITLE
        title=Label(self.root,text="Student Result Management System",font=("times new roman",20,"bold"),bg="black",fg="red").place(x=0,y=0,relwidth=1,height=50)
        #this above line is used to get the label SRMS^, font(font_style,size,bold), bg(background color), fg(foreground color), relwidth is used to get the same width as that of dashboard

        #MENU 
        M_Frame=LabelFrame(self.root, text="Menu",font=("times new roman",15),bg="white")
        M_Frame.place(x=60,y=150,width=1350,height=80)

        #BUTTON

        btn_course=Button(M_Frame,text="Course",font=("times new roman",15,"bold"),bg="black",fg="red",cursor="hand2",command=self.add_course).place(x=40,y=5,width=200,height=40)
        #(command=self.add_course) is used call add_course()
        btn_student=Button(M_Frame,text="Student",font=("times new roman",15,"bold"),bg="black",fg="red",cursor="hand2",command=self.add_student).place(x=380,y=5,width=200,height=40)
        #(command=self.add_student) is used to call add_student()
        btn_result=Button(M_Frame,text="Result",font=("times new roman",15,"bold"),bg="black",fg="red",cursor="hand2",command=self.add_result).place(x=720,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="View Student Result",font=("times new roman",15,"bold"),bg="black",fg="red",cursor="hand2",command=self.add_report).place(x=1040,y=5,width=200,height=40)
        #btn_logout=Button(M_Frame,text="Logout",font=("times new roman",15,"bold"),bg="black",fg="red",cursor="hand2").place(x=900,y=5,width=200,height=40)
        #btn_exit=Button(M_Frame,text="Exit",font=("times new roman",15,"bold"),bg="black",fg="red",cursor="hand2").place(x=1120,y=5,width=200,height=40)
        
        #UPDATE DETAILS
        # self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("times new roman",20),bd=10,relief=SUNKEN,bg="black",fg="red")
        # self.lbl_course.place(x=40,y=300,width=600,height=200)

        # self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",font=("times new roman",20),bd=10,relief=SUNKEN,bg="black",fg="red")
        # self.lbl_student.place(x=850,y=300,width=600,height=200)

        # self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("times new roman",20),bd=10,relief=SUNKEN,bg="black",fg="red")
        # self.lbl_result.place(x=450,y=550,width=600,height=200)

    #this add_course() is used to get the COURSE DETAILS interface when clicked on COURSE LABEL
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    #this add_student() is used to get the STUDENT DETAILS interface when clicked on STUDENT LABEL
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)   

    #this add_result() is used to get the RESULT DETAILS interface when clicked on RESULT LABEL
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)

    #this add_report() is used to get the VIEW STUDENT DETAILS interface when clicked on VIEW DETAILS LABEL
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)         



if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()

