#using tkinter library as it is used for making gui
from tkinter import* 
from tkinter import ttk
from PIL import Image, ImageTk

#creating class
class Face_Recognition_System:
    def __init__(self,root):#calling constructor
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION ATTENDANCE SYSTEM")



       #first image
        img=Image.open(r"D:\PYTHON\IMAGES COLLGE\vitbhopal.jpg")
        img=img.resize((500,130), Image.BILINEAR)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
      #second image
        img1=Image.open(r"D:\PYTHON\IMAGES COLLGE\blue.jpg")
        img1=img1.resize((500,130), Image.BILINEAR)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"D:\PYTHON\IMAGES COLLGE\blue.jpg")
        img2=img2.resize((550,130), Image.BILINEAR)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #background 
        img3=Image.open(r"D:\PYTHON\IMAGES COLLGE\white.jpg")
        img3=img3.resize((1530,710), Image.BILINEAR)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #creating a label for title 
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDACE SYSTEM",font=("TIMES NEW ROMAN",16),background="White",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #Student details/enteries(creating button for it using iamge)
        img4=Image.open(r"D:\PYTHON\IMAGES COLLGE\student.jpg")
        img4=img4.resize((220,220), Image.BILINEAR)
        self.photoimg4=ImageTk.PhotoImage(img4)

        #creating button 
        b1= Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        #btton with txt
        b1_1= Button(bg_img,text="STUDENT DETAILS",cursor="hand2",font=("TIMES NEW ROMAN",14),background="White",fg="black")
        b1_1.place(x=200,y=300,width=220,height=40)

        #face detection button and text

        img5=Image.open(r"D:\PYTHON\IMAGES COLLGE\face.jpg")
        img5=img5.resize((220,220), Image.BILINEAR)
        self.photoimg5=ImageTk.PhotoImage(img5)
     #creating button
        b2= Button(bg_img,image=self.photoimg5,cursor="hand2")
        b2.place(x=500,y=100,width=220,height=220)
        # button with text
        b2_1= Button(bg_img,text="FACE DETECTION",cursor="hand2",font=("TIMES NEW ROMAN",14),background="White",fg="black")
        b2_1.place(x=500,y=300,width=220,height=40)

        #ATTENDANCE BUTTON\
        img6=Image.open(r"D:\PYTHON\IMAGES COLLGE\atm.png")
        img6=img6.resize((220,220), Image.BILINEAR)
        self.photoimg6=ImageTk.PhotoImage(img6)
        #creating button
        b3= Button(bg_img,image=self.photoimg6,cursor="hand2")
        b3.place(x=800,y=100,width=220,height=220)
        # button with text
        b3_1= Button(bg_img,text="ATTENDANCE",cursor="hand2",font=("TIMES NEW ROMAN",14),background="White",fg="black")
        b3_1.place(x=800,y=300,width=220,height=40)

        #TRAIN FACE BUTTON
        img7=Image.open(r"D:\PYTHON\IMAGES COLLGE\train.png")
        img7=img7.resize((220,220), Image.BILINEAR)
        self.photoimg7=ImageTk.PhotoImage(img7)
       #creating button
        b4= Button(bg_img,image=self.photoimg7,cursor="hand2")
        b4.place(x=200,y=400,width=220,height=220)
        # button with text
        b4_1= Button(bg_img,text="TRAIN DATA",cursor="hand2",font=("TIMES NEW ROMAN",14),background="White",fg="black")
        b4_1.place(x=200,y=600,width=220,height=40)

         #PHOTO FACE BUTTON
        img8=Image.open(r"D:\PYTHON\IMAGES COLLGE\photo.jpg")
        img8=img8.resize((220,220), Image.BILINEAR)
        self.photoimg8=ImageTk.PhotoImage(img8)
         #creating button
        b5= Button(bg_img,image=self.photoimg8,cursor="hand2")
        b5.place(x=500,y=400,width=220,height=220)
        # button with text
        b5_1= Button(bg_img,text="PHOTOS",cursor="hand2",font=("TIMES NEW ROMAN",14),background="White",fg="black")
        b5_1.place(x=500,y=600,width=220,height=40)

        #EXIT BUTTON
        img9=Image.open(r"D:\PYTHON\IMAGES COLLGE\exx.png")
        img9=img9.resize((220,220), Image.BILINEAR)
        self.photoimg9=ImageTk.PhotoImage(img9)
 #creating button
        b6= Button(bg_img,image=self.photoimg9,cursor="hand2")
        b6.place(x=800,y=400,width=220,height=220)
# button with text
        b6_1= Button(bg_img,text="EXIT",cursor="hand2",font=("TIMES NEW ROMAN",14),background="White",fg="black")
        b6_1.place(x=800,y=600,width=220,height=40)


      
      






        


        




        
        
        
        
        
        

#this the object created for upper class
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()