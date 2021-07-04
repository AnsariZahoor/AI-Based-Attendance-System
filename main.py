import mysql.connector as connection

from tkinter import ttk,simpledialog,filedialog, messagebox
from tkinter.filedialog import askopenfilename, askopenfile 
from tkinter.ttk import Progressbar
import tkinter.messagebox as tmsg
from tkinter import font
from tkinter import *

from datetime import datetime
from datetime import date
from time import strftime
from time import time
import time

from PIL import ImageTk, Image 
import pandas as pd
import smtplib
import csv
import os


# ======================================================================================================================

def main_window():
    root.destroy()
    import login

def topFtime():
    string = strftime('%I:%M:%S')
    stringp = strftime(' %p')
    curr_time.config(text = string)
    curr_timee.config(text = stringp)
    curr_time.after(1000,topFtime)

def topFdate():
    string = strftime('%d %b %Y')
    curr_date.config(text = string)
    curr_date.after(1000,topFdate)


# ================================================ New Enrolmnet 1 ======================================================================
# ================================================ New Enrolmnet 1 ======================================================================
# ================================================ New Enrolmnet 1 ======================================================================

import cv2

def capImg():
    statusvar.set("Capture photo of a student")

    className = []
    images = []
    path= "Image_Dataset"
    ClassNamelst = ['fy','FY','fY','Fy','sy','SY','sY','Sy','TY','ty','Ty','tY']
    
    file_path = simpledialog.askstring("","Enter class FY/SY/TY : ")

    if file_path == "" or file_path == None or file_path not in ClassNamelst:
        messagebox.showerror('Error  :(','Invalid Class Name')

    else :

        myList = os.listdir(f'{path}/{file_path}')

        for cl in myList: 
            #cls is name of img
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            #First element of img
            className.append(os.path.splitext(cl)[0])

        student_name = simpledialog.askstring("","Enter student name ( Format : 'rollno name' ) ")

        if student_name == '' or student_name == None :
            messagebox.showerror('Error  :(','Student name not entered')

        elif student_name in className :
            messagebox.showerror('Error  :(',f'{student_name} already exist')
        
        else : 
            try :
                studentRollnoType = student_name[:2].isdigit()
                studentNameType = student_name[3:].isdigit()

                if  studentRollnoType is False  or  studentNameType  is True :
                        messagebox.showerror('Error  :(',f'Invalid student name {student_name} ')
                else :

                    cam = cv2.VideoCapture(0)

                    while (student_name):
                        ret, frame = cam.read()
                        if not ret:
                            messagebox.showerror('Error  :(','Something went worng !')
                            break
                        cv2.imshow("Take a snapshot", frame)

                        if cv2.waitKey(1) & 0xFF==ord('s'):
                            # Press 's' to Stop
                            break
                        elif cv2.waitKey(1) & 0xFF==ord('c'):
                            img_name = f"Image_Dataset/{file_path}/{student_name}.png"
                            cv2.imwrite(img_name, frame)
                            messagebox.showinfo('Success  :)',f'{student_name} added to {file_path} class ')
                            break

                    cam.release()
                    cv2.destroyAllWindows()
                    statusvar.set("Ready...")

            except Exception as es :
                messagebox.showerror("Error",f"Error due to: {str(es)}")

    statusvar.set("Ready...")

# -----------

def openImg():
    statusvar.set("File explorer has open")
    
    file = askopenfile(initialdir="Image_Dataset/",mode ='r', filetypes =[('Image Files', '*.png'),('Image Files', '*.jpg')]) 
    
    if file is not None:
        statusvar.set("You can't select any file")
        tmsg.showwarning('','View mode only')
    
    statusvar.set("Ready...")

# -------------

import shutil 
def resetCopyFile():
    newEnF2.destinationText.delete(0,END)
    newEnF2.sourceText.delete(0,END)
  
def resetCopyFileS():
    newEnF2.sourceText.delete(0,END)
  
def resetCopyFileCN():
    newEnF2.destinationText.delete(0,END)
  
def NewEnrol_className():
    resetCopyFileCN()
    try :
        ClassNamelst = ['fy','FY','fY','Fy','sy','SY','sY','Sy','TY','ty','Ty','tY']
        file_path = simpledialog.askstring("","Select Class FY/SY/TY : ")
        if file_path == "" or file_path is None or file_path not in ClassNamelst:
            messagebox.showerror('Error  :(','Invalid Class Name')
        else:
            destinationdirectory = f'Image_Dataset//{file_path}'
            newEnF2.destinationText.insert('1', destinationdirectory) 
            statusvar.set(destinationdirectory)
    except:
        messagebox.showerror("Error  :(", "File not selected")
    finally :
        statusvar.set("Ready...")     

def NewEnrol_SourceBrowse():
    resetCopyFileS()
    statusvar.set("File explorer has open. Select student image")

    newEnF2.files_list = list(filedialog.askopenfilenames(initialdir ="/",       title="Select A File",
                                            filetype=(("Image files", "*.png"),("Image files", "*.jpg"))))
    if  newEnF2.files_list == '' or newEnF2.files_list == None :
        messagebox.showerror("Error  :(", "File not selected")
        statusvar.set("Ready...")
    else :
        try :
            newEnF2.sourceText.insert('1', newEnF2.files_list)
            statusvar.set(newEnF2.files_list)
        except:
            messagebox.showerror("Error  :(", "File not selected")
        finally :
            statusvar.set("Ready...")   

def NewEnrol_CopyFile():
    try :
        files_list = newEnF2.files_list
        destination_location = destinationLocation.get()
        for f in files_list:
            shutil.copy(f, destination_location)
        
        messagebox.showinfo('Success  :)',"Photo has been uploaded successfully")
        resetCopyFile()
        statusvar.set("Ready...") 
    except:
        messagebox.showerror("Error  :(", "File not selected")
        statusvar.set("Ready...") 

# -------------

def display_img():
    statusvar.set("Window has open to view image")

    def open_img(): 
        # Select the Imagename from a folder
        global x 
        x = openfilename() 

        # opens the image 
        img = Image.open(x) 
        
        # resize the image and apply a high-quality down sampling filter 
        img = img.resize((450, 450), Image.ANTIALIAS) 

        # PhotoImage class is used to add image to widgets, icons etc 
        img = ImageTk.PhotoImage(img) 

        # create a label 
        panel = Label(img_window, image = img) 
        
        # set the image as img 
        panel.image = img 
        panel.place(x=50,y=70)

    def openfilename():
        filename = filedialog.askopenfilename(initialdir="Image_Dataset/", filetypes =[('Image Files', '*.png'),('Image Files', '*.jpg')])  
        return filename

    def delfile():
        
        global x 

        try :
            res=messagebox.askquestion('Delete Image', 'Do you really want to delete ?',parent=img_window)
            if res == 'yes' :
                os.remove(x)
                messagebox.showinfo('Success  :)',f"{x} has been deleted")
                window()
            else :
                pass
        except :
            tmsg.showerror('Error  :(','File not selected')
            


    def window():
        img_window.destroy()
        statusvar.set("Ready...")

    img_window = Toplevel(root)
    img_window.title("Image")
    img_window.geometry("550x550+400+100") 
    img_window.iconbitmap('tkinter_image/icon2.ico')
    img_window.config(bg="#EFEFF6")
    img_window.focus_force()
    img_window.grab_set() 
    img_window.resizable(0,0)

    Openbtn = Button(img_window, text ='Open image',bg="#a4aadb",fg='black',bd=0,cursor="hand2", command = open_img).place(x=150,y=20,width=80,height=25)
    delBtn = Button(img_window, text ='Delete',bg="#a4aadb",fg='red',bd=0,cursor="hand2", command = delfile).place(x=250,y=20,width=80,height=25)
    Xbtn = Button(img_window, text ='Exit',bg="red",fg='white',bd=0,cursor="hand2", command = window).place(x=350,y=20,width=80,height=25)

# ================================================ Mark Attendance 2 ======================================================================
# ================================================ Mark Attendance 2 ======================================================================
# ================================================ Mark Attendance 2 ======================================================================


from attendence import start,startByTime
import time

def markAtt():
    statusvar.set("Ready to Mark Attendance")
    if timeValue.get() == '1':
        startByTime()
    else :
        start()  
    statusvar.set("Ready...")


def mark_openCSV():
    statusvar.set("File explorer has open")
    file = askopenfile(initialdir="Attendance_Files/",mode ='r', filetypes =[('CSV Files', '*.csv')]) 
    if file is not None:
        statusvar.set("You can't select any file")
        tmsg.showwarning('','View mode only')
    statusvar.set("Ready...")


def mark_browseFile():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    statusvar.set("File explorer has open")
    
    global filename
    filename = filedialog.askopenfilename(initialdir="Attendance_Files",
                                            title="Select A File",
                                            filetype=(("CSV files", "*.csv"),("All Files", "*.*")))
    if  filename == '' or filename == None :
        messagebox.showerror("Error  :(", "File not selected")
        statusvar.set("Ready...")
    else :
        try:
            label_file["text"] = filename
            statusvar.set(os.path.basename(filename))
            return None
        except:
            messagebox.showerror("Error  :(", "Something went wrong !")


def mark_LoadCSV():
    """If the file selected is valid this will load the file into the Treeview"""
    file_path = label_file["text"]

    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        messagebox.showerror("Error  :(", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        messagebox.showerror("Error  :(", "File does not exist")
        return None

    statusvar.set('Ready..')

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None


def clear_data():
    tv1.delete(*tv1.get_children())
    statusvar.set('Ready...')
    return None

def mark_sort():
    try :
        data = pd.read_csv(filename) 
        #sorting data frame by Team and then By names 
        data.sort_values(["Rollno"], axis=0, ascending=True, inplace=True)
    except:
        messagebox.showerror("Error  :(", "File has not selected !")


    clear_data()
    tv1["column"] = list(data.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

    data_rows = data.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in data_rows:
        tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None
    statusvar.set("Ready...")

def mark_absentStud():
    try:      
        global filename
        data = pd.read_csv(filename)
        ClassNamelst = ['fy','FY','fY','Fy','sy','SY','sY','Sy','TY','ty','Ty','tY']
        class_name = simpledialog.askstring("","Enter Class FY/SY/TY: ")
        if class_name is None or class_name == '' or class_name not in ClassNamelst:
            messagebox.showerror('Error  :(','Invalid Class Name')
        else :
            studRecords = pd.read_csv(f'Student_Records/{class_name}.csv')
            studRecords = studRecords['Rollno'].to_list()
            Totalstuds = len(studRecords)
            roll_col = data['Rollno'].to_list()
            if class_name == 'FY' or class_name == 'fy' :
                roll_col.append(Totalstuds+1)
            elif class_name == 'SY' or class_name == 'sy':
                roll_col.append(Totalstuds+1)
            else :
                roll_col.append(Totalstuds+1)

            missing_value = [ele for ele in range(max(roll_col)+1) if ele not in roll_col]
            missing_len = len(missing_value[1:])
            statusvar.set(f'No. of absent students : {missing_len}')
            tmsg.showinfo('Absent',f'Absent students : {missing_value[1:]}')
            statusvar.set('Ready...')
    except :
        messagebox.showerror("Error  :(", "File not selected")

def mark_delFile(): 
    global filename
    try :
        if os.path.exists(filename) and os.path.isfile(filename) :
            res=messagebox.askquestion('Delete file', 'Do you really want to delete ?')
            statusvar.set(f'{filename}')
            if res == 'yes' :
                os.remove(filename) 
                statusvar.set(f'File has been deleted {filename}')
                label_file["text"] = ''
                clear_data()
                tmsg.showinfo('Success  :)','File deleted successfully...')
                statusvar.set('Ready...')
            else:
                pass
        else:
            messagebox.showerror('Error  :(','File not found')
    except :
        messagebox.showerror('Error  :(','File not found')
    



def UploaddbFy():
    global filename
    statusvar.set("Upload Attendance records")
    def uploadCSVdb():     
        try :
            data = pd.read_csv (filename)   
            df = pd.DataFrame(data, columns= ['Rollno','Name','Time'])

            # Connect to SQL Server
            db = connection.connect(host="localhost",user="root",database='fy')
            cursor = db.cursor()

            if fyDB.get() == 1 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO imperative_programming (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name,row.Time))
            elif  fyDB.get() == 2 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO digital_electronic (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name,row.Time))
            elif  fyDB.get() == 3 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO operating_system (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name,row.Time))
            elif  fyDB.get() == 4 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO discrete_mathematics (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name,row.Time))
            elif  fyDB.get() == 5 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO communication_skills (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name, row.Time))
            elif  fyDB.get() == 6 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO oops (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name, row.Time))
            elif  fyDB.get() == 7 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO microprocessor_architecture (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name, row.Time))
            elif  fyDB.get() == 8 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO web_programming (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name, row.Time))
            elif  fyDB.get() == 9 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO numStat_methods (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name, row.Time))
            elif  fyDB.get() == 10:
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO green_computing (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name, row.Time))
                    
            db.commit()
            db.close()

            mrrwindow()
            tmsg.showinfo('Success  :)','File has been uploaded successfully')
            statusvar.set("Ready...")

        except  :
            mrrwindow()
            messagebox.showerror('Error  :(','Database is not connected / File not selected')
            statusvar.set("Ready...")

    def mrrwindow():
        mrr_window.destroy()
        statusvar.set("Ready...")

    mrr_window = Toplevel(root)
    mrr_window.title("Subjects")
    mrr_window.geometry("600x300+5+100")
    mrr_window.iconbitmap('tkinter_image/icon2.ico') 
    mrr_window.config(bg="#EFEFF6")
    mrr_window.resizable(0,0)
    mrr_window.focus_force()
    mrr_window.grab_set()
    pri1Font = font.Font(family="@Microsoft YaHei UI",size=10,weight="bold") 
    pri2Font = font.Font(family="@Microsoft YaHei UI",size=15) 
    secFont = ('Ubuntu', 10)

    frame1=Frame(mrr_window,bg="#EFEFF6")
    frame1.place(x=0,y=0,relwidth=1,relheight=1)
        
    title=LabelFrame(frame1,text=" First Year ",font=pri1Font,fg="#0E0C28",bg="#EFEFF6").place(x=10,y=10,width=580,height=280)

    sem1=Label(frame1,text="Semester 1",font=pri2Font,fg="#242849",bg="#EFEFF6").place(x=20,y=55)
    sem2=Label(frame1,text="Semester 2",font=pri2Font,fg="#242849",bg="#EFEFF6").place(x=20,y=145)
        
    fyDB =IntVar()
 
    Chk1=Checkbutton(frame1,text="Imp prog",variable=fyDB,onvalue=1,offvalue=0,font=secFont,bg="#EFEFF6").place(x=20,y=90)
    Chk2=Checkbutton(frame1,text="Digital elec...",variable=fyDB,onvalue=2,offvalue=0,font=secFont,bg="#EFEFF6").place(x=120,y=90)
    Chk3=Checkbutton(frame1,text="Opersting sys..",variable=fyDB,onvalue=3,offvalue=0,font=secFont,bg="#EFEFF6").place(x=240,y=90)
    Chk4=Checkbutton(frame1,text="Disc Maths",variable=fyDB,onvalue=4,offvalue=0,font=secFont,bg="#EFEFF6").place(x=360,y=90)
    Chk5=Checkbutton(frame1,text="Comm skills",variable=fyDB,onvalue=5,offvalue=0,font=secFont,bg="#EFEFF6").place(x=480,y=90)
                
    Chk6=Checkbutton(frame1,text="OOPs",variable=fyDB,onvalue=6,offvalue=0,font=secFont,bg="#EFEFF6").place(x=20,y=180)
    Chk7=Checkbutton(frame1,text="Micro Arch...",variable=fyDB,onvalue=7,offvalue=0,font=secFont,bg="#EFEFF6").place(x=120,y=180)
    Chk8=Checkbutton(frame1,text="Web prog...",variable=fyDB,onvalue=8,offvalue=0,font=secFont,bg="#EFEFF6").place(x=240,y=180)
    Chk9=Checkbutton(frame1,text="Num&Stat M. ",variable=fyDB,onvalue=9,offvalue=0,font=secFont,bg="#EFEFF6").place(x=360,y=180)
    Chk10=Checkbutton(frame1,text="Green Com...",variable=fyDB,onvalue=10,offvalue=0,font=secFont,bg="#EFEFF6").place(x=480,y=180)
        
    btn_upload=Button(frame1, text='Upload',bg="#a4aadb",fg='black',bd=0,cursor="hand2",command=uploadCSVdb).place(x=220,y=250,width=80,height=25)

    btn_exit=Button(frame1, text='Cancel' ,bg="red",fg='white',bd=0,cursor="hand2",command=mrrwindow).place(x=320,y=250,width=80,height=25)

def UploaddbSy():
    global filename
    statusvar.set("Upload Attendance Records")
    def uploadCSVdb():
        try :      
            data = pd.read_csv (filename)   
            df = pd.DataFrame(data, columns= ['Rollno','Name','Time'])

            # Connect to SQL Server
            db = connection.connect(host="localhost",user="root",database='sy')
            cursor = db.cursor()
            # Insert DataFrame to Table
            if syDB.get() == 1 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO python (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name,row.Time))
            elif  syDB.get() == 2 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO data_structures (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name,row.Time))
            elif  syDB.get() == 3 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO computer_networking (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name,row.Time))
            elif  syDB.get() == 4 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO dbms (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name,row.Time))
            elif  syDB.get() == 5 :
                for row in df.itertuples():
                        cursor.execute(f'''INSERT INTO maths (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name,row.Time))
            elif  syDB.get() == 6 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO java (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name,row.Time))
            elif  syDB.get() == 7 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO embedded_system (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name,row.Time))
            elif  syDB.get() == 8 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO cost (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name,row.Time))
            elif  syDB.get() == 9 :
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO software_engineering (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name,row.Time))
            elif  syDB.get() == 10:
                for row in df.itertuples():
                    cursor.execute(f'''INSERT INTO cga (Rollno, Name, Time)VALUES (%s,%s,%s)''',(row.Rollno, row.Name,row.Time))
                
            db.commit()
            db.close()
            
            mrrwindow()
            tmsg.showinfo('Success  :)','File has been uploaded successfully')
            statusvar.set("Ready...")

        except  :
            mrrwindow()
            messagebox.showerror('Error  :(','Database is not connected/File not selected')
            statusvar.set("Ready...")
            
    def mrrwindow():
        mrr_window.destroy()
        statusvar.set("Ready...")

    mrr_window = Toplevel(root)
    mrr_window.title("Subjects")
    mrr_window.geometry("600x300+5+100")
    mrr_window.iconbitmap('tkinter_image/icon2.ico')
    mrr_window.config(bg="#EFEFF6")
    mrr_window.resizable(0,0)
    mrr_window.focus_force()
    mrr_window.grab_set()

    pri1Font = font.Font(family="@Microsoft YaHei UI",size=10,weight="bold") 
    pri2Font = font.Font(family="@Microsoft YaHei UI",size=15) 
    secFont = ('Ubuntu', 10)

    frame1=Frame(mrr_window,bg="#EFEFF6")
    frame1.place(x=0,y=0,relwidth=1,relheight=1)
        

    title=LabelFrame(frame1,text=" Second Year ",font=pri1Font,fg="#0E0C28",bg="#EFEFF6").place(x=10,y=10,width=580,height=280)

    sem1=Label(frame1,text="Semester 3",font=pri2Font,fg="#242849",bg="#EFEFF6").place(x=20,y=55)
    sem2=Label(frame1,text="Semester 4",font=pri2Font,fg="#242849",bg="#EFEFF6").place(x=20,y=145)
        
    syDB =IntVar()
 
    Chk=Checkbutton(frame1,text="Python",variable=syDB,onvalue=1,offvalue=0,font=secFont,bg="#EFEFF6").place(x=20,y=90)
    Chk=Checkbutton(frame1,text="Data structures",variable=syDB,onvalue=2,offvalue=0,font=secFont,bg="#EFEFF6").place(x=120,y=90)
    Chk=Checkbutton(frame1,text="Computer net..",variable=syDB,onvalue=3,offvalue=0,font=secFont,bg="#EFEFF6").place(x=240,y=90)
    Chk=Checkbutton(frame1,text="DBMS",variable=syDB,onvalue=4,offvalue=0,font=secFont,bg="#EFEFF6").place(x=360,y=90)
    Chk=Checkbutton(frame1,text="Maths",variable=syDB,onvalue=5,offvalue=0,font=secFont,bg="#EFEFF6").place(x=480,y=90)
        
        
    Chk=Checkbutton(frame1,text="Java",variable=syDB,onvalue=6,offvalue=0,font=secFont,bg="#EFEFF6").place(x=20,y=180)
    Chk=Checkbutton(frame1,text="Embedded sys.",variable=syDB,onvalue=7,offvalue=0,font=secFont,bg="#EFEFF6").place(x=120,y=180)
    Chk=Checkbutton(frame1,text="COST",variable=syDB,onvalue=8,offvalue=0,font=secFont,bg="#EFEFF6").place(x=240,y=180)
    Chk=Checkbutton(frame1,text="Software Eng",variable=syDB,onvalue=9,offvalue=0,font=secFont,bg="#EFEFF6").place(x=360,y=180)
    Chk=Checkbutton(frame1,text="CG & A",variable=syDB,onvalue=10,offvalue=0,font=secFont,bg="#EFEFF6").place(x=480,y=180)
        
    btn_upload=Button(frame1, text='Upload',bg="#a4aadb",fg='black',bd=0,cursor="hand2",command=uploadCSVdb).place(x=220,y=250,width=80,height=25)

    btn_exit=Button(frame1, text='Cancel' ,bg="red",fg='white',bd=0,cursor="hand2",command=mrrwindow).place(x=320,y=250,width=80,height=25)


# ================================================ View Attendance 3 ======================================================================
# ================================================ View Attendance 3 ======================================================================
# ================================================ View Attendance 3 ======================================================================

def FetchdbFy():
    statusvar.set("View Attendance")

    def Fetchdb():
        try:
            # Connect to SQL Server
            db = connection.connect(host="localhost",user="root",database='fy')
            cursor = db.cursor()
            # Insert DataFrame to Table
            if fyDB.get() == 1 :
                clear_data()
                cursor.execute('SELECT * FROM imperative_programming')
                rows = cursor.fetchall() 
            elif  fyDB.get() == 2 :
                clear_data()
                cursor.execute('SELECT * FROM digital_electronic')
                rows = cursor.fetchall() 
            elif  fyDB.get() == 3 :
                clear_data()
                cursor.execute('SELECT * FROM operating_system')
                rows = cursor.fetchall() 
            elif  fyDB.get() == 4 :
                clear_data()
                cursor.execute('SELECT * FROM discrete_mathematics')
                rows = cursor.fetchall() 
            elif  fyDB.get() == 5 :
                clear_data()
                cursor.execute('SELECT * FROM communication_skills')
                rows = cursor.fetchall() 
            elif  fyDB.get() == 6 :
                clear_data()
                cursor.execute('SELECT * FROM oops')
                rows = cursor.fetchall() 
            elif  fyDB.get() == 7 :
                clear_data()
                cursor.execute('SELECT * FROM microprocessor_architecture')
                rows = cursor.fetchall() 
            elif  fyDB.get() == 8 :
                clear_data()
                cursor.execute('SELECT * FROM web_programming')
                rows = cursor.fetchall() 
            elif  fyDB.get() == 9 :
                clear_data()
                cursor.execute('SELECT * FROM numStat_methods')
                rows = cursor.fetchall() 
            elif  fyDB.get() == 10:
                clear_data()
                cursor.execute('SELECT * FROM green_computing')
                rows = cursor.fetchall() 

            for row in rows:
                tree.insert("", END, values=row) 
                
            db.commit()
            db.close()
            dbwindow()

            statusvar.set("Ready...")

        except :
            dbwindow()
            messagebox.showerror('Error  :(','Database is not connected / Subject not selected')
            statusvar.set("Ready...")


    def clear_data():
        tree.delete(*tree.get_children())
        return None

    def dbwindow():
        db_window.destroy()
        statusvar.set("Ready...")

    db_window = Toplevel(root)
    db_window.title("Subjects")
    db_window.geometry("600x300+5+100") 
    db_window.iconbitmap('tkinter_image/icon2.ico')
    db_window.config(bg="#EFEFF6")
    db_window.resizable(0,0) 
    db_window.focus_force()
    db_window.grab_set()

    pri1Font = font.Font(family="@Microsoft YaHei UI",size=10,weight="bold") 
    pri2Font = font.Font(family="@Microsoft YaHei UI",size=15) 
    secFont = ('Ubuntu', 10)

    frame1=Frame(db_window,bg="#EFEFF6")
    frame1.place(x=0,y=0,relwidth=1,relheight=1)
        

    title=LabelFrame(frame1,text=" First Year ",font=pri1Font,fg="#0E0C28",bg="#EFEFF6").place(x=10,y=10,width=580,height=280)

    sem1=Label(frame1,text="Semester 1",font=pri2Font,fg="#242849",bg="#EFEFF6").place(x=20,y=55)
    sem2=Label(frame1,text="Semester 2",font=pri2Font,fg="#242849",bg="#EFEFF6").place(x=20,y=145)
        
    fyDB =IntVar()
 
    Chk=Checkbutton(frame1,text="Imp prog",variable=fyDB,onvalue=1,offvalue=0,font=secFont,bg="#EFEFF6").place(x=20,y=90)
    Chk=Checkbutton(frame1,text="Digital elec...",variable=fyDB,onvalue=2,offvalue=0,font=secFont,bg="#EFEFF6").place(x=120,y=90)
    Chk=Checkbutton(frame1,text="Opersting sys..",variable=fyDB,onvalue=3,offvalue=0,font=secFont,bg="#EFEFF6").place(x=240,y=90)
    Chk=Checkbutton(frame1,text="Disc Maths",variable=fyDB,onvalue=4,offvalue=0,font=secFont,bg="#EFEFF6").place(x=360,y=90)
    Chk=Checkbutton(frame1,text="Comm skills",variable=fyDB,onvalue=5,offvalue=0,font=secFont,bg="#EFEFF6").place(x=480,y=90)
        
        
    Chk=Checkbutton(frame1,text="OOPs",variable=fyDB,onvalue=6,offvalue=0,font=secFont,bg="#EFEFF6").place(x=20,y=180)
    Chk=Checkbutton(frame1,text="Micro Arch...",variable=fyDB,onvalue=7,offvalue=0,font=secFont,bg="#EFEFF6").place(x=120,y=180)
    Chk=Checkbutton(frame1,text="Web prog...",variable=fyDB,onvalue=8,offvalue=0,font=secFont,bg="#EFEFF6").place(x=240,y=180)
    Chk=Checkbutton(frame1,text="Num&Stat M. ",variable=fyDB,onvalue=9,offvalue=0,font=secFont,bg="#EFEFF6").place(x=360,y=180)
    Chk=Checkbutton(frame1,text="Green Com...",variable=fyDB,onvalue=10,offvalue=0,font=secFont,bg="#EFEFF6").place(x=480,y=180)
        
    btn_upload=Button(frame1, text='Fetch',bg="#a4aadb",fg='black',bd=0,cursor="hand2",command=Fetchdb).place(x=220,y=250,width=80,height=25)

    btn_exit=Button(frame1, text='Cancel' ,bg="red",fg='white',bd=0,cursor="hand2",command=dbwindow).place(x=320,y=250,width=80,height=25)

def FetchdbSy():
    statusvar.set("View Attendance")
    def Fetchdb():
        try:
            db = connection.connect(host="localhost",user="root",database='sy')
            cursor = db.cursor()
            # Insert DataFrame to Table
            if syDB.get() == 1 :
                clear_data()
                cursor.execute('SELECT * FROM python')
                rows = cursor.fetchall() 
            elif  syDB.get() == 2 :
                clear_data()
                cursor.execute('SELECT * FROM data_structures')
                rows = cursor.fetchall() 
            elif  syDB.get() == 3 :
                clear_data()
                cursor.execute('SELECT * FROM computer_networking')
                rows = cursor.fetchall() 
            elif  syDB.get() == 4 :
                clear_data()
                cursor.execute('SELECT * FROM dbms')
                rows = cursor.fetchall() 
            elif  syDB.get() == 5 :
                clear_data()
                cursor.execute('SELECT * FROM maths')
                rows = cursor.fetchall() 
            elif  syDB.get() == 6 :
                clear_data()
                cursor.execute('SELECT * FROM java')
                rows = cursor.fetchall() 
            elif  syDB.get() == 7 :
                clear_data()
                cursor.execute('SELECT * FROM embedded_system')
                rows = cursor.fetchall() 
            elif  syDB.get() == 8 :
                clear_data()
                cursor.execute('SELECT * FROM cost')
                rows = cursor.fetchall() 
            elif  syDB.get() == 9 :
                clear_data()
                cursor.execute('SELECT * FROM software_engineering')
                rows = cursor.fetchall() 
            elif  syDB.get() == 10:
                clear_data()
                cursor.execute('SELECT * FROM cga')
                rows = cursor.fetchall() 
            
            for row in rows:
                tree.insert("", END, values=row) 
                
            db.commit()
            db.close()
            dbwindow()
            statusvar.set("Ready...")

        except  :
            dbwindow()
            messagebox.showerror('Error  :(','Database is not connected / Subject not selected')
            statusvar.set("Ready...")

    def clear_data():
        tree.delete(*tree.get_children())
        return None

    def dbwindow():
        db_window.destroy()
        statusvar.set("Ready...")

    db_window = Toplevel(root)
    db_window.title("Subjects")
    db_window.geometry("600x300+5+100") 
    db_window.config(bg="#EFEFF6")
    db_window.iconbitmap('tkinter_image/myicon.ico')
    db_window.resizable(0,0) 
    db_window.focus_force()
    db_window.grab_set()
    pri1Font = font.Font(family="@Microsoft YaHei UI",size=10,weight="bold") 
    pri2Font = font.Font(family="@Microsoft YaHei UI",size=15) 
    secFont = ('Ubuntu', 10)

    frame1=Frame(db_window,bg="#EFEFF6")
    frame1.place(x=0,y=0,relwidth=1,relheight=1)
        

    title=LabelFrame(frame1,text=" Second Year ",font=pri1Font,fg="#0E0C28",bg="#EFEFF6").place(x=10,y=10,width=580,height=280)

    sem1=Label(frame1,text="Semester 3",font=pri2Font,fg="#242849",bg="#EFEFF6").place(x=20,y=55)
    sem2=Label(frame1,text="Semester 4",font=pri2Font,fg="#242849",bg="#EFEFF6").place(x=20,y=145)
        
    syDB =IntVar()
 
    Chk=Checkbutton(frame1,text="Python",variable=syDB,onvalue=1,offvalue=0,font=secFont,bg="#EFEFF6").place(x=20,y=90)
    Chk=Checkbutton(frame1,text="Data structures",variable=syDB,onvalue=2,offvalue=0,font=secFont,bg="#EFEFF6").place(x=120,y=90)
    Chk=Checkbutton(frame1,text="Computer net..",variable=syDB,onvalue=3,offvalue=0,font=secFont,bg="#EFEFF6").place(x=240,y=90)
    Chk=Checkbutton(frame1,text="DBMS",variable=syDB,onvalue=4,offvalue=0,font=secFont,bg="#EFEFF6").place(x=360,y=90)
    Chk=Checkbutton(frame1,text="Maths",variable=syDB,onvalue=5,offvalue=0,font=secFont,bg="#EFEFF6").place(x=480,y=90)
        
        
    Chk=Checkbutton(frame1,text="Java",variable=syDB,onvalue=6,offvalue=0,font=secFont,bg="#EFEFF6").place(x=20,y=180)
    Chk=Checkbutton(frame1,text="Embedded sys.",variable=syDB,onvalue=7,offvalue=0,font=secFont,bg="#EFEFF6").place(x=120,y=180)
    Chk=Checkbutton(frame1,text="COST",variable=syDB,onvalue=8,offvalue=0,font=secFont,bg="#EFEFF6").place(x=240,y=180)
    Chk=Checkbutton(frame1,text="Software Eng",variable=syDB,onvalue=9,offvalue=0,font=secFont,bg="#EFEFF6").place(x=360,y=180)
    Chk=Checkbutton(frame1,text="CG & A",variable=syDB,onvalue=10,offvalue=0,font=secFont,bg="#EFEFF6").place(x=480,y=180)
        
    btn_upload=Button(frame1, text='Fetch',bg="#a4aadb",fg='black',bd=0,cursor="hand2",command=Fetchdb).place(x=220,y=250,width=80,height=25)
    btn_exit=Button(frame1, text='Cancel' ,bg="red",fg='white',bd=0,cursor="hand2",command=dbwindow).place(x=320,y=250,width=80,height=25)

# ================================================ DATABASE ======================================================================
# ================================================ DATABASE ======================================================================
# ================================================ DATABASE ======================================================================

def editdbFy():
    def Fetchdb():
        try:
            db = connection.connect(host="localhost",user="root",database='fy')
            cursor = db.cursor()
            # Insert DataFrame to Table
            if fyDB.get() == 1 :
                clear_data()
                cursor.execute('SELECT * FROM imperative_programming')
                rows = cursor.fetchall() 
            elif  fyDB.get() == 2 :
                clear_data()
                cursor.execute('SELECT * FROM digital_electronic')
                rows = cursor.fetchall()  
            elif  fyDB.get() == 3 :
                clear_data()
                cursor.execute('SELECT * FROM operating_system')
                rows = cursor.fetchall()    
            elif  fyDB.get() == 4 :
                clear_data()
                cursor.execute('SELECT * FROM discrete_mathematics')
                rows = cursor.fetchall() 
            elif  fyDB.get() == 5 :
                clear_data()
                cursor.execute('SELECT * FROM communication_skills')
                rows = cursor.fetchall() 
            elif  fyDB.get() == 6 :
                clear_data()
                cursor.execute('SELECT * FROM oops')
                rows = cursor.fetchall() 
            elif  fyDB.get() == 7 :
                clear_data()
                cursor.execute('SELECT * FROM microprocessor_architecture')
                rows = cursor.fetchall() 
            elif  fyDB.get() == 8 :
                clear_data()
                cursor.execute('SELECT * FROM web_programming')
                rows = cursor.fetchall() 
            elif  fyDB.get() == 9 :
                clear_data()
                cursor.execute('SELECT * FROM numStat_methods')
                rows = cursor.fetchall() 
            elif  fyDB.get() == 10:
                clear_data()
                cursor.execute('SELECT * FROM green_computing')
                rows = cursor.fetchall()

            for row in rows:
                student_tablefy.insert("", END, values=row)
                
            db.commit()
            db.close()   
            statusfyvar.set("Data Fetched")


        except  :
            messagebox.showerror('Error  :(','Database is not connected',parent=db_window)
      

    # -------------------------------
    def clear_data():
        try:
            student_tablefy.delete(*student_tablefy.get_children())
            return None
        except :
            messagebox.showerror('Error  :(','Something went wrong',parent=db_window)

    def add():
        # Insert DataFrame to Table
        if Rollno_var.get()=="" or name_var.get()=="" :
            messagebox.showerror("Error  :(","Enter Rollno & Name",parent=db_window)
        else :
            try :
                con = connection.connect(host="localhost",user="root",database='fy')
                cur = con.cursor()
                if fyDB.get() == 1 :
                    cur.execute("insert into imperative_programming  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from imperative_programming")
                elif  fyDB.get() == 2 :
                    cur.execute("insert into digital_electronic  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from digital_electronic")
                elif  fyDB.get() == 3 :
                    cur.execute("insert into operating_system  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from operating_system")
                elif  fyDB.get() == 4 :
                    cur.execute("insert into discrete_mathematics  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from discrete_mathematics")
                elif  fyDB.get() == 5 :
                    cur.execute("insert into communication_skills  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from communication_skills")
                elif  fyDB.get() == 6 :
                    cur.execute("insert into oops  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from oops")
                elif  fyDB.get() == 7 :
                    cur.execute("insert into microprocessor_architecture  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from microprocessor_architecture")
                elif  fyDB.get() == 8 :
                    cur.execute("insert into web_programming  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from web_programming")
                elif  fyDB.get() == 9 :
                    cur.execute("insert into numStat_methods  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from numStat_methods")
                elif  fyDB.get() == 10:
                    cur.execute("insert into green_computing  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from green_computing")

                rows=cur.fetchall()
                if len(rows)!=0:
                    student_tablefy.delete(*student_tablefy.get_children())
                    for row in rows:
                        student_tablefy.insert('',END,value=row)
                    con.commit()
                clear()
                con.close()
                statusfyvar.set("Record has been inserted")
            
            except :
                clear()
                messagebox.showerror('Error  :(','Database is not connected',parent=db_window)


    # -------------------------------------

    def clear():
        id_var.set("")
        Rollno_var.set("")
        name_var.set("")

    # -------------------------------------

    def delete_data():
        try :
            con = connection.connect(host="localhost",user="root",database='fy')

            cur = con.cursor()

            if fyDB.get() == 1 :
                cur.execute("delete from imperative_programming where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from imperative_programming")
                rows=cur.fetchall()
            elif  fyDB.get() == 2 :
                cur.execute("delete from digital_electronic where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from digital_electronic")
                rows=cur.fetchall()
            elif  fyDB.get() == 3 :
                cur.execute("delete from operating_system where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from operating_system")
                rows=cur.fetchall()
            elif  fyDB.get() == 4 :
                cur.execute("delete from discrete_mathematics where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from discrete_mathematics")
                rows=cur.fetchall()
            elif  fyDB.get() == 5 :
                cur.execute("delete from communication_skills where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from communication_skills")
                rows=cur.fetchall()
            elif  fyDB.get() == 6 :
                cur.execute("delete from oops where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from oops")
                rows=cur.fetchall()
            elif  fyDB.get() == 7 :
                cur.execute("delete from microprocessor_architecture where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from microprocessor_architecture")
                rows=cur.fetchall()
            elif  fyDB.get() == 8 :
                cur.execute("delete from web_programming where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from web_programming")
                rows=cur.fetchall()
            elif  fyDB.get() == 9 :
                cur.execute("delete from numStat_methods where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from numStat_methods")
                rows=cur.fetchall()
            elif  fyDB.get() == 10:
                cur.execute("delete from green_computing where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from green_computing")
                rows=cur.fetchall()


            if len(rows)!=0:
                student_tablefy.delete(*student_tablefy.get_children())
                for row in rows:
                    student_tablefy.insert('',END,value=row)
                con.commit()


            con.close()
            clear()
            statusfyvar.set("Record has been deleted")

        except :
            clear()
            messagebox.showerror('Error  :(','Something went wrong ',parent=db_window)
        

    def dbwindow():
        db_window.destroy()
        statusvar.set("Ready...")

    def search_data():
        try :
                
            con = connection.connect(host="localhost",user="root",database='fy')
            cursor=con.cursor()
            
            if fyDB.get() == 1 :
                cursor.execute("select * from imperative_programming where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall() 
            elif  fyDB.get() == 2 :
                cursor.execute("select * from digital_electronic where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall() 
            elif  fyDB.get() == 3 :
                cursor.execute("select * from operating_system where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall() 
            elif  fyDB.get() == 4 :
                cursor.execute("select * from discrete_mathematics where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall() 
            elif  fyDB.get() == 5 :
                cursor.execute("select * from communication_skills where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall() 
            elif  fyDB.get() == 6 :
                cursor.execute("select * from oops where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall() 
            elif  fyDB.get() == 7 :
                cursor.execute("select * from microprocessor_architecture where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall() 
            elif  fyDB.get() == 8 :
                cursor.execute("select * from web_programming where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall() 
            elif  fyDB.get() == 9 :
                cursor.execute("select * from numStat_methods where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall() 
            elif  fyDB.get() == 10:
                cursor.execute("select * from green_computing where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall() 
    
            
            
            
            if len(rows)!=0:
                student_tablefy.delete(*student_tablefy.get_children())
                for row in rows:
                        student_tablefy.insert('',END,value=row)
                con.commit()
            con.close()
            clear()

        except :
            messagebox.showerror('Error  :(','Database is not connected',parent=db_window)
         
    # -----------------------------------------------

    db_window = Toplevel(root)
    db_window.title("First Year Database")
    db_window.state("zoomed") 
    db_window.iconbitmap('tkinter_image/icon2.ico') 
    db_window.config(bg="#EFEFF6")
    db_window.grab_set()
    pri1Font = font.Font(family="@Microsoft YaHei UI",size=10,weight="bold") 
    pri2Font = font.Font(family="@Microsoft YaHei UI",size=15) 
    secFont = ('Ubuntu', 10)

    frame1=Frame(db_window,bg="#EFEFF6")
    frame1.place(x=10,y=0,relwidth=1,relheight=1)
        
    # ------------------------------------------

    title=LabelFrame(frame1,text=" First Year ",font=pri1Font,fg="#0E0C28").place(x=10,y=10,width=580,height=280)

    sem1=Label(frame1,text="Semester 1",font=pri2Font,fg="#242849").place(x=20,y=55)
    sem2=Label(frame1,text="Semester 2",font=pri2Font,fg="#242849").place(x=20,y=145)
        
    fyDB =IntVar()
 
    Chk=Checkbutton(frame1,text="Imp prog",variable=fyDB,onvalue=1,offvalue=0,font=secFont).place(x=20,y=90)
    Chk=Checkbutton(frame1,text="Digital elec...",variable=fyDB,onvalue=2,offvalue=0,font=secFont).place(x=120,y=90)
    Chk=Checkbutton(frame1,text="Opersting sys..",variable=fyDB,onvalue=3,offvalue=0,font=secFont).place(x=240,y=90)
    Chk=Checkbutton(frame1,text="Disc Maths",variable=fyDB,onvalue=4,offvalue=0,font=secFont).place(x=360,y=90)
    Chk=Checkbutton(frame1,text="Comm skills",variable=fyDB,onvalue=5,offvalue=0,font=secFont).place(x=480,y=90)
        
        
    Chk=Checkbutton(frame1,text="OOPs",variable=fyDB,onvalue=6,offvalue=0,font=secFont).place(x=20,y=180)
    Chk=Checkbutton(frame1,text="Micro Arch...",variable=fyDB,onvalue=7,offvalue=0,font=secFont).place(x=120,y=180)
    Chk=Checkbutton(frame1,text="Web prog...",variable=fyDB,onvalue=8,offvalue=0,font=secFont).place(x=240,y=180)
    Chk=Checkbutton(frame1,text="Num&Stat M. ",variable=fyDB,onvalue=9,offvalue=0,font=secFont).place(x=360,y=180)
    Chk=Checkbutton(frame1,text="Green Com...",variable=fyDB,onvalue=10,offvalue=0,font=secFont).place(x=480,y=180)
        
    btn_fetch=Button(frame1, text='Fetch',bg="#a4aadb",fg='black',bd=0,cursor="hand2",command=Fetchdb).place(x=270,y=250,width=80,height=25)
    

    # ---------------------------------

    id_var=StringVar() 
    Rollno_var=StringVar()
    name_var=StringVar()

    IDtitle=LabelFrame(frame1,font=pri1Font,fg="#0E0C28").place(x=10,y=320,width=580,height=80)

    lbl_id=Label(frame1,text="Id :",bg=rootColor,font=('Ubuntu', 12,'bold'),anchor=W).place(x=60,y=350,width=100,height=25)
    txt_id=Entry(frame1,textvariable=id_var,font=Font_btn).place(x=100,y=350,width=250,height=25)
    deletebtn=Button(frame1,text="Delete",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=delete_data).place(x=390,y=350,width=100,height=25)
    
    ADDtitle=LabelFrame(frame1,font=pri1Font,fg="#0E0C28").place(x=10,y=430,width=580,height=200)

    lbl_roll=Label(frame1,text="Roll no. :",bg=rootColor,font=('Ubuntu', 12,'bold'),anchor=W).place(x=100,y=470,width=100,height=25)
    txt_Roll=Entry(frame1,textvariable=Rollno_var,font=Font_btn).place(x=180,y=470,width=280,height=25)
    
    lbl_name=Label(frame1,text="Name : ",bg=rootColor,font=('Ubuntu', 12,'bold'),anchor=W).place(x=100,y=520,width=100,height=25)
    txt_name=Entry(frame1,textvariable=name_var,font=Font_btn).place(x=180,y=520,width=280,height=25)
 
    Addbtn=Button(frame1,text="Add",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=add).place(x=220,y=580,width=140,height=25)


    # --------------------------------------

    frame2=Frame(db_window,bg=rootColor)
    frame2.place(x=0,y=670,relwidth=1,height=50)

    statusfyvar = StringVar()
    statusfyvar.set("Ready...")
    sbarfy = Label(frame2,textvariable=statusfyvar,font=Font_btn,anchor=W).place(x=80,y=0,width=650,height=40)
    sbarfyText = Label(frame2,text ='Status : ',font=Font_btn).place(x=15,y=0,width=60,height=40)

    # ---------------------------------------

    frame3=Frame(db_window,bg="#EFEFF6")
    frame3.place(x=630,y=20,width=700,height=610)

    search_by=StringVar()
    search_txt=StringVar()

    lbl_search=Label(frame3,text="Search by : ",fg="black",bg='#EFEFF6',font=('Ubuntu', 12,'bold')).place(x=0,y=0,width=100,height=25)

    combo_search=ttk.Combobox(frame3,textvariable=search_by,font=Font_btn,cursor='hand2',state="readonly")
    combo_search['value']=('Select','Rollno','Name')
    combo_search.current(0)
    combo_search.place(x=100,y=0,width=140,height=25)

    txt_search=Entry(frame3,textvariable=search_txt,font=Font_btn,bd=1).place(x=260,y=0,width=150,height=25)
    
    # searchbtn=Button(dblbl3,text="Search",command=search_data,bg=BtnTxtClr,bd=0).place(x=350,y=5,width=100,height=20)
    searchbtn=Button(frame3,text="Search",bg=BtnTxtClr,bd=0,command=search_data).place(x=430,y=0,width=120,height=25)
    showallbtn=Button(frame3,text="Show All",bg=BtnTxtClr,bd=0,command=Fetchdb).place(x=560,y=0,width=120,height=25)

    # --------------------------------------------

    Table_Frame=Frame( frame3,bg="white")
    Table_Frame.place(x=0,y=40,relwidth=1,relheight=1)

    scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
    student_tablefy=ttk.Treeview(Table_Frame,column=("Id","Rollno","Name","Date","Time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=student_tablefy.xview)
    scroll_y.config(command=student_tablefy.yview)
    student_tablefy.heading("Id",text="Id")
    student_tablefy.heading("Rollno",text="Rollno")
    student_tablefy.heading("Name",text="Name")
    student_tablefy.heading("Date",text="Date")
    student_tablefy.heading("Time",text="Time")
    student_tablefy['show']='headings'
    student_tablefy.column("Id",width=50)
    student_tablefy.column("Rollno",width=50)
    student_tablefy.column("Name",width=100)
    student_tablefy.column("Date",width=100)
    student_tablefy.column("Time",width=100)
    student_tablefy.pack(fill=BOTH,expand=1)

def editdbSy():
    def Fetchdb():
        try:
            db = connection.connect(host="localhost",user="root",database='sy')
            cursor = db.cursor()
            # Insert DataFrame to Table
            if syDB.get() == 1 :
                clear_data()
                cursor.execute('SELECT * FROM python')
                rows = cursor.fetchall() 
            elif  syDB.get() == 2 :
                clear_data()
                cursor.execute('SELECT * FROM data_structures')
                rows = cursor.fetchall() 
            elif  syDB.get() == 3 :
                clear_data()
                cursor.execute('SELECT * FROM computer_networking')
                rows = cursor.fetchall() 
            elif  syDB.get() == 4 :
                clear_data()
                cursor.execute('SELECT * FROM dbms')
                rows = cursor.fetchall() 
            elif  syDB.get() == 5 :
                clear_data()
                cursor.execute('SELECT * FROM maths')
                rows = cursor.fetchall() 
            elif  syDB.get() == 6 :
                clear_data()
                cursor.execute('SELECT * FROM java')
                rows = cursor.fetchall() 
            elif  syDB.get() == 7 :
                clear_data()
                cursor.execute('SELECT * FROM embedded_system')
                rows = cursor.fetchall() 
            elif  syDB.get() == 8 :
                clear_data()
                cursor.execute('SELECT * FROM cost')
                rows = cursor.fetchall() 
            elif  syDB.get() == 9 :
                clear_data()
                cursor.execute('SELECT * FROM software_engineering')
                rows = cursor.fetchall() 
            elif  syDB.get() == 10:
                clear_data()
                cursor.execute('SELECT * FROM cga')
                rows = cursor.fetchall() 
            
            for row in rows:
                student_tablesy.insert("", END, values=row) 
                
            db.commit()
            db.close()
            statussyvar.set("Data Fetched")

        except  :
     
            messagebox.showerror('Error  :(','Database is not connected',parent=db_window)
      

    def clear_data():
        try:
            student_tablesy.delete(*student_tablesy.get_children())
            return None
        except Exception as e :
            messagebox.showerror('Error  :(',f'Something went wrong',parent=db_window)

    # -------------------------------

    def add():
        # Insert DataFrame to Table
        if Rollno_var.get()=="" or name_var.get()=="":
            messagebox.showerror("Error :(","Enter Rollno & Name",parent=db_window)
        else :
            try:
                    
                con = connection.connect(host="localhost",user="root",database='sy')
                cur = con.cursor()
                if syDB.get() == 1 :
                    cur.execute("insert into python  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from python")
                elif  syDB.get() == 2 :
                    cur.execute("insert into data_structures  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from data_structures")
                elif  syDB.get() == 3 :
                    cur.execute("insert into computer_networking  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from computer_networking")
                elif  syDB.get() == 4 :
                    cur.execute("insert into dbms  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from dbms")
                elif  syDB.get() == 5 :
                    cur.execute("insert into maths  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from maths")
                elif  syDB.get() == 6 :
                    cur.execute("insert into java  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from java")
                elif  syDB.get() == 7 :
                    cur.execute("insert into embedded_system  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from embedded_system")
                elif  syDB.get() == 8 :
                    cur.execute("insert into cost  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from cost")
                elif  syDB.get() == 9 :
                    cur.execute("insert into software_engineering  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from software_engineering")
                elif  syDB.get() == 10:
                    cur.execute("insert into cga  (Rollno, Name) VALUES (%s,%s)",(Rollno_var.get(),name_var.get()))
                    con.commit()
                    cur.execute("select * from cga")

                rows=cur.fetchall()
                if len(rows)!=0:
                    student_tablesy.delete(*student_tablesy.get_children())
                    for row in rows:
                        student_tablesy.insert('',END,value=row)
                    con.commit()
                clear()
                con.close()
                statussyvar.set("Record has been inserted")
            
            except :
                clear()
                messagebox.showerror('Error  :(','Database is not connected',parent=db_window)


    # -------------------------------------

    def clear():
        id_var.set("")
        Rollno_var.set("")
        name_var.set("")

    # -------------------------------------

    def delete_data():
        try:
            con = connection.connect(host="localhost",user="root",database='sy')

            cur = con.cursor()

            if syDB.get() == 1 :
                cur.execute("delete from python where id= %s", (id_var.get(),))
                con.commit()
                cur.execute("select * from python")
                rows=cur.fetchall()
            elif  syDB.get() == 2 :
                cur.execute("delete from data_structures where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from data_structures")
                rows=cur.fetchall()
            elif  syDB.get() == 3 :
                cur.execute("delete from computer_networking where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from computer_networking")
                rows=cur.fetchall()
            elif  syDB.get() == 4 :
                cur.execute("delete from dbms where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from dbms")
                rows=cur.fetchall()
            elif  syDB.get() == 5 :
                cur.execute("delete from maths where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from maths")
                rows=cur.fetchall()
            elif  syDB.get() == 6 :
                cur.execute("delete from java where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from java")
                rows=cur.fetchall()
            elif  syDB.get() == 7 :
                cur.execute("delete from embedded_system where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from embedded_system")
                rows=cur.fetchall()
            elif  syDB.get() == 8 :
                cur.execute("delete from cost where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from cost")
                rows=cur.fetchall()
            elif  syDB.get() == 9 :
                cur.execute("delete from software_engineering where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from software_engineering")
                rows=cur.fetchall()
            elif  syDB.get() == 10:
                cur.execute("delete from cga where id=%s", (id_var.get(),))
                con.commit()
                cur.execute("select * from cga")
                rows=cur.fetchall()

            if len(rows)!=0:
                student_tablesy.delete(*student_tablesy.get_children())
                for row in rows:
                    student_tablesy.insert('',END,value=row)
            con.commit()
            clear()
            con.close()
            statussyvar.set("Record has been deleted")


        except :
            messagebox.showerror('Error  :(','Something went wrong ',parent=db_window)
        

    def search_data():
        try:
                
            con = connection.connect(host="localhost",user="root",database='sy')
            cursor=con.cursor()

            if syDB.get() == 1 :
                cursor.execute("select * from python where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall() 
            elif  syDB.get() == 2 :
                cursor.execute("select * from data_structures where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall() 
            elif  syDB.get() == 3 :
                cursor.execute("select * from computer_networking where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall() 
            elif  syDB.get() == 4 :
                cursor.execute("select * from dbms where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall() 
            elif  syDB.get() == 5 :
                cursor.execute("select * from maths where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall() 
            elif  syDB.get() == 6 :
                cursor.execute("select * from java where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall() 
            elif  syDB.get() == 7 :
                cursor.execute("select * from embedded_system where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall()             
            elif  syDB.get() == 8 :
                cursor.execute("select * from cost where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall()             
            elif  syDB.get() == 9 :
                cursor.execute("select * from cost where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall()             
            elif  syDB.get() == 10:
                cursor.execute("select * from cga where "+str(search_by.get())+" LIKE  '%"+str(search_txt.get()) +"%' ")
                rows = cursor.fetchall()             


            if len(rows)!=0:
                student_tablesy.delete(*student_tablesy.get_children())
                for row in rows:
                    student_tablesy.insert('',END,value=row)
                con.commit()
            con.close()
            clear()
    
        except :
            messagebox.showerror('Error  :(','Database is not connected',parent=db_window)


    # -----------------------------------------------

    db_window = Toplevel(root)
    db_window.title("Second Year Database")
    db_window.state("zoomed") 
    db_window.config(bg="#EFEFF6")
    db_window.grab_set()
    db_window.iconbitmap('tkinter_image/icon2.ico') 


    pri1Font = font.Font(family="@Microsoft YaHei UI",size=10,weight="bold") 
    pri2Font = font.Font(family="@Microsoft YaHei UI",size=15) 
    secFont = ('Ubuntu', 10)

    frame1=Frame(db_window,bg="#EFEFF6")
    frame1.place(x=10,y=0,relwidth=1,relheight=1)
        

    title=LabelFrame(frame1,text=" Second Year ",font=pri1Font,fg="#0E0C28").place(x=10,y=10,width=580,height=280)

    sem1=Label(frame1,text="Semester 3",font=pri2Font,fg="#242849").place(x=20,y=55)
    sem2=Label(frame1,text="Semester 4",font=pri2Font,fg="#242849").place(x=20,y=145)
        
    syDB =IntVar()
 
    Chk=Checkbutton(frame1,text="Python",variable=syDB,onvalue=1,offvalue=0,font=secFont).place(x=20,y=90)
    Chk=Checkbutton(frame1,text="Data structures",variable=syDB,onvalue=2,offvalue=0,font=secFont).place(x=120,y=90)
    Chk=Checkbutton(frame1,text="Computer net..",variable=syDB,onvalue=3,offvalue=0,font=secFont).place(x=240,y=90)
    Chk=Checkbutton(frame1,text="DBMS",variable=syDB,onvalue=4,offvalue=0,font=secFont).place(x=360,y=90)
    Chk=Checkbutton(frame1,text="Maths",variable=syDB,onvalue=5,offvalue=0,font=secFont).place(x=480,y=90)
        
        
    Chk=Checkbutton(frame1,text="Java",variable=syDB,onvalue=6,offvalue=0,font=secFont).place(x=20,y=180)
    Chk=Checkbutton(frame1,text="Embedded sys.",variable=syDB,onvalue=7,offvalue=0,font=secFont).place(x=120,y=180)
    Chk=Checkbutton(frame1,text="COST",variable=syDB,onvalue=8,offvalue=0,font=secFont).place(x=240,y=180)
    Chk=Checkbutton(frame1,text="Software Eng",variable=syDB,onvalue=9,offvalue=0,font=secFont).place(x=360,y=180)
    Chk=Checkbutton(frame1,text="CG & A",variable=syDB,onvalue=10,offvalue=0,font=secFont).place(x=480,y=180)
        
    btn_fetch=Button(frame1, text='Fetch',bg="#a4aadb",fg='black',bd=0,cursor="hand2",command=Fetchdb).place(x=270,y=250,width=80,height=25)

    # ---------------------------------

    id_var=StringVar() 
    Rollno_var=StringVar()
    name_var=StringVar()


    IDtitle=LabelFrame(frame1,font=pri1Font,fg="#0E0C28").place(x=10,y=320,width=580,height=80)
    
    lbl_id=Label(frame1,text="Id :",bg=rootColor,font=('Ubuntu', 12,'bold'),anchor=W).place(x=60,y=350,width=100,height=25)
    txt_id=Entry(frame1,textvariable=id_var,font=Font_btn).place(x=100,y=350,width=250,height=25)
    deletebtn=Button(frame1,text="Delete",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=delete_data).place(x=390,y=350,width=100,height=25)
    
    ADDtitle=LabelFrame(frame1,font=pri1Font,fg="#0E0C28").place(x=10,y=430,width=580,height=200)

    lbl_roll=Label(frame1,text="Roll no. :",bg=rootColor,font=('Ubuntu', 12,'bold'),anchor=W).place(x=100,y=470,width=100,height=25)
    txt_Roll=Entry(frame1,textvariable=Rollno_var,font=Font_btn).place(x=180,y=470,width=280,height=25)
    
    lbl_name=Label(frame1,text="Name : ",bg=rootColor,font=('Ubuntu', 12,'bold'),anchor=W).place(x=100,y=520,width=100,height=25)
    txt_name=Entry(frame1,textvariable=name_var,font=Font_btn).place(x=180,y=520,width=280,height=25)
 
    Addbtn=Button(frame1,text="Add",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=add).place(x=220,y=580,width=140,height=25)


    # --------------------------------------

    frame2=Frame(db_window,bg=rootColor)
    frame2.place(x=0,y=670,relwidth=1,height=50)

    statussyvar = StringVar()
    statussyvar.set("Ready...")
    sbarsy = Label(frame2,textvariable=statussyvar,font=Font_btn,anchor=W).place(x=80,y=0,width=650,height=40)
    sbarsyText = Label(frame2,text ='Status : ',font=Font_btn).place(x=15,y=0,width=60,height=40)

    # --------------------------------------
    frame3=Frame(db_window,bg="#EFEFF6")
    frame3.place(x=630,y=20,width=700,height=610)

    search_by=StringVar()
    search_txt=StringVar()

    lbl_search=Label(frame3,text="Search by : ",fg="black",bg='#EFEFF6',font=('Ubuntu', 12,'bold')).place(x=0,y=0,width=100,height=25)

    combo_search=ttk.Combobox(frame3,textvariable=search_by,font=Font_btn,cursor='hand2',state="readonly")
    combo_search['value']=('Select','Rollno','Name')
    combo_search.current(0)
    combo_search.place(x=100,y=0,width=140,height=25)

    txt_search=Entry(frame3,textvariable=search_txt,font=Font_btn,bd=1).place(x=260,y=0,width=150,height=25)
    
    # searchbtn=Button(dblbl3,text="Search",command=search_data,bg=BtnTxtClr,bd=0).place(x=350,y=5,width=100,height=20)
    searchbtn=Button(frame3,text="Search",bg=BtnTxtClr,bd=0,command=search_data).place(x=430,y=0,width=120,height=25)
    showallbtn=Button(frame3,text="Show All",bg=BtnTxtClr,bd=0,command=Fetchdb).place(x=560,y=0,width=120,height=25)

    # --------------------------------------------

    Table_Frame=Frame( frame3,bg="white")
    Table_Frame.place(x=0,y=40,relwidth=1,relheight=1)

    scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
    student_tablesy=ttk.Treeview(Table_Frame,column=("Id","Rollno","Name","Date","Time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=student_tablesy.xview)
    scroll_y.config(command=student_tablesy.yview)
    student_tablesy.heading("Id",text="Id")
    student_tablesy.heading("Rollno",text="Rollno")
    student_tablesy.heading("Name",text="Name")
    student_tablesy.heading("Date",text="Date")
    student_tablesy.heading("Time",text="Time")
    student_tablesy['show']='headings'
    student_tablesy.column("Id",width=50)
    student_tablesy.column("Rollno",width=50)
    student_tablesy.column("Name",width=100)
    student_tablesy.column("Date",width=100)
    student_tablesy.column("Time",width=100)
    student_tablesy.pack(fill=BOTH,expand=1)

# ================================================ Defaulter list ======================================================================
# ================================================ Defaulter list ======================================================================
# ================================================ Defaulter list ======================================================================

def downloaddbFy():
    statusvar.set("Download Attendance Records")

    def fetch_table_data():
        global subjectName
        try :
            db = connection.connect(host="localhost",user="root",database='fy')
            cursor = db.cursor()
            # Insert DataFrame to Table
            if fyDB.get() == 1 :
                subjectName = 'Imperative Programming'
                cursor.execute('SELECT * FROM imperative_programming')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  fyDB.get() == 2 :
                subjectName = 'Digital Electronic'
                cursor.execute('SELECT * FROM digital_electronic')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  fyDB.get() == 3 :
                subjectName = 'Operating System'
                cursor.execute('SELECT * FROM operating_system')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  fyDB.get() == 4 :
                subjectName = 'Discrete Mathematics'
                cursor.execute('SELECT * FROM discrete_mathematics')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  fyDB.get() == 5 :
                subjectName = 'Communication Skills'
                cursor.execute('SELECT * FROM communication_skills')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  fyDB.get() == 6 :
                subjectName = 'OOPs'
                cursor.execute('SELECT * FROM oops')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  fyDB.get() == 7 :
                subjectName = 'Microprocessor Architecture'
                cursor.execute('SELECT * FROM microprocessor_architecture')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  fyDB.get() == 8 :
                subjectName = 'Web Programming'
                cursor.execute('SELECT * FROM web_programming')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  fyDB.get() == 9 :
                subjectName = 'NumStat Methods'
                cursor.execute('SELECT * FROM numStat_methods')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  fyDB.get() == 10:
                subjectName = 'Green Computing'
                cursor.execute('SELECT * FROM green_computing')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 

            # Closing connection
            db.commit()
            db.close()
                    
            return header, rows

        except :
            dbwindow()
            messagebox.showerror('Error  :(','Database is not connected')
            statusvar.set("Ready...")


    def importFile():
        global subjectName
        today = datetime.today()
        currDate = today.strftime("%d-%b-%Y")
        ClassNamelst = ['fy','FY','fY','Fy','sy','SY','sY','Sy','TY','ty','Ty','tY']

        file_path = simpledialog.askstring("Input string","Enter Class FY/SY/TY : ")

        if file_path == "" or file_path == None or file_path not in ClassNamelst:
            messagebox.showerror('Error  :(','Invalid Class Name')
            dbwindow()
        else :
            try:
                header, rows = fetch_table_data()
                # Create csv file
                f = open(f'Defaulter_List/{file_path}/{subjectName} Defaulter_List {currDate}.csv', 'w')

                # Write header
                f.write(','.join(header) + '\n')

                for row in rows:
                    f.write(','.join(str(r) for r in row) + '\n')

                f.close()
                dbwindow()
                tmsg.showinfo('Success  :)','Attendance records has been downloaded successfully ')
                statusvar.set("Ready...")

            except Exception as e:
                dbwindow()
                messagebox.showerror('Error  :(',f'Error due to {str(e)}')
                statusvar.set("Ready...")
        
    def dbwindow():
        db_window.destroy()
        statusvar.set("Ready...")

    db_window = Toplevel(root)
    db_window.title("Subjects")
    db_window.geometry("600x300+5+100") 
    db_window.config(bg="#EFEFF6")
    db_window.iconbitmap('tkinter_image/icon2.ico')
    db_window.resizable(0,0)
    db_window.focus_force()
    db_window.grab_set()

    pri1Font = font.Font(family="@Microsoft YaHei UI",size=10,weight="bold") 
    pri2Font = font.Font(family="@Microsoft YaHei UI",size=15) 
    secFont = ('Ubuntu', 10)

    frame1=Frame(db_window,bg="#EFEFF6")
    frame1.place(x=0,y=0,relwidth=1,relheight=1)
        

    title=LabelFrame(frame1,text=" First Year ",font=pri1Font,fg="#0E0C28",bg="#EFEFF6").place(x=10,y=10,width=580,height=280)

    sem1=Label(frame1,text="Semester 1",font=pri2Font,fg="#242849",bg="#EFEFF6").place(x=20,y=55)
    sem2=Label(frame1,text="Semester 2",font=pri2Font,fg="#242849",bg="#EFEFF6").place(x=20,y=145)
        
    fyDB =IntVar()

    Chk=Checkbutton(frame1,text="Imp prog",variable=fyDB,onvalue=1,offvalue=0,font=secFont,bg="#EFEFF6").place(x=20,y=90)
    Chk=Checkbutton(frame1,text="Digital elec...",variable=fyDB,onvalue=2,offvalue=0,font=secFont,bg="#EFEFF6").place(x=120,y=90)
    Chk=Checkbutton(frame1,text="Opersting sys..",variable=fyDB,onvalue=3,offvalue=0,font=secFont,bg="#EFEFF6").place(x=240,y=90)
    Chk=Checkbutton(frame1,text="Disc Maths",variable=fyDB,onvalue=4,offvalue=0,font=secFont,bg="#EFEFF6").place(x=360,y=90)
    Chk=Checkbutton(frame1,text="Comm skills",variable=fyDB,onvalue=5,offvalue=0,font=secFont,bg="#EFEFF6").place(x=480,y=90)
        
        
    Chk=Checkbutton(frame1,text="OOPs",variable=fyDB,onvalue=6,offvalue=0,font=secFont,bg="#EFEFF6").place(x=20,y=180)
    Chk=Checkbutton(frame1,text="Micro Arch...",variable=fyDB,onvalue=7,offvalue=0,font=secFont,bg="#EFEFF6").place(x=120,y=180)
    Chk=Checkbutton(frame1,text="Web prog...",variable=fyDB,onvalue=8,offvalue=0,font=secFont,bg="#EFEFF6").place(x=240,y=180)
    Chk=Checkbutton(frame1,text="Num&Stat M. ",variable=fyDB,onvalue=9,offvalue=0,font=secFont,bg="#EFEFF6").place(x=360,y=180)
    Chk=Checkbutton(frame1,text="Green Com...",variable=fyDB,onvalue=10,offvalue=0,font=secFont,bg="#EFEFF6").place(x=480,y=180)
        
    btn_download=Button(frame1, text='Download',bg="#a4aadb",fg='black',bd=0,cursor="hand2",command=importFile).place(x=220,y=250,width=80,height=25)
    btn_exit=Button(frame1, text='Cancel' ,bg="red",fg='white',bd=0,cursor="hand2",command=dbwindow).place(x=320,y=250,width=80,height=25)

def downloaddbSy():
    statusvar.set("Download Attendance Records")
    def fetch_table_data():
        global subjectName
        try :

            db = connection.connect(host="localhost",user="root",database='sy')
            cursor = db.cursor()
            # Insert DataFrame to Table
            if syDB.get() == 1 :
                subjectName = 'Python'
                cursor.execute('SELECT * FROM python')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  syDB.get() == 2 :
                subjectName = 'Data Structures'
                cursor.execute('SELECT * FROM data_structures')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  syDB.get() == 3 :
                subjectName = 'Computer Networking'
                cursor.execute('SELECT * FROM computer_networking')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  syDB.get() == 4 :
                subjectName = 'DBMS'
                cursor.execute('SELECT * FROM dbms')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  syDB.get() == 5 :
                subjectName = 'Maths'
                cursor.execute('SELECT * FROM maths')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  syDB.get() == 6 :
                subjectName = 'Java'
                cursor.execute('SELECT * FROM java')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  syDB.get() == 7 :
                subjectName = 'Embedded System'
                cursor.execute('SELECT * FROM embedded_system')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  syDB.get() == 8 :
                subjectName = 'COST'
                cursor.execute('SELECT * FROM cost')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  syDB.get() == 9 :
                subjectName = 'Software Engineering'
                cursor.execute('SELECT * FROM software_engineering')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 
            elif  syDB.get() == 10:
                subjectName = 'CGA'
                cursor.execute('SELECT * FROM cga')
                header = [row[0] for row in cursor.description]
                rows = cursor.fetchall() 

            # Closing connection
            db.commit()
            db.close()
        
            return header, rows

        except  :
            dbwindow()
            messagebox.showerror('Error  :(','Database is not connected')
            statusvar.set("Ready...")

    def importFile():
        global subjectName
        today = datetime.today()
        currDate = today.strftime("%d-%b-%Y")
        ClassNamelst = ['fy','FY','fY','Fy','sy','SY','sY','Sy','TY','ty','Ty','tY']

        file_path = simpledialog.askstring("Input string","Enter Class FY/SY/TY : ")

        if file_path == "" or file_path == None or file_path not in ClassNamelst:
            messagebox.showerror('Error  :(','Invalid Class Name')
            dbwindow()
        else :
            try:
                header, rows = fetch_table_data()
                # Create csv file
                f = open(f'Defaulter_List/{file_path}/{subjectName} Defaulter_List {currDate}.csv', 'w')

                # Write header
                f.write(','.join(header) + '\n')

                for row in rows:
                    f.write(','.join(str(r) for r in row) + '\n')

                f.close()
                # print(str(len(rows)) + ' rows written successfully to ' + f.name)

                dbwindow()
                tmsg.showinfo('Success  :)','Attendance records has been downloaded successfully ')
                statusvar.set("Ready...")

            except Exception as e :
                dbwindow()
                messagebox.showerror('Error  :(',f'Error due to {str(e)}')
                statusvar.set("Ready...")
        
    def dbwindow():
        db_window.destroy()
        statusvar.set("Ready...")


    db_window = Toplevel(root)
    db_window.title("Subjects")
    db_window.geometry("600x300+5+100") 
    db_window.config(bg="#EFEFF6")
    db_window.iconbitmap('tkinter_image/icon2.ico') 
    db_window.resizable(0,0)
    db_window.focus_force()
    db_window.grab_set()


    pri1Font = font.Font(family="@Microsoft YaHei UI",size=10,weight="bold") 
    pri2Font = font.Font(family="@Microsoft YaHei UI",size=15) 
    secFont = ('Ubuntu', 10)

    frame1=Frame(db_window,bg="#EFEFF6")
    frame1.place(x=0,y=0,relwidth=1,relheight=1)
        

    title=LabelFrame(frame1,text=" Second Year ",font=pri1Font,fg="#0E0C28",bg="#EFEFF6").place(x=10,y=10,width=580,height=280)

    sem1=Label(frame1,text="Semester 1",font=pri2Font,fg="#242849",bg="#EFEFF6").place(x=20,y=55)
    sem2=Label(frame1,text="Semester 2",font=pri2Font,fg="#242849",bg="#EFEFF6").place(x=20,y=145)
        
    syDB =IntVar()

    Chk=Checkbutton(frame1,text="Python",variable=syDB,onvalue=1,offvalue=0,font=secFont,bg="#EFEFF6").place(x=20,y=90)
    Chk=Checkbutton(frame1,text="Data structures.",variable=syDB,onvalue=2,offvalue=0,font=secFont,bg="#EFEFF6").place(x=120,y=90)
    Chk=Checkbutton(frame1,text="Computer net...",variable=syDB,onvalue=3,offvalue=0,font=secFont,bg="#EFEFF6").place(x=240,y=90)
    Chk=Checkbutton(frame1,text="DBMS",variable=syDB,onvalue=4,offvalue=0,font=secFont,bg="#EFEFF6").place(x=360,y=90)
    Chk=Checkbutton(frame1,text="Maths",variable=syDB,onvalue=5,offvalue=0,font=secFont,bg="#EFEFF6").place(x=480,y=90)
        
        
    Chk=Checkbutton(frame1,text="Java",variable=syDB,onvalue=6,offvalue=0,font=secFont,bg="#EFEFF6").place(x=20,y=180)
    Chk=Checkbutton(frame1,text="Embedded sys.",variable=syDB,onvalue=7,offvalue=0,font=secFont,bg="#EFEFF6").place(x=120,y=180)
    Chk=Checkbutton(frame1,text="COST",variable=syDB,onvalue=8,offvalue=0,font=secFont,bg="#EFEFF6").place(x=240,y=180)
    Chk=Checkbutton(frame1,text="Software Eng",variable=syDB,onvalue=9,offvalue=0,font=secFont,bg="#EFEFF6").place(x=360,y=180)
    Chk=Checkbutton(frame1,text="CG & A",variable=syDB,onvalue=10,offvalue=0,font=secFont,bg="#EFEFF6").place(x=480,y=180)
        
    btn_download=Button(frame1, text='Download',bg="#a4aadb",fg='black',bd=0,cursor="hand2",command=importFile).place(x=220,y=250,width=80,height=25)
    btn_exit=Button(frame1, text='Cancel',bg="red",fg='white',bd=0,cursor="hand2",command=dbwindow).place(x=320,y=250,width=80,height=25)

def openCSV_defL():
    statusvar.set("File explorer has open")
    file = askopenfile(initialdir="Defaulter_List/",mode ='r', filetypes =[('CSV Files', '*.csv')]) 
    if file is not None:
        statusvar.set("You can't select any file")
        tmsg.showwarning('','View mode only')
    statusvar.set("Ready...")


def browseFile_defL():
    statusvar.set("File explorer has open")
    global filename_defL
    filename_defL = filedialog.askopenfilename(initialdir="Defaulter_List/",
                                                title="Select A File",
                                                filetype=(("CSV files", "*.csv"),("All files", "*.*")))
    if  filename_defL == '' or filename_defL == None :
        messagebox.showerror("Error  :(", "File not selected")
        statusvar.set("Ready...")
    else :
        try :
            label_file_defl["text"] = filename_defL
            statusvar.set(os.path.basename(filename_defL))
            return None
            statusvar.set("Ready...")
        except Exception as e:
            messagebox.showerror("Error  :(", f"Something went wrong ! {e}")


def loadCSV_defL():
    """If the file selected is valid this will load the file into the Treeview"""
    file_path = label_file_defl["text"]
    try:
        excel_filename= r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        messagebox.showerror("Error  :(", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        messagebox.showerror("Error  :(", "File does not exist")
        return None
    
    statusvar.set('Ready..')

    clear_data_defL()
    tv2["column"] = list(df.columns)
    tv2["show"] = "headings"
    for column in tv2["columns"]:
        tv2.heading(column, text=column) # let the column heading = column name

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv2.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None


def clear_data_defL():
    tv2.delete(*tv2.get_children())
    statusvar.set('Ready...')
    return None


def delFile_defL(): 
    global filename_defL
    try:
        if(os.path.exists(filename_defL) and os.path.isfile(filename_defL)): 
            statusvar.set(f'{os.path.basename(filename_defL)}')
            res=messagebox.askquestion('Delete file', 'Do you really want to delete ?')
            if res == 'yes' :
                os.remove(filename_defL) 
                statusvar.set(f'File has been deleted {filename_defL}')
                label_file_defl["text"] = ''
                clear_data_defL()
                tmsg.showinfo('Success  :)','File has been deleted')
                statusvar.set('Ready...')
            else: 
                statusvar.set('Ready...')
        else :
            messagebox.showerror('Error  :(','File not found')
    except:
        messagebox.showerror('Error  :(','File not selected')


def sort_defL():
    try :
        data = pd.read_csv(filename_defL) 
        #sorting data frame by Team and then By names 
        data.sort_values(["rollno"], axis=0, ascending=True, inplace=True)
    except :
        messagebox.showerror("Error  :(", "File has not selected !")

    clear_data_defL()
    tv2["column"] = list(data.columns)
    tv2["show"] = "headings"
    for column in tv2["columns"]:
        tv2.heading(column, text=column) # let the column heading = column name

    data_rows = data.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in data_rows:
        tv2.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None
    statusvar.set("Ready...")

import shutil
def downloadDeflst():
    global filename_defL
    try :
        destinationdirectory = filedialog.askdirectory(initialdir ="C:/")
        shutil.copy(filename_defL, destinationdirectory)
        messagebox.showinfo('Success  :)',"File has been downloaded")
    except :
        messagebox.showerror("Error  :(", "File not selected")
    finally :
        statusvar.set("Ready...")   

def genPer():
    import defaulterLstGenerator as dflg
    dflg.gen_Per()

def genDefL():
    import defaulterLstGenerator as dflg
    dflg.gen_Def()

def genDefNewL():
    import defaulterLstGenerator as dflg
    dflg.gen_Def_newL()


# ================================================ Message ======================================================================
# ================================================ Message ======================================================================
# ================================================ Message ======================================================================


def browseFileMail():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    
    statusvar.set("File explorer has open")
    global SendMailFilename
    SendMailFilename = filedialog.askopenfilename(initialdir="Attendance_Files/",
                                            title="Select A File",
                                            filetype=(("CSV files", "*.csv"),("All Files", "*.*")))
    
    if  SendMailFilename == '' or SendMailFilename == None :
        messagebox.showerror("Error  :(", "File not selected")
        statusvar.set("Ready...")
    else :
        try:
            msg_label_file["text"] = SendMailFilename

            statusvar.set(os.path.basename(SendMailFilename))

            attedanceFile = pd.read_csv(SendMailFilename)
            lstAtt = attedanceFile.Rollno.to_list()           
            lbl=Label(msgF2,text=f'{len(lstAtt)}',font=New1Font_sec,bg='white',anchor=W).place(x=360,y=205,width=50,height=20)
            return None
            statusvar.set("Ready...")

        except :
            messagebox.showerror("Error  :(", "Something went wrong !")
            statusvar.set("Ready...")

def sendmsgPr():
    global path

    Font_btn = ('Cursive ', 10,'bold')

    today = date.today()
    currDate = today.strftime(" %d-%b-%Y ")

    SendMailFilename1 = msg_label_file["text"]
    
    attedanceFile = pd.read_csv(SendMailFilename1)
    classSheet = pd.read_csv(f'Student_Records/{path}.csv')
    lstAtt = attedanceFile.Rollno.to_list()
    dictClassSheet = dict(zip(list(classSheet.Rollno), list(classSheet.email)))
    
    SendLectureName = os.path.basename(SendMailFilename1)
    SendLectureName = os.path.splitext(SendLectureName)[0][:-11]

    progress_bar1.start()
    progress_bar1["maximum"] = len(lstAtt)
    progress_bar1["value"] = 0


    try :   

        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login("ansarizahoor77@gmail.com","Zahoor@ansari1")

        New2Font_sec = ('Cursive ', 10,'bold')
        lbl=Label(msgF2,text='Please wait...',font=New2Font_sec,bg='white').place(x=200,y=100,width=300,height=20)
        
        for i in lstAtt:
            for x in dictClassSheet.keys():
                if i == x :
                    
                    lbl=Label(msgF2,text=f'{i}',font=New1Font_sec,bg='white',anchor=W).place(x=100,y=30,width=50,height=20)     
                    
                    progress_bar1["value"] += len(lstAtt)
                    progress_bar1.update()

                    studEmail = dictClassSheet[i]
            
                    message = f"""\
                    K.C College

                    Hi Rollno {i}. You are present in {SendLectureName} lecture on {currDate}.
                    """
                    server.sendmail('ansarizahoor77@gmail.com',studEmail,message)
        
        server.quit()

        progress_bar1.stop()

        statusvar.set("Ready...")

        messagebox.showinfo('Success  :)','Email has sent to present students')
        
        successlbl2=Label(msgF2,text='Message sent successsfully',font=New2Font_sec,bg='white',fg='red').place(x=200,y=100,width=300,height=20)

        sendmsgAb()

    except :
        messagebox.showerror("Error  :(","Check your internet connection")
        statusvar.set("Ready...")

def sendmsgAb():
    global path

    Font_btn = ('Cursive ', 10,'bold')

    today = date.today()
    currDate = today.strftime(" %d-%b-%Y ")

    SendMailFilename2 = msg_label_file["text"]
            
    attedanceFile = pd.read_csv(SendMailFilename2)

    classSheet = pd.read_csv(f'Student_Records/{path}.csv')
    lstAtt = attedanceFile.Rollno.to_list()
    dictClassSheet = dict(zip(list(classSheet.Rollno), list(classSheet.email)))

    def getList(dictClassSheet):
        list = []
        for key in dictClassSheet.keys():
            list.append(key)     
        return list
    newClassList = getList(dictClassSheet)

    for i in lstAtt:
        newClassList.remove(i)
    # print(newClassList)

    
    SendLectureName = os.path.basename(SendMailFilename2)
    SendLectureName = os.path.splitext(SendLectureName)[0][:-11]

    lbl=Label(msgF3,text=f'{len(newClassList)}',font=New1Font_sec,bg='white',anchor=W).place(x=360,y=205,width=50,height=20)

    progress_bar2.start()
    progress_bar2["maximum"] = len(newClassList)
    progress_bar2["value"] = 0

    try :   
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login("ansarizahoor77@gmail.com","Zahoor@ansari1")

        New2Font_sec = ('Cursive ', 10,'bold')
        lbl=Label(msgF3,text='Please wait...',font=New2Font_sec,bg='white').place(x=200,y=100,width=300,height=20)

        for i in newClassList:
            for j in dictClassSheet.keys():
                if i == j :
        
                    lbl=Label(msgF3,text=f'{i}',font=New1Font_sec,bg='white',anchor=W).place(x=100,y=30,width=50,height=20)     
                    
                    progress_bar2["value"] += len(newClassList)
                    progress_bar2.update()

                    studEmail = dictClassSheet[i]
   
                    message = f"""\
                    K.C College

                    Hi Rollno {i}. You are absent in {SendLectureName} lecture on {currDate}.
                    """

                    server.sendmail('ansarizahoor77@gmail.com',studEmail,message)
        
        server.quit()

        progress_bar2.stop()
        
        statusvar.set("Ready...")

        messagebox.showinfo('Success  :)','Email has sent to absent students')
        
        successlbl2=Label(msgF3,text='Message sent successsfully',font=New2Font_sec,bg='white',fg='red').place(x=200,y=100,width=300,height=20)

    except  :
        messagebox.showerror("Error  :(","Check your internet connection")
        statusvar.set("Ready...")

def  SendMail():
    statusvar.set("Sending Emails")
    global path
    path = simpledialog.askstring("","Enter Class FY/SY/TY : ")
    ClassNamelst = ['fy','FY','fY','Fy','sy','SY','sY','Sy','TY','ty','Ty','tY']
    if path == '' or path is None or path not in ClassNamelst:
        messagebox.showerror("Error  :(","Invalid Class Name")
        statusvar.set("Ready...")
    else :
        try :
            sendmsgPr()
        except :
            messagebox.showerror("Error  :(","File not selected")
            statusvar.set("Ready...")

       
# ======================================================================================================================

root = Tk()
root.state('zoomed')
root.title('AI - Attendance System')
root.iconbitmap('tkinter_image/myicon.ico')

Font_btn = font.Font(family="Ubuntu",size=10)
Font_secd = font.Font(family="@Microsoft YaHei UI",size=19)

rootColor = '#EFEFF6'
FrameClr = '#0E0C28'
BtnClr = '#242849'
FrBtnTxtClr = '#a4aadb'
BtnTxtClr = '#c0b4fc'

# =====================================================================================================================

# ---------------------------------------------------------------------Frames



def show_frame(frame):
    frame.tkraise()

full_frame_1 = Frame(root,bg=rootColor)
full_frame_2 = Frame(root,bg=rootColor)
full_frame_3 = Frame(root,bg=rootColor)
full_frame_4 = Frame(root,bg=rootColor)
full_frame_5 = Frame(root,bg=rootColor)
full_frame_6 = Frame(root,bg=rootColor)
full_frame_7 = Frame(root,bg=rootColor)

for frame in (full_frame_1,full_frame_2,full_frame_3,full_frame_4,full_frame_5,full_frame_6,full_frame_7):
    frame.place(x=250,y=50,relwidth=1,height=620)


show_frame(full_frame_2)

left_frame = Frame(root,bg=FrameClr)
left_frame.place(x=0,y=0,width=220,relheight=1)

top_frame = Frame(root,bg=rootColor)
top_frame.place(x=250,y=0,relwidth=1,height=50)

bottom_frame = Frame(root,bg=rootColor)
bottom_frame.place(x=250,y=670,relwidth=1,height=50)

# ---------------------------------------------

statusvar = StringVar()
statusvar.set("Welcome to AI - Attendance System")
sbar = Label(bottom_frame,textvariable=statusvar,font=Font_btn,anchor=W).place(x=70,y=0,width=650,height=40)

sbarText = Label(bottom_frame,text ='Status : ',font=Font_btn).place(x=5,y=0,width=60,height=40)


# --------------------------------------Left frame----------------------------------------------


# function to change properties of button on hover 
def changeOnHover(button, colorOnHover, colorOnLeave): 

	# adjusting backgroung of the widget 
	# background on entering widget 
	button.bind("<Enter>", func=lambda e: button.config( 
		background=colorOnHover,foreground='white'))

	# background color on leving widget 
	button.bind("<Leave>", func=lambda e: button.config( 
		background=colorOnLeave,foreground='#a4aadb'))


# ---------------------------------------------------------------

fontlogo = font.Font(family="@Microsoft YaHei UI",size=16,weight="bold")

leftSubframe = Frame(left_frame,bg=FrameClr).place(x=0,y=0,width=250,height=60)

logo = PhotoImage(file="tkinter_image/logo.png")
logolbl = Label(leftSubframe,image=logo,bg=FrameClr).place(x=5,y=10,width=70)
logotxtlbl = Label(leftSubframe,text='K.C College',font=fontlogo,fg='white',bg=FrameClr).place(x=80,y=20,width=120)


leftFrfontbtn = font.Font(family="@Microsoft YaHei UI",size=11,weight="bold")

newenrol = PhotoImage(file="tkinter_image/newenrol.png")
leftSubframeBtn1 = Button(left_frame,image=newenrol ,compound=LEFT, text="New Enrolment",disabledforeground='black',font=leftFrfontbtn,bd=0,cursor='hand2',bg=FrameClr,fg=FrBtnTxtClr,command=lambda: show_frame(full_frame_1),anchor=W,padx=20)
leftSubframeBtn1.place(x=0,y=90,width=220,height=60)
changeOnHover(leftSubframeBtn1, BtnClr, FrameClr) 

mrrattimg = PhotoImage(file="tkinter_image/mrr.png")
leftSubframeBtn2 = Button(left_frame,image=mrrattimg,compound=LEFT , text="Mark Attendance",font=leftFrfontbtn,bd=0,cursor='hand2',bg =FrameClr,fg=FrBtnTxtClr,command=lambda: show_frame(full_frame_2),anchor=W,padx=20)
leftSubframeBtn2.place(x=0,y=150,width=220,height=60)
changeOnHover(leftSubframeBtn2, BtnClr, FrameClr) 

viewatt = PhotoImage(file="tkinter_image/viewatt.png")
leftSubframeBtn3 = Button(left_frame,image=viewatt,compound=LEFT , text="View Attendance",font=leftFrfontbtn,bd=0,cursor='hand2',bg=FrameClr,fg=FrBtnTxtClr,command=lambda: show_frame(full_frame_3),anchor=W,padx=20)
leftSubframeBtn3.place(x=0,y=210,width=220,height=60)
changeOnHover(leftSubframeBtn3, BtnClr, FrameClr) 

dbase = PhotoImage(file="tkinter_image/dbase.png")
leftSubframeBtn5 = Button(left_frame,image=dbase,compound=LEFT , text="Database",font=leftFrfontbtn,bd=0,cursor='hand2',bg=FrameClr,fg=FrBtnTxtClr,command=lambda: show_frame(full_frame_4),anchor=W,padx=20)
leftSubframeBtn5.place(x=0,y=270,width=220,height=60)
changeOnHover(leftSubframeBtn5, BtnClr, FrameClr) 

deflist = PhotoImage(file="tkinter_image/deflist.png")
leftSubframeBtn6 = Button(left_frame,image=deflist,compound=LEFT , text="Defaulter",font=leftFrfontbtn,bd=0,cursor='hand2',bg=FrameClr,fg=FrBtnTxtClr,command=lambda: show_frame(full_frame_5),anchor=W,padx=20)
leftSubframeBtn6.place(x=0,y=330,width=220,height=60)
changeOnHover(leftSubframeBtn6, BtnClr, FrameClr) 

mssg = PhotoImage(file="tkinter_image/mssg.png")
leftSubframeBtn7 = Button(left_frame,image=mssg,compound=LEFT , text="Message",font=leftFrfontbtn,bd=0,cursor='hand2',bg=FrameClr,fg=FrBtnTxtClr,command=lambda: show_frame(full_frame_6),anchor=W,padx=20)
leftSubframeBtn7.place(x=0,y=390,width=220,height=60)
changeOnHover(leftSubframeBtn7, BtnClr, FrameClr) 

# ----------------------------------------------------------------------

curr_date = Label(top_frame,font=('@Microsoft YaHei UI ',25),background=rootColor, foreground=FrameClr)
curr_date.place(x=0,y=5,width=400,height=50)

curr_time = Label(top_frame,font=('ds-digital',30),background=rootColor, foreground=FrameClr)
curr_time.place(x=380,y=8,width=350,height=50)

curr_timee = Label(curr_time,font=('ds-digital',15),background=rootColor, foreground=FrameClr,anchor=E)
curr_timee.place(x=250,y=20,width=40,height=20)

logount_img = PhotoImage(file="tkinter_image/logout.png")
logout_btn = Button(top_frame,text='Logout ',image=logount_img,compound=RIGHT,font =('Cursive ', 11,'bold'),foreground =FrameClr ,bg=rootColor,cursor='hand2',bd=0,activeforeground='red',command=main_window)
logout_btn.place(x=1000,y=20,width=85,height=30)

topFdate()
topFtime()




# -----------------------------------------------------------------------New Enrollment Frames 1
# -----------------------------------------------------------------------New Enrollment Frames 1
# -----------------------------------------------------------------------New Enrollment Frames 1
# -----------------------------------------------------------------------New Enrollment Frames 1

newEnF1 = Frame(full_frame_1,highlightbackground='black',highlightthickness=1,bg='white')
newEnF1.place(x=40,y=40,width=250,height=250)

newEnF2 = Frame(full_frame_1,highlightbackground='black',highlightthickness=1,bg='white')
newEnF2.place(x=370,y=40,width=670,height=250)


newEnF3 = Frame(full_frame_1,highlightbackground='black',highlightthickness=1,bg='white')
newEnF3.place(x=40,y=330,width=250,height=250)

newEnF4 = Frame(full_frame_1,highlightbackground='black',highlightthickness=1,bg='white')
newEnF4.place(x=370,y=330,width=250,height=250)

# -------------------------------------

newEn1Img1 = PhotoImage(file="tkinter_image/capture.png")
newEnlblF11 = Label(newEnF1,image=newEn1Img1,bg='white').place(x=83,y=10)
newEnlblF12 = Label(newEnF1,text='Capture Image',bg='white' ,font=Font_secd).place(x=38,y=96)

Capbtn = Button(newEnF1, text="Capture",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=capImg).place(x=89,y=150,width=80,height=25)

newEnlblF3 = Label(newEnF1,text='Note : Press "c" to capture photo',fg='Red',bg='white', font=Font_btn).place(x=30,y=195)
newEnlblF4 = Label(newEnF1,text='Note : Press "s" to stop camera',fg='Red',bg='white', font=Font_btn).place(x=30,y=220)

# -------------------------------------

newEn1Img2 = PhotoImage(file="tkinter_image/uploadimg.png")
newEnlblF21 = Label(newEnF2,image=newEn1Img2,bg='white').place(x=10,y=10)
newEnlblF22 = Label(newEnF2,text='Upload Image',bg='white' ,font=Font_secd).place(x=100,y=35)


sourceLocation = StringVar() 
destinationLocation = StringVar() 

link_Label = Label(newEnF2, text ="Select The File To Upload : ",bg='white').place(x=20,y=100) 
newEnF2.sourceText = Entry(newEnF2, width = 60, textvariable = sourceLocation) 
newEnF2.sourceText.place(x=170,y=100) 
source_browseButton = Button(newEnF2, text="Browse",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=NewEnrol_SourceBrowse).place(x=570,y=100,width=80,height=25)


destinationLabel = Label(newEnF2, text ="Class Name : ", bg ="white").place(x=20,y=150) 
newEnF2.destinationText = Entry(newEnF2, width = 60, textvariable = destinationLocation) 
newEnF2.destinationText.place(x=170,y=150) 
dest_browseButton = Button(newEnF2, text ="Select",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black', command = NewEnrol_className).place(x=570,y=150,width=80,height=25)
	
copyBtn = Button(newEnF2, text ="Upload",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black', command = NewEnrol_CopyFile).place(x=570,y=200,width=80,height=25)	

newEnlbl25 = Label(newEnF2,text='Image with Student Rollno & Name  |  Format : "RollNo Name"  |  Ex: "03 Zahoor"',fg='Red',bg='white', font=Font_btn).place(x=20,y=200)

# -----------------------------------

newEn1Img3 = PhotoImage(file="tkinter_image/openImg.png")
newEnlblF31 = Label(newEnF3,image=newEn1Img3,bg='white').place(x=83,y=10)
newEnlblF32 = Label(newEnF3,text='Open Image',bg='white' ,font=Font_secd).place(x=45,y=100)
newEnlblF33 = Label(newEnF3,text='File',bg='white' ,font=Font_secd).place(x=105,y=140)

Openbtn = Button(newEnF3, text="Open file",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=openImg).place(x=89,y=190,width=80,height=25)

# --------------------------------------

newEnImg4 = PhotoImage(file="tkinter_image/imageView.png")
newEnlblF41 = Label(newEnF4,image=newEnImg4,bg='white').place(x=83,y=10)
newEnlblF42 = Label(newEnF4,text='View Image',bg='white' ,font=Font_secd).place(x=55,y=100)

Viewbtn = Button(newEnF4, text="View",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=display_img).place(x=89,y=190,width=80,height=25)



# ---------------------------------------------------------------------MarkAttendance Frames 2
# ---------------------------------------------------------------------MarkAttendance Frames 2
# ---------------------------------------------------------------------MarkAttendance Frames 2
# ---------------------------------------------------------------------MarkAttendance Frames 2


mrrF1 = Frame(full_frame_2,highlightbackground=FrameClr,highlightthickness=1,bg='white')
mrrF1.place(x=40,y=40,width=250,height=250)

mrrF2 = Frame(full_frame_2,highlightbackground=FrameClr,highlightthickness=1,bg='white')
mrrF2.place(x=370,y=40,width=250,height=250)


mrrF3 = Frame(full_frame_2,highlightbackground=FrameClr,highlightthickness=1,bg='white')
mrrF3.place(x=40,y=330,width=250,height=250)

mrrF4 = Frame(full_frame_2,highlightbackground=FrameClr,highlightthickness=1,bg='white')
mrrF4.place(x=370,y=330,width=250,height=250)

mrrF5 = Frame(full_frame_2,highlightbackground=FrameClr,highlightthickness=1,bg='white')
mrrF5.place(x=700,y=40,width=350,height=540)

# ---------------------------------------

marr1Img = PhotoImage(file="tkinter_image/face.png")
mrrlblF1 = Label(mrrF1,image=marr1Img,bg='white').place(x=83,y=10)
mrrlblF2 = Label(mrrF1,text='Mark',bg='white' ,font=Font_secd).place(x=93,y=92)
mrrlblF3 = Label(mrrF1,text='Attendance',bg='white' , font=Font_secd).place(x=50,y=122)

markAtt_btn = Button(mrrF1, text="Start",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=markAtt).place(x=89,y=165,width=80,height=25)

timeValue = StringVar()
timerCheckbtn = Checkbutton(mrrF1,text='Timer',bg='white',cursor='hand2',variable=timeValue,onvalue=1,offvalue=0,font=Font_btn)
timerCheckbtn.deselect()
timerCheckbtn.place(x=100,y=195)

mrrlblF11 = Label(mrrF1,text='Note : Press "s" to stop camera',fg='Red',bg='white', font=Font_btn).place(x=30,y=220)

# --------------------------------------

mrr2Img = PhotoImage(file="tkinter_image/csv.png")
mrr2lblF21 = Label(mrrF2,image=mrr2Img,bg='white').place(x=170,y=5)
mrr2lblF22 = Label(mrrF2,text='Import File',bg='white', font=Font_secd).place(x=10,y=20)

# Frame for open file dialog
file_frame = LabelFrame(mrrF2, text=" Open File ",bg='white')
file_frame.place(height=80, width=230, y=95, x=10)

# The file/file path text
label_file = Label(file_frame, text="No File Selected",bg='white')
label_file.place(rely=0 ,relx=0)

mrrLoadCSVbtn = Button(mrrF2, text="Load",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black', command=lambda: mark_LoadCSV() ).place(x=30,y=195,width=80,height=25)
mrrBrowsebtn = Button(mrrF2, text="Browse",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black', command=lambda: mark_browseFile() ).place(x=140,y=195,width=80,height=25)

# -----------------------------------

mrr3Img = PhotoImage(file="tkinter_image/db.png")
mrr3lblF31 = Label(mrrF3,image=mrr3Img,bg='white').place(x=170,y=20)
mrr3lblF32 = Label(mrrF3,text='Store into',bg='white', font=Font_secd).place(x=20,y=10)
mrr3lblF33 = Label(mrrF3,text='Database',bg='white', font=Font_secd).place(x=20,y=40)

mrr3DBbtnF31 = Button(mrrF3, text="First Year",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=UploaddbFy).place(x=80,y=100,width=100,height=25)
mrr3DBbtnF32 = Button(mrrF3, text="Second Year",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=UploaddbSy).place(x=80,y=150,width=100,height=25)
mrr3DBbtnF33 = Button(mrrF3, text="Third Year",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',state=DISABLED).place(x=80,y=200,width=100,height=25)


# ---------------------------
mrrViewFilebtn = Button(mrrF4, text="View Files",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=mark_openCSV).place(x=72,y=30,width=110,height=25)
mrrSortbtn = Button(mrrF4, text="Sort ASC",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=mark_sort).place(x=72,y=80,width=110,height=25)
mrrAbsentbtn = Button(mrrF4, text="Absent",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=mark_absentStud).place(x=72,y=130,width=110,height=25)
mrrDelbtn = Button(mrrF4, text="Delete",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='red',command=mark_delFile).place(x=30,y=195,width=80,height=25)
mrrClrbtn = Button(mrrF4, text="Clear",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black', command=lambda: clear_data()).place(x=140,y=195,width=80,height=25)

# ---------------------------------------

## Treeview Widget
tv1 = ttk.Treeview(mrrF5)
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

treescrolly = Scrollbar(mrrF5, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = Scrollbar(mrrF5, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget


# ---------------------------------------------------------------------ViewAttendance Frames 3
# ---------------------------------------------------------------------ViewAttendance Frames 3
# ---------------------------------------------------------------------ViewAttendance Frames 3
# ---------------------------------------------------------------------ViewAttendance Frames 3
# ---------------------------------------------------------------------ViewAttendance Frames 3


viewAttF1 = Frame(full_frame_3,highlightbackground=FrameClr,highlightthickness=1,bg='white')
viewAttF1.place(x=40,y=40,width=250,height=250)

viewAttF2 = Frame(full_frame_3,highlightbackground=FrameClr,highlightthickness=1,bg='white')
viewAttF2.place(x=370,y=40,width=680,height=550)


viewAttImg1 = PhotoImage(file="tkinter_image/viewdb.png")
viewAttlbl1 = Label(viewAttF1,image=viewAttImg1,bg='white').place(x=160,y=20)
viewAttlbl2 = Label(viewAttF1,text='Fetch From',bg='white', font=Font_secd).place(x=10,y=10)
viewAttlbl3 = Label(viewAttF1,text='Database',bg='white', font=Font_secd).place(x=10,y=40)

viewDBbtnFY = Button(viewAttF1, text="First Year",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=FetchdbFy).place(x=80,y=100,width=100,height=25)
viewDBbtnSY = Button(viewAttF1, text="Second Year",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=FetchdbSy).place(x=80,y=150,width=100,height=25)
viewDBbtnTY = Button(viewAttF1, text="Third Year",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',state=DISABLED).place(x=80,y=200,width=100,height=25)

TableMargin = Frame(viewAttF2, width=500)
TableMargin.pack(side=TOP)
# scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, column=("c1", "c2", "c3","c4","c5"), show='headings',height=400, selectmode="extended", yscrollcommand=scrollbary.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
# scrollbarx.config(command=tree.xview)
# scrollbarx.pack(side=BOTTOM, fill=X)
tree.column("#1", anchor=CENTER,stretch=NO, width=110)
tree.heading("#1", text="ID")
tree.column("#2", anchor=CENTER,stretch=NO, width=110)
tree.heading("#2", text="ROLLNO")
tree.column("#3", anchor=CENTER,stretch=NO, width=150)
tree.heading("#3", text="NAME")
tree.column("#4", anchor=CENTER,stretch=NO, width=150)
tree.heading("#4", text="DATE")
tree.column("#5", anchor=CENTER,stretch=NO, width=150)
tree.heading("#5", text="TIME")
tree.pack()

# ---------------------------------------------------------------------Database Frames 4
# ---------------------------------------------------------------------Database Frames 4
# ---------------------------------------------------------------------Database Frames 4
# ---------------------------------------------------------------------Database Frames 4
# ---------------------------------------------------------------------Database Frames 4


dblbl = Frame(full_frame_4,highlightbackground=FrameClr,highlightthickness=1,bg='white')
dblbl.place(x=20,y=50,width=350,height=180)

dblblImg1 = PhotoImage(file="tkinter_image/fetchdb.png")
dblbl1 = Label(dblbl,image=dblblImg1,bg='white').place(x=220,y=30)
dblbl2 = Label(dblbl,text='Fetch From',bg='white', font=Font_secd).place(x=10,y=20)
dblbl3 = Label(dblbl,text='Database',bg='white', font=Font_secd).place(x=10,y=50)

dbBbtn1 = Button(dblbl, text="First Year",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=editdbFy).place(x=10,y=120,width=100,height=25)
dbBbtn2 = Button(dblbl, text="Second Year",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=editdbSy).place(x=120,y=120,width=100,height=25)
dbBbtn3 = Button(dblbl, text="Third Year",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',state= DISABLED).place(x=230,y=120,width=100,height=25)


# -----------------------------------------------------------------------Defualter Frames 5
# -----------------------------------------------------------------------Defualter Frames 5
# -----------------------------------------------------------------------Defualter Frames 5
# -----------------------------------------------------------------------Defualter Frames 5


defF1 = Frame(full_frame_5,highlightbackground='black',highlightthickness=1,bg='white')
defF1.place(x=40,y=40,width=250,height=250)


defF2 = Frame(full_frame_5,highlightbackground='black',highlightthickness=1,bg='white')
defF2.place(x=370,y=40,width=690,height=370)

defF3 = Frame(full_frame_5,highlightbackground='black',highlightthickness=1,bg='white')
defF3.place(x=40,y=330,width=250,height=250)

defF4 = Frame(full_frame_5)
defF4.place(x=370,y=430,width=690,height=150)

# -------------------------------------------------------

def1Img = PhotoImage(file="tkinter_image/csv.png")
def1lbl1 = Label(defF1,image=def1Img,bg='white').place(x=170,y=5)
def1lbl2 = Label(defF1,text='Import File', font=Font_secd,bg='white').place(x=10,y=20)

# Frame for open file dialog
file_frame_del = LabelFrame(defF1, text=" Open File ",bg='white')
file_frame_del.place(height=80, width=230, y=95, x=10)

# The file/file path text
label_file_defl = Label(file_frame_del, text="No File Selected",bg='white')
label_file_defl.place(rely=0 ,relx=0)

defLoadbtn = Button(defF1, text="Load",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black', command= loadCSV_defL ).place(x=30,y=195,width=80,height=25)
defBrowsebtn = Button(defF1, text="Browse",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black', command= browseFile_defL ).place(x=140,y=195,width=80,height=25)

# -------------------------------------------------------------------------

tv2 = ttk.Treeview(defF2)
tv2.place(relheight=1, relwidth=1,x=1,y=0) # set the height and width of the widget to 100% of its container (frame1).
treescrolly = Scrollbar(defF2, orient="vertical", command=tv2.yview) # command means update the yaxis view of the widget
treescrollx = Scrollbar(defF2, orient="horizontal", command=tv2.xview) # command means update the xaxis view of the widget
tv2.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview w idget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget

# ---------------------------------------------------------------------

def3Img = PhotoImage(file="tkinter_image/downdb.png")
def3lbl1 = Label(defF3,image=def3Img,bg='white').place(x=180,y=15)
def3lbl2 = Label(defF3,text='Download', font=Font_secd,bg='white').place(x=10,y=7)
def3lbl3 = Label(defF3,text='File', font=Font_secd,bg='white').place(x=10,y=42)

mrr3DBbtn = Button(defF3, text="First Year",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=downloaddbFy).place(x=80,y=100,width=100,height=25)
mrr3DBbtn = Button(defF3, text="Second Year",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=downloaddbSy).place(x=80,y=150,width=100,height=25)
mrr3DBbtn = Button(defF3, text="Third Year",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',state=DISABLED).place(x=80,y=200,width=100,height=25)


deflblfr = LabelFrame(defF4,text=' Defaultor List ').place(x=10,y=10,width=670,height=140)


defPerbtn = Button(defF4, text="Percentage",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=genPer).place(x=50,y=50,width=110,height=25)
defPerGenbtn = Button(defF4, text="Pre Generate",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=genDefL).place(x=200,y=50,width=110,height=25)
defGenbtn = Button(defF4, text="Generate",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=genDefNewL).place(x=360,y=50,width=110,height=25)
defDownloadbtn = Button(defF4, text="Download",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=downloadDeflst).place(x=510,y=50,width=110,height=25)

defViewFilebtn = Button(defF4, text="View Files",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=openCSV_defL).place(x=50,y=100,width=110,height=25)
defSortbtn = Button(defF4, text="Sort ASC",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black',command=sort_defL).place(x=200,y=100,width=110,height=25)
defClrbtn = Button(defF4, text="Clear",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='black', command=lambda: clear_data_defL() ).place(x=360,y=100,width=110,height=25)
defDelbtn = Button(defF4, text="Delete",font=Font_btn,bd=0,cursor='hand2',bg=BtnTxtClr,fg='red',command=delFile_defL).place(x=510,y=100,width=110,height=25)

# -----------------------------------------------------------------------Message Frames 5
# -----------------------------------------------------------------------Message Frames 5
# -----------------------------------------------------------------------Message Frames 5
# -----------------------------------------------------------------------Message Frames 5
New1Font_sec = ('Cursive ', 15,'bold')
New2Font_sec = ('Cursive ', 10,'bold')
pri1Font = font.Font(family="@Microsoft YaHei UI",size=10,weight="bold") 
pri2Font = font.Font(family="@Microsoft YaHei UI",size=15) 
secFont = ('Ubuntu', 10) 

msgF1 = Frame(full_frame_6,highlightbackground='black',highlightthickness=1,bg='white')
msgF1.place(x=40,y=40,width=250,height=250)

msgF2 = Frame(full_frame_6,highlightbackground='black',highlightthickness=1,bg='white')
msgF2.place(x=370,y=40,width=670,height=250)

msgF3 = Frame(full_frame_6,highlightbackground='black',highlightthickness=1,bg='white')
msgF3.place(x=370,y=330,width=670,height=250)



msgImg = PhotoImage(file="tkinter_image/csv.png")
msglbl1 = Label(msgF1,image=msgImg,bg='white').place(x=170,y=5)
msglbl2 = Label(msgF1,text='Load File',bg='white', font=Font_secd).place(x=10,y=20)

# Frame for open file dialog
msgfile_frame = LabelFrame(msgF1, text=" Open File ",bg='white')
msgfile_frame.place(height=80, width=230, y=95, x=10)

# The file/file path text
msg_label_file = Label(msgfile_frame, text="No File Selected",bg='white')
msg_label_file.place(rely=0 ,relx=0)


# -------

lbl11=Label(msgF2,text='Rollno : ',font=New1Font_sec,bg='white').place(x=20,y=25)

progress_bar1 = ttk.Progressbar(msgF2, orient = 'horizontal', length = 620, mode = 'determinate')
progress_bar1.place(x=20,y=70)


lbl12=Label(msgF2,text='Total number of present students : ',font=New1Font_sec,bg='white').place(x=20,y=200)

# -----------

lbl21=Label(msgF3,text='Rollno : ',font=New1Font_sec,bg='white').place(x=20,y=25)

progress_bar2 = ttk.Progressbar(msgF3, orient = 'horizontal', length = 620, mode = 'determinate')
progress_bar2.place(x=20,y=70)


lbl22=Label(msgF3,text='Total number of absent students : ',font=New1Font_sec,bg='white').place(x=20,y=200)

 
Browsebtn = Button(msgF1, text="Browse",font=Font_btn,bd=0,cursor='hand2',fg='#0E0C28',bg=BtnTxtClr, command=browseFileMail).place(x=140,y=195,width=80,height=25)
Sendbtn = Button(msgF1, text="Mail",font=Font_btn,bd=0,cursor='hand2',fg='#0E0C28',bg=BtnTxtClr, command=SendMail ).place(x=30,y=195,width=80,height=25)


root.mainloop()
