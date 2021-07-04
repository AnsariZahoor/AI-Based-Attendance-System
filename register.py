import mysql.connector as connection
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from tkinter import font
from tkinter import*
import re



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("AI - Attendance System")
        self.root.iconbitmap('tkinter_image/myicon.ico')
        self.root.state('zoomed')
        self.root.config(bg="#EFEFF6")

        Font_btn = ('Ubuntu', 10)
        Sec_font = font.Font(family="@Microsoft YaHei UI",size=10,weight="bold")
        Sec_font2 = font.Font(family="@Microsoft YaHei UI",size=10)

        self.frame1=Frame(self.root,bg='#EFEFF6')
        self.frame1.place(x=150,y=50,width=1060,relheight=600)

        self.loginImg = PhotoImage(file="tkinter_image/register.png")
        loginlbl = Label(self.frame1,image=self.loginImg,bg='#EFEFF6').place(x=0,y=0,width=1060,height=600)
        
    
        self.text_username=Entry(self.frame1,font=Font_btn,bg="white",bd=0)
        self.text_username.place(x=55,y=198,width=568,height=25)
       
        self.text_email=Entry(self.frame1,font=Font_btn,bg="white",bd=0)
        self.text_email.place(x=55,y=297,width=260,height=25)

        self.text_contact=Entry(self.frame1,font=Font_btn,bg="white",bd=0)
        self.text_contact.place(x=363,y=298,width=260,height=25)

        self.text_password=Entry(self.frame1,show='*',font=Font_btn,bg="white",bd=0)
        self.text_password.place(x=55,y=410,width=260,height=25)

        self.text_cofp=Entry(self.frame1,show='*',font=Font_btn,bg="white",bd=0)
        self.text_cofp.place(x=363,y=410,width=260,height=25)
        
        btn_register=Button(self.frame1, text='Submit' ,font=Sec_font,fg="white",bg='#a4aadb',bd=0,cursor="hand2",activebackground='#a4aadb',command=self.checkEmail).place(x=245,y=491,width=185,height=32)
        btn_for=Button(self.frame1, text="Already have an account ",cursor="hand2" , font=Sec_font2,bd=0,bg='white',fg="black",activebackground='white',activeforeground='#a4aadb',command=self.login).place(x=233,y=540,width=190)
        
        self.regImg = PhotoImage(file="tkinter_image/arrow.png")
        reglbl = Label(self.frame1,image=self.regImg,bg='white').place(x=408,y=546)

    def checkEmail(self):
        Font_btn = ('Ubuntu', 10)
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if(re.search(regex, self.text_email.get())):
            self.register_data()
        else:
            messagebox.showerror("Error  :(","Please enter valid email id",parent=self.root)


    def login(self):
        self.root.destroy()
        import login


    def clear(self):
        self.text_username.delete(0,END),
        self.text_email.delete(0,END),
        self.text_contact.delete(0,END),
        self.text_password.delete(0,END),
        self.text_cofp.delete(0,END)
    


    def register_data(self):
        Font_btn = ('Ubuntu', 10)
        if self.text_username.get()=="" or self.text_contact.get()=="" or self.text_email.get()=="" or self.text_password.get()=="" or self.text_cofp.get()=="":
            messagebox.showerror("Error  :(","All fields are required",parent=self.root)
        elif len(self.text_contact.get()) != 10:
            messagebox.showerror("Error  :(","Please enter valid phone number",parent=self.root)
        elif self.text_password.get()!=self.text_cofp.get():
            messagebox.showerror("Error  :(","Password & Confirm Password does not match ",parent=self.root)
        else:
            try:
                con = connection.connect(host="localhost",user="root",database='logindb')
                cur=con.cursor()
    
                cur.execute("select * from login where username='"+self.text_username.get()+"'")
                row=cur.fetchone()
            
                if row!=None:
                    messagebox.showerror("Error  :(","This username is already taken",parent=self.root)
                else:
                    cur.execute("insert into login (username,email,phone_number,password) VALUES (%s,%s,%s,%s)",
                               (self.text_username.get(),
                                self.text_email.get(),
                                self.text_contact.get(),
                                self.text_password.get()
                               ))
                    con.commit()
                    con.close()     
                    messagebox.showinfo("Success  :)","Account created successfully",parent=self.root)
                    self.clear()
         
            except Exception as es:
                messagebox.showerror("Error  :(",f"Error due to: {str(es)},",parent=self.root)

            
root=Tk()           
obj=Register(root)
root.mainloop()
