
from tkinter import* 
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




#creating class
class Student:
    def __init__(self,root):#calling constructor
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION ATTENDANCE SYSTEM")

        #creating variables 

        self.var_Regno=StringVar()
        self.var_Name=StringVar()
        self.var_Email=StringVar()
        self.var_branch=StringVar()
        self.va_year=StringVar()

        #1st image
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
        title_lbl=Label(bg_img,text="STUDENT REGISTRATION DETAILS",font=("TIMES NEW ROMAN",16),background="White",fg="DARK GREEN")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #CREATING FRAME

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=0,width=5000,height=1000)

        #creating label frames
        #leftside label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="", font=("TIMES NEW ROMAN",12))
        Left_frame.place(x=0,y=0,width=850,height=1000)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text=" ACADEMIC DETAILS", font=("TIMES NEW ROMAN",12))
        current_course_frame.place(x=1,y=10,width=850,height=145)

        #BRANCH LABEL
        branch_label=Label(current_course_frame,text="BRANCH",font=("TIMES NEW ROMAN",12),bg="white")
        branch_label.grid(row=0,column=0,sticky=W)


       
        branch_combo=ttk.Combobox(current_course_frame,textvariable=self.var_branch,font=("TIMES NEW ROMAN",12),state="readonly")
        branch_combo["values"]=("Select","CSE CORE","CYBER","AIML","GAMING","ECE")
        branch_combo.current(0)
        branch_combo.grid(row=0,column=1)

        #SUBJECT
       ##subject_label=Label(current_course_frame,text="SUBJECT",font=("TIMES NEW ROMAN",12),bg="white")
       ##ssubject_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)
#
       ##subject_combo=ttk.Combobox(current_course_frame,font=("TIMES NEW ROMAN",12),state="readonly")
       ##subject_combo["values"]=("Select","MATHS","JAVA","c++")
        #ssubject_combo.current(0)
        #subject_combo.grid(row=0,column=3,sticky=W)

        #BATCH
        batch_label=Label(current_course_frame,text="BATCH",font=("TIMES NEW ROMAN",12),bg="white")
        batch_label.grid(row=1,column=0,padx=10,sticky=W)

        batch_combo=ttk.Combobox(current_course_frame,textvariable=self.va_year,font=("TIMES NEW ROMAN",12),state="readonly")
        batch_combo["values"]=("Select","2021","2022","2023")
        batch_combo.current(0)
        batch_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #student details/ information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text=" STUDENT INFORMATION ", font=("TIMES NEW ROMAN",12))
        class_Student_frame.place(x=1,y=150,width=850,height=250)
        #student name
        name_label=Label(class_Student_frame,text="NAME ",font=("TIMES NEW ROMAN",12),bg="white")
        name_label.grid(row=0,column=0,padx=10,sticky=W)

        # taking the entries
        Name_entry=ttk.Entry(class_Student_frame,textvariable=self.var_Name,width=20,font=(("Times new roman",12)))
        Name_entry.grid(row=0,column=1,padx=10,sticky=W)

        #gender
       #gender_label=Label(class_Student_frame,text="GENDER",font=("TIMES NEW ROMAN",12),bg="white")
       #ender_label.grid(row=0,column=2,padx=10,sticky=W)
       #ender_combo=ttk.Combobox(class_Student_frame,font=("TIMES NEW ROMAN",12),state="readonly")
       #gender_combo["values"]=("Select","MALE","FEMALE")
       #gender_combo.current(0)
       #gender_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #REGESTRATION NUMBER

        Regno_label=Label(class_Student_frame,text="REG NO",font=(("times new roman",12)))
        Regno_label.grid(row=1,column=0,padx=10,sticky=W)

        #taking entries
        reg_entry=ttk.Entry(class_Student_frame,textvariable=self.var_Regno,width=20,font=(("TIMES NEW ROMAN",12)))
        reg_entry.grid(row=1,column=1,padx=10,sticky=W)

        #EMAIL ADRESS 
        EMAIL_label=Label(class_Student_frame,text="EMAIL ID",font=(("times new roman",12)))
        EMAIL_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #taking entries
        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_Email,width=20,font=(("TIMES NEW ROMAN",12)))
        email_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        


        #RADIO BUTTONS
        self.var_radio1=StringVar()

        radiobutton1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="take photo",value="yes")
        radiobutton1.grid(row=3,column=0,padx=10,pady=25,sticky=W)

        

        radiobutton2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No",value="no")
        radiobutton2.grid(row=3,column=16,padx=10,sticky=W)

        #button frames
        bttn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white",width=150)
        bttn_frame.place(x=0,y=175,width=715,height=70)

        #save / submit button
        save=Button(bttn_frame,text="Save",command=self.add_data,width=15,font=(("TIMES NEW ROMAN",12)),bg="navy blue",fg="white")
        save.grid(row=0,column=0,)

        #update button

        update=Button(bttn_frame,text="Update",command=self.update_data,width=15,font=(("TIMES NEW ROMAN",12)),bg="navy blue",fg="white")
        update.grid(row=0,column=1,)

        #delete button

        delete=Button(bttn_frame,text="Delete",command=self.delete_data,width=15,font=(("TIMES NEW ROMAN",12)),bg="navy blue",fg="white")
        delete.grid(row=0,column=2,)

        #reset button

        reset=Button(bttn_frame,text="Reset",command=self.reset_data,width=15,font=(("TIMES NEW ROMAN",12)),bg="navy blue",fg="white")
        reset.grid(row=0,column=3,)

        #take photo sample

        takephoto=Button(bttn_frame,text="take photo",command=self.generate_data,width=15,font=(("TIMES NEW ROMAN",12)),bg="navy blue",fg="white")
        takephoto.grid(row=0,column=4,)

        #updatephoto
        
        updatephoto=Button(bttn_frame,text="Update Photo",width=15,font=(("TIMES NEW ROMAN",12)),bg="navy blue",fg="white")
        updatephoto.grid(row=0,column=5,)



        



        



                         

        

        
      








        







        #RIGHTSIDE LABEL
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="", font=("TIMES NEW ROMAN",12))
        Right_frame.place(x=740,y=0,width=1050,height=1000)

        #search system

        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text=" SEARCH", font=("TIMES NEW Roman",12))
        search_frame.place(x=0,y=0,width=850,height=150)

        Regno_label=Label(search_frame,text="REG NO ",font=(("times new roman",12)))
        Regno_label.grid(row=1,column=0,padx=10,sticky=W)  

        #taking entry of reg number

        rege_entry=ttk.Entry(search_frame,width=20,font=(("TIMES NEW ROMAN",12)))
        rege_entry.grid(row=1,column=1,padx=10,sticky=W)

        #creating button

        save=Button(search_frame,text="Save",width=5,font=(("TIMES NEW ROMAN",12)),bg="navy blue",fg="white")
        save.grid(row=1,column=3,)
        #show button
        show=Button(search_frame,text="Show All",width=6,font=(("TIMES NEW ROMAN",12)),bg="navy blue",fg="white")
        show.grid(row=1,column=4, padx=4)

        #create a table frame

        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="", font=("TIMES NEW Roman",12))
        table_frame.place(x=1,y=145,width=790,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient="horizontal")
        scroll_y=ttk.Scrollbar(table_frame,orient="vertical")

        self.student_table=ttk.Treeview(table_frame,column=("REGNO", "NAME","EMAIL","BATCH","BRANCH","PHOTO"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

       #creating heading for scrollings
        self.student_table.heading("REGNO",text="Reg no")
        self.student_table.heading("NAME",text="Name")
        self.student_table.heading("EMAIL",text="Email")
        self.student_table.heading("BATCH",text="BATCH")
        self.student_table.heading("BRANCH",text="BRANCH")
        self.student_table.heading("PHOTO",text="photo")

        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

  #-----------------------------------------------------------------
  #creating function to add data
     #creating function to add data
    def add_data(self):
       if self.var_Regno.get()=="" or self.var_Name.get()=="" or self.var_Email.get()=="":messagebox.showerror("Error","All Fields are Required",parent=self.root)

       else:
           try:
                  conn=mysql.connector.connect(host="localhost",user="root",password="yashrajkotia@123",database="face_recognition",auth_plugin = "mysql_native_password")
                  my_cursor=conn.cursor()
                  my_cursor.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s)",(self.var_Regno.get(),self.var_Name.get(),self.var_Email.get(),self.va_year.get(),self.var_branch.get(),self.var_radio1.get()))
                  conn.commit()
                  self.fetch_data()
                  conn.close()
                  messagebox.showinfo("Success","Data has been inserted successfully",parent=self.root)

           except Exception as e:
                     messagebox.showerror("Error",f"Error due to: {str(e)}",parent=self.root)

    #creating function to fetch data
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",user="root",password="yashrajkotia@123",database="face_recognition",auth_plugin = "mysql_native_password")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from student")
         data=my_cursor.fetchall()

         if len(data)!=0:
              self.student_table.delete(*self.student_table.get_children())
              for i in data:
                   self.student_table.insert("",END,values=i)
              conn.commit()
              conn.close()

    def get_cursor(self,event):
         cursor_focus=self.student_table.focus()
         content=self.student_table.item(cursor_focus)
         data=content["values"]
         self.var_Regno.set(data[0])
         self.var_Name.set(data[1])
         self.var_Email.set(data[2])
         self.va_year.set(data[3])
         self.var_branch.set(data[4])
         self.var_radio1.set(data[5])

         #creating update function

    def update_data(self):
          if self.var_Regno.get()=="" or self.var_Name.get()=="" or self.var_Email.get()=="":messagebox.showerror("Error","All Fields are Required",parent=self.root)
          else:
               try:
                    Upadate=messagebox.askyesno("Update","Do you want to update details",parent=self.root)
                    if Upadate>0:
                         conn=mysql.connector.connect(host="localhost",user="root",password="yashrajkotia@123",database="face_recognition",auth_plugin = "mysql_native_password")
                         my_cursor=conn.cursor()
                         my_cursor.execute("update student set reg=%s,name=%s,email=%s,batch=%s,branch=%s,photo=%s",(self.var_Regno.get(),self.var_Name.get(),self.var_Email.get(),self.va_year.get(),self.var_branch.get(),self.var_radio1.get()))
                    else:
                         if not Upadate:
                              return
                    messagebox.showinfo("SUCCESS","details updated",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
               except Exception as e:
                messagebox.showerror("Error",f"Error due to: {str(e)}",parent=self.root)

                #delete button
    def delete_data(self):
         if self.var_Regno.get()=="":
              messagebox.showerror("ERROR ","student reg no required",parent=self.root)
         else:
              try:
                   delete=messagebox.askyesno("Student delete page","do you want to delete details",parent=self.root)
                   if delete>0:
                        conn=mysql.connector.connect(host="localhost",user="root",password="yashrajkotia@123",database="face_recognition",auth_plugin = "mysql_native_password")
                        my_cursor=conn.cursor()
                        sql="delete from student where reg=%s"
                        val=(self.var_Regno.get(),)
                        my_cursor.execute(sql,val)

                   else:
                        if not delete:
                             return
                        
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("DELETED","details deleletd",parent=self.root)
              except Exception as e:
                messagebox.showerror("Error",f"Error due to: {str(e)}",parent=self.root)

                #reset button

    def reset_data(self):
         self.var_Regno.set(" ")
         self.var_Name.set(" ")
         self.var_Email.set(" ")
         self.va_year.set(" ")
         self.var_branch.set("")
         self.var_radio1.set("")

         #generate datset/ take photo

    def generate_data(self):
         if self.var_Regno.get()=="" or self.var_Name.get()=="" or self.var_Email.get()=="":messagebox.showerror("Error","All Fields are Required",parent=self.root)

         else:
              try:
                    conn=mysql.connector.connect(host="localhost",user="root",password="yashrajkotia@123",database="face_recognition",auth_plugin = "mysql_native_password")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                         id+=1
                    my_cursor.execute("update student set reg=%s,name=%s,email=%s,batch=%s,branch=%s,photo=%s",(self.var_Regno.get(),self.var_Name.get(),self.var_Email.get(),self.va_year.get(),self.var_branch.get(),self.var_radio1.get()))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()
              
              

                    #loading the predefined file 

                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    #function for cropping the image

                    def face_cropped(img):
                         gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                         faces=face_classifier.detectMultiScale(gray,1.3,5)
                         #scaling factor =1.3
                         #minimum neighbour =5

                         for(x,y,w,h) in faces:
                              face_cropped=img[y:y+h,x:x+w]
                              return face_cropped
                         
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                         ret,my_frame=cap.read()
                         if face_cropped(my_frame) is not None:
                              img_id+=1
                              face=cv2.resize(face_cropped(my_frame),(450,450))
                              face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                              file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                              cv2.imwrite(file_name_path,face)
                              cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                              cv2.imshow("CROPPED FACE",face)

                         if cv2.waitKey(1)==13 or int(img_id)==100:
                              break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data set complete ")
              except Exception as e:
               messagebox.showerror("Error",f"Error due to: {str(e)}",parent=self.root)

                    
                    
                    
                    

                    
                    



                   
                   
              
         
         



         

              

         


                          
                          

         

        



                               
                               














                                                                                                                                                                                                                                                                                                                 
        
if __name__=="__main__":
     root=Tk()
     obj=Student(root)
     root.mainloop()