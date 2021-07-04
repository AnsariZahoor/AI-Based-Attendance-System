from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time 
from tkinter import font
from math import *
from tkinter import messagebox,ttk
import mysql.connector as connection

class Login_window:

    def __init__(self,root):     
        rootColor = '#EFEFF6'
        FrameClr = '#0E0C28'
        BtnClr = '#242849'
        BtnTxtClr = '#a4aadb'

        self.root=root
        self.root.title("AI - Attendance System")
        self.root.iconbitmap('tkinter_image/myicon.ico')
        self.root.state('zoomed')
        self.root.configure(bg=rootColor)


        Font_btn = ('Ubuntu', 10)
        Sec_font = font.Font(family="@Microsoft YaHei UI",size=10,weight="bold")
        Sec_font2 = font.Font(family="@Microsoft YaHei UI",size=10)


        self.login_frame=Frame(self.root,bg=rootColor)
        self.login_frame.place(x=300,y=120,width=765,height=468)


        self.loginImg = PhotoImage(file="tkinter_image/login.png")
        loginlbl = Label(self.login_frame,image=self.loginImg).place(x=0,y=0,width=765,height=468)


        self.text_username=Entry(self.login_frame,font=Font_btn,bg="#F7F7F7",bd=0)
        self.text_username.place(x=510,y=150,width=190,height=30)


        self.text_password=Entry(self.login_frame,show='*',font=Font_btn,bg="#F7F7F7",bd=0)
        self.text_password.place(x=510,y=225,width=190,height=30)
        

        btn_login=Button(self.login_frame, text="LOGIN" , command=self.login, cursor="hand2",font=Sec_font,fg="white",bg='#a4aadb',bd=0,activebackground='#a4aadb').place(x=475,y=287,width=215,height=35)

        
        btn_for=Button(self.login_frame, text="Forget Password ?",cursor="hand2" ,command=self.forget_password_window, font=Sec_font2,bd=0,bg='White',fg="black",activebackground='white',activeforeground='#a4aadb').place(x=530,y=330)
        
        self.regImg = PhotoImage(file="tkinter_image/arrow.png")
        reglbl = Label(self.login_frame,image=self.regImg,bg='white').place(x=646,y=425)


        btn_reg=Button(self.login_frame, text="Create New Account ",cursor="hand2" ,command=self.register_window, font=Sec_font2,bg="white",bd=0,fg="black",activebackground='white',activeforeground='#a4aadb').place(x=510,y=420)
  
        self.lbl=Label(self.login_frame,bd=0)
        self.lbl.place(x=100,y=100,height=250,width=250)
        
        # self.working()

   
    def reset(self):
        self.text_new_username.delete(0,END)
        self.text_email.delete(0,END)
        self.text_phone.delete(0,END)
        self.text_new_password.delete(0,END)
   
    def reset_login(self):
        self.text_username.delete(0,END)
        self.text_password.delete(0,END)


    def forget_password(self):
        if (self.text_new_username.get()=="" or self.text_email.get()=="" or self.text_new_password.get()=="") and  (self.text_new_username.get()=="" or self.text_phone.get()=="" or self.text_new_password.get()==""):
            messagebox.showerror("Error  :(","Required fields are empty",parent=self.root2)
        else:
            try:
                con = connection.connect(host="localhost",user="root",database='logindb')
                # con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from login where username='"+self.text_new_username.get()+"' and email='"+self.text_email.get()+"' or phone_number='"+self.text_phone.get()+"'")
                row=cur.fetchone()
                if row==None:
                   messagebox.showerror("Error  :(","Username/Email/Phone number are invalid",parent=self.root2)
                else:
                   cur.execute("update login set password='"+self.text_new_password.get()+"' where username='"+self.text_new_username.get()+"'")
                   con.commit()
                   con.close()
                   self.reset()
                   self.root2.destroy()
                   messagebox.showinfo("Success  :)","Your password has been reset ",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error  :(","Database is not connected",parent=self.root2)
            
    def forget_password_window(self):
        if self.text_username.get()=="" :
            messagebox.showerror("Error  :(","Enter username to reset your password",parent=self.root)
        else:
            try:
                con = connection.connect(host="localhost",user="root",database='logindb')
                cur=con.cursor()
                cur.execute("select * from login where username='"+self.text_username.get()+"'")
                row=cur.fetchone()
                if row==None:
                   messagebox.showerror("Error  :(","Invalid username",parent=self.root)
                else:
                    con.close()
                    self.reset_login()
                    
                    self.root2=Toplevel()
                    self.root2.title("Forget password")
                    self.root2.geometry("350x500+680+120")
                    self.root2.config(bg="white")
                    self.root2.iconbitmap('tkinter_image/myicon.ico')
                    self.root2.resizable(False, False)
                    self.root2.focus_force()
                    self.root2.grab_set()

                                        
                    Sec_font = font.Font(family="@Microsoft YaHei UI",size=10,weight="bold")
                    Font_btn = ('Ubuntu', 10)

                    self.root2.forget = PhotoImage(file="tkinter_image/forget.png")
                    forgetlbl = Label(self.root2,image=self.root2.forget,bg='white').place(x=0,y=0,width=350,height=500)
          
                    self.text_new_username=Entry(self.root2,font=Font_btn,bg="#F7F7F7",bd=0)
                    self.text_new_username.place(x=90,y=115,width=215,height=29)
                            
                    self.text_email=Entry(self.root2,font=Font_btn,bg="#F7F7F7",bd=0)
                    self.text_email.place(x=90,y=197,width=215,height=29)
                            
                    self.text_phone=Entry(self.root2,font=Font_btn,bg="#F7F7F7",bd=0)
                    self.text_phone.place(x=90,y=282,width=215,height=29)
                            
                    self.text_new_password=Entry(self.root2,show='*',font=Font_btn,bg="#F7F7F7",bd=0)
                    self.text_new_password.place(x=90,y=366,width=215,height=29)

                    self.btn_forget=Button(self.root2, text="Reset" , cursor="hand2",command=self.forget_password,font=Sec_font,fg="white",bg='#a4aadb',bd=0,activebackground='#a4aadb').place(x=90,y=438,width=160,height=29)   

            except Exception as es:
                messagebox.showerror("Error  :(","Database is not connected",parent=self.root)
        
    def register_window(self):
        self.root.destroy()
        import register
       
    def splashScreen(self):
        self.root.destroy()
        import splashScreen
         

    def login(self):
        if self.text_username.get()=="" or self.text_password.get()=="":
            messagebox.showerror("Error  :(","Enter username or password",parent=self.root)
        else:
            try:
                con = connection.connect(host="localhost",user="root",database='logindb')
                cur=con.cursor()
                cur.execute("select * from login where username='"+self.text_username.get()+"' and password='"+self.text_password.get()+"'")
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error  :(","Invalid username & password",parent=self.root)         
                else:
                    con.close()
                    self.splashScreen()
            except Exception as es:
                messagebox.showerror("Error  :(","Database is not connected",parent=self.root)
            

    def clock_image(self,hr,min_,sec_):
        clock=Image.new('RGB',(250,250),(255,255,255))
        draw=ImageDraw.Draw(clock)

        bg=Image.open("tkinter_image/clock.png")
        clock.paste(bg,(0,0))

        origin=125,125
       
        # hours
        # draw.line((125,125,150,100),fill="white",width=2)
        draw.line((origin,125+40*sin(radians(hr)),125-40*cos(radians(hr))),fill="white",width=3)

        # minutes
        draw.line((origin,125+90*sin(radians(min_)),125-90*cos(radians(min_))),fill="white",width=1)
        # draw.line((125,125,200,180),fill="white",width=1)

        # second
        draw.line((origin,125+65*sin(radians(sec_)),125-65*cos(radians(sec_))),fill="white",width=1)
        # draw.line((125,125,150,180),fill="white",width=1)
 
        draw.ellipse((122,122,127,127),fill="#2C302F")

        clock.save("tkinter_image/clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        #print(h,m,s)
        #print(hr,min_,sec_)
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="tkinter_image/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)



    

root=Tk()
obj=Login_window(root)
obj.working()
root.mainloop()
