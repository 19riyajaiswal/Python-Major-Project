from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from time import strftime
from datetime import datetime
import os 
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x790+0+0")
        self.root.title("Face Recognition System")

        # first image
        img=Image.open(r"1628243597666college-images\college_images\BestFacialRecognition.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimage)
        f_lbl.place(x=0,y=0,width=450,height=130)

        # second image
        img1=Image.open(r"1628243597666college-images\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=450,y=0,width=450,height=130)

        # third image
        img2=Image.open(r"1628243597666college-images\college_images\images.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=900,y=0,width=450,height=130)

        # background image
        img3=Image.open(r"1628243597666college-images\college_images\u.jpg")
        img3=img3.resize((1350,710),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=130,width=1350,height=710)
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1350,height=42)

        # =============time================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        lbl = Label(title_lbl, font = ('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        #================student details button===============
        img4=Image.open(r"1628243597666college-images\college_images\gettyimages-1022573162.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimage4,command=self.student_details,cursor="hand2")
        b1.place(x=130,y=80,width=200,height=180)
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=130,y=260,width=200,height=40) 

        #================detect face button===============
        img5=Image.open(r"1628243597666college-images\college_images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimage5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimage5,cursor="hand2",command=self.face_data)
        b1.place(x=430,y=80,width=200,height=180)
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=430,y=260,width=200,height=40)

        #================attendance button===============
        img6=Image.open(r"1628243597666college-images\college_images\report.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimage6=ImageTk.PhotoImage(img6)
        b1=Button(bg_img,image=self.photoimage6,cursor="hand2",command=self.attendance_data)
        b1.place(x=730,y=80,width=200,height=180)
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=730,y=260,width=200,height=40)

        #================Help button===============
        img7=Image.open(r"1628243597666college-images\college_images\help.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimage7=ImageTk.PhotoImage(img7)
        b1=Button(bg_img,image=self.photoimage7,cursor="hand2",command=self.help_data)
        b1.place(x=1030,y=80,width=200,height=180)
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1030,y=260,width=200,height=40)

        #================Train Data button===============
        img8=Image.open(r"1628243597666college-images\college_images\Train.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimage8=ImageTk.PhotoImage(img8)
        b1=Button(bg_img,image=self.photoimage8,cursor="hand2",command=self.train_data)
        b1.place(x=130,y=320,width=200,height=180)
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=130,y=500,width=200,height=40)

        #================photos button===============
        img9=Image.open(r"1628243597666college-images\college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimage9=ImageTk.PhotoImage(img9)
        b1=Button(bg_img,image=self.photoimage9,cursor="hand2",command=self.open_img)
        b1.place(x=430,y=320,width=200,height=180)
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=430,y=500,width=200,height=40)

        #================developer===============
        img10=Image.open(r"1628243597666college-images\college_images\dev.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimage10=ImageTk.PhotoImage(img10)
        b1=Button(bg_img,image=self.photoimage10,cursor="hand2",command=self.developer_data)
        b1.place(x=730,y=320,width=200,height=180)
        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=730,y=500,width=200,height=40)

        #================Exit button===============
        img11=Image.open(r"1628243597666college-images\college_images\exit.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimage11=ImageTk.PhotoImage(img11)
        b1=Button(bg_img,image=self.photoimage11,cursor="hand2",command=self.iExit)
        b1.place(x=1030,y=320,width=200,height=180)
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1030,y=500,width=200,height=40)

    def open_img(self):
        os.startfile("data")
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure want to exit from this project?",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

        # ===========Function buttons=================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)      
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()