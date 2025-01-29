from tkinter import* 
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):  # calling constructor
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION ATTENDANCE SYSTEM")

        title_lbl = Label(self.root, text="FACE DETECTITON", font=("TIMES NEW ROMAN", 16,"bold"), background="White", fg="DARK GREEN")
        title_lbl.place(x=0, y=0, width=1530, height=45)
       #image 1
        img_top=Image.open(r"D:\PYTHON\IMAGES COLLGE\faceee.jpg")
        img_top=img_top.resize((750,750), Image.BILINEAR)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=48,width=750,height=750)

        #image 2
        img_bottom=Image.open(r"D:\PYTHON\IMAGES COLLGE\man.jpg")
        img_bottom=img_bottom.resize((850,750), Image.BILINEAR)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=750,y=48,width=850,height=750)

        #button
        face_button= Button(f_lbl,text="FACE",cursor="hand2",command=self.face_recog,font=("TIMES NEW ROMAN",14,"bold"),background="white",fg="Red")
        face_button.place(x=392,y=680,width=100,height=25)


        # creating a  function

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,colors,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:y+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="yashrajkotia@123",database="face_recognition",auth_plugin = "mysql_native_password")
                my_cursor=conn.cursor()


                my_cursor.execute("select name from student where reg="+str(id))
                result=my_cursor.fetchone()[0]
                n=str(n)

                my_cursor.execute("select reg  from student where reg="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                if confidence>77:
                    cv2.putText(img,f"REG NO:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f" NAME:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Face not found",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome",img)
            

            if cv2.waitKey(1)==13:
              
              break
            
        video_cap.release()
        cv2.destroyAllWindows()



       



                    










if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()