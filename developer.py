from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",30,"bold"),bg="light yellow",fg="blue")
        title_lbl.place(x=0,y=0,width=1350,height=35)

        img_top=Image.open(r"1628243597666college-images\college_images\dev.jpg")
        img_top=img_top.resize((1350,720))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1350,height=720)

        # ==================frame=================
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=830,y=0,width=500,height=600)
        img_top1=Image.open(r"1628243597666college-images\college_images\Riya.png")
        img_top1=img_top1.resize((200,200))
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        # Developer info
        dev_label=Label(main_frame,text="Hello, My name is Riya Jaiswal.",font=("times new roman",15,"bold"),bg="white",fg="dark blue")
        dev_label.place(x=0,y=5)
        dev_label=Label(main_frame,text="I am a student of MCA(last sem).",font=("times new roman",15,"bold"),bg="white",fg="dark blue")
        dev_label.place(x=0,y=35)
        dev_label=Label(main_frame,text="I am junior Python Developer.",font=("times new roman",15,"bold"),bg="white",fg="dark blue")
        dev_label.place(x=0,y=65)
        img2=Image.open(r"1628243597666college-images\college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2=img2.resize((500,390),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        f_lbl=Label(main_frame,image=self.photoimage2)
        f_lbl.place(x=0,y=210,width=500,height=390)

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()