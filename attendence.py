# import library
import face_recognition
import numpy as np
import cv2
import os

from datetime import datetime
from datetime import date
from time import time
from tkinter import *

import smtplib
import pandas as pd 
from tkinter import *
from tkinter import ttk
import time

from tkinter.ttk import Progressbar
from tkinter import messagebox
from tkinter import font
from tkinter import simpledialog,messagebox


def start():
    today = date.today()
    global input_filename
    input_filename = simpledialog.askstring("","Enter subject name : ")

    if input_filename == '' or input_filename is None:
        messagebox.showerror("Error  :(","Subject name not entered")

    else :
        ClassNamelst = ['fy','FY','fY','Fy','sy','SY','sY','Sy','TY','ty','Ty','tY']
        global file_path
        file_path = simpledialog.askstring("","Enter Class FY/SY/TY : ")

        if file_path == '' or file_path is None or file_path not in ClassNamelst:
            messagebox.showerror("Error  :(","Invalid Class Name")

        else :

            try : 
                filename = input_filename + today.strftime(" %d-%b-%Y")
                # dataset images path -
                path = f'Image_Dataset/{file_path}'
                images = []
                className = []
                roll =[]
                myList = os.listdir(path)
                # print(myList)

                for cl in myList: 
                    #cls is name of img
                    curImg = cv2.imread(f'{path}/{cl}')
                    images.append(curImg)
                    #First element of img
                    className.append(os.path.splitext(cl)[0])

                # print(className)

                # ------------------------------------------------------

                #Finding encodings
                def findEncodings(images):
                    encodeList = []
                    for img in images:
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        encode = face_recognition.face_encodings(img)[0]
                        encodeList.append(encode)
                    return encodeList
                # ---------------------------------------------------------

                global CSVfilename
                CSVfilename = f'Attendance_Files/{file_path}/{filename}.csv'
                #Mark Attendence
                with open(CSVfilename,'x') as f:
                    f.write('Rollno,Name,Date,Time')


                def markAttendance(name,rollno):
                    with open(CSVfilename,'r+') as f:
                        myDataList = f.readlines()
                        nameList = []
                        for line in myDataList:
                            entry = line.split(',')
                            nameList.append(entry[0])
                        if (name and rollno) not in nameList :
                            now = datetime.now()
                            dtString = now.strftime('%H:%M:%S')
                            currDate = today.strftime("%d-%b-%Y")
                            f.writelines(f'\n{rollno},{name},{currDate},{dtString}')

                # -----------------------------------------------------
                encodeListKnown = findEncodings(images)
                # print(len(encodeListKnown))
                # print('Encoding Completed....')

            

                #Take img thorugh webcam
                cap = cv2.VideoCapture(0) #0 is id

                while True:
                    success, img = cap.read()
                    # resize img
                    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
                    # convert into rgb
                    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

                    faceCurrFrame = face_recognition.face_locations(imgS)
                    encodesCurrFrame = face_recognition.face_encodings(imgS,faceCurrFrame)

                    for encodeFace, faceLoc in zip(encodesCurrFrame,faceCurrFrame):
                        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
                        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
                        # print(faceDis)
                        matcheIndex = np.argmin(faceDis)


                        if matches[matcheIndex]:
                            name = className[matcheIndex].upper()
                            # print(name)
                            y1,x2,y2,x1 = faceLoc
                            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                            # color , thickness
                            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

                            markAttendance(name[3:],name[0:2])

                    cv2.imshow('Attendance',img)
                    if cv2.waitKey(1) & 0xFF == ord('s'):   
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Success  :)','Attendance has been marked')
                veriftySend()
            except Exception as es:
                messagebox.showerror("Error  :(",f"Error due to: {str(es)}")


def startByTime():
    today = date.today()
    global input_filename
    input_filename = simpledialog.askstring("","Enter subject name : ")

    if input_filename == '' or input_filename is None :
        messagebox.showerror("Error  :(","Subject name not entered")

    else:
        ClassNamelst = ['fy','FY','fY','Fy','sy','SY','sY','Sy','TY','ty','Ty','tY']
        global file_path
        file_path = simpledialog.askstring("","Enter Class FY/SY/TY : ")
        if file_path == '' or file_path is None or file_path not in ClassNamelst:
            messagebox.showerror("Error  :(","Invalid Class Name")

        else :

            user_input = simpledialog.askinteger("","Enter Time in Minutes")
            
            if user_input == '' or user_input is None :
                messagebox.showerror("Error  :(","Time has not set")

            else :
                try : 
                    filename = input_filename + today.strftime(" %d-%b-%Y")

                    # dataset images path -
                    path = f'Image_Dataset/{file_path}'
                    images = []
                    className = []
                    roll =[]
                    myList = os.listdir(path)
                    # print(myList)

                    for cl in myList: 
                        #cls is name of img
                        curImg = cv2.imread(f'{path}/{cl}')
                        images.append(curImg)
                        #First element of img
                        className.append(os.path.splitext(cl)[0])

                    # print(className)

                    # ------------------------------------------------------

                    #Finding encodings
                    def findEncodings(images):
                        encodeList = []
                        for img in images:
                            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                            encode = face_recognition.face_encodings(img)[0]
                            encodeList.append(encode)
                        return encodeList
                    # ---------------------------------------------------------
                    global CSVfilename
                    CSVfilename = f'Attendance_Files/{file_path}/{filename}.csv'
                    #Mark Attendence
                    with open(CSVfilename,'x') as f:
                        f.write('Rollno,Name,Date,Time')

                    def markAttendance2(name,rollno):
                        with open(CSVfilename,'r+') as f:
                            myDataList = f.readlines()
                            nameList = []
                            for line in myDataList:
                                entry = line.split(',')
                                nameList.append(entry[0])
                            if (name and rollno) not in nameList :
                                now = datetime.now()
                                dtString = now.strftime('%H:%M:%S')
                                currDate = today.strftime("%d-%b-%Y")
                                f.writelines(f'\n{rollno},{name},{currDate},{dtString}')
                    # -----------------------------------------------------
                    encodeListKnown = findEncodings(images)
                    # print(len(encodeListKnown))
                    # print('Encoding Completed....')


                    start_time = time.time()
                    print(start_time)
                    capture_duration= int(user_input)*60
                    print(capture_duration)
                    #Take img thorugh webcam
                    cap = cv2.VideoCapture(0) #0 is id

                    while  ( time.time() - start_time ) < capture_duration :
                        success, img = cap.read()
                        # resize img
                        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
                        # convert into rgb
                        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

                        faceCurrFrame = face_recognition.face_locations(imgS)
                        encodesCurrFrame = face_recognition.face_encodings(imgS,faceCurrFrame)

                        for encodeFace, faceLoc in zip(encodesCurrFrame,faceCurrFrame):
                            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
                            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
                            # print(faceDis)
                            matcheIndex = np.argmin(faceDis)


                            if matches[matcheIndex]:
                                name = className[matcheIndex].upper()
                                print(name)
                                y1,x2,y2,x1 = faceLoc
                                y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                                                                    # color , thickness
                                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

                                markAttendance2(name[3:],name[0:2])

                        cv2.imshow('Attendance',img)
                        if cv2.waitKey(1) & 0xFF == ord('s'):
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo('Success  :)','Attendance has been marked')
                    veriftySend()
                except Exception as es:
                    print('Error : ', es)
                    messagebox.showerror("Error  :(",f"Error due to: {str(es)}")

def veriftySend():
    res=messagebox.askquestion('Send E-Mail', '''Do you want to send emails ? Note : Connect to the internet''')
    if res == 'yes' :
        SendMail()



def SendMail():
    class Root(Tk):
        def __init__(self):
            global CSVfilename
            super(Root, self).__init__()

            Font_btn = ('Cursive ', 10,'bold')

            self.title("Sending E-mails...")
            self.geometry('300x200+100+100')
            self.resizable(0,0)
            self.config(bg='#EFEFF6')
            self.focus_force()
            self.grab_set()
            self.iconbitmap('tkinter_image/mail.ico')

            attedanceFile = pd.read_csv(CSVfilename)
            lstAtt = attedanceFile.Rollno.to_list()

            self.lbl=Label(self,text='Please wait...',font=Font_btn)
            self.lbl.place(x=100,y=60)

            self.lbl=Label(self,text=f'Total number of present students : {len(lstAtt)}',font=Font_btn)
            self.lbl.place(x=10,y=170)

            self.progressBar()
            
            

        def progressBar(self):            
            self.progress_bar = ttk.Progressbar(self, orient = 'horizontal', length = 280, mode = 'determinate')
            self.progress_bar.place(x=10,y=40)
            self.sendMailPr()
            
        def sendMailPr(self):

            Font_btn = ('Cursive ', 10,'bold')

            global CSVfilename
            global input_filename
            global file_path

            path = f'Student_Records/{file_path}.csv'

            today = date.today()
            currDate = today.strftime(" %d-%b-%Y ")

            
              
            attedanceFile = pd.read_csv(CSVfilename)
            classSheet = pd.read_csv(path)
            lstAtt = attedanceFile.Rollno.to_list()
            # print(lstAtt)

            dictClassSheet = dict(zip(list(classSheet.Rollno), list(classSheet.email)))
            # print(dictClassSheet)

            self.progress_bar.start()
            self.progress_bar["maximum"] = len(lstAtt)
            self.progress_bar["value"] = 0

            try :
                server = smtplib.SMTP_SSL('smtp.gmail.com',465)
                server.login("ansarizahoor77@gmail.com","Zahoor@ansari1")


                for i in lstAtt:
                    for x in dictClassSheet.keys():
                        if i == x :
                            self.lbl=Label(self,text=f'Rollno : {i} ',font=Font_btn).place(x=10,y=10)
                            
                            self.progress_bar["value"] += len(lstAtt)
                            self.progress_bar.update()

                            studEmail = dictClassSheet[i]
                        
                            message = f"""\
                            K.C College

                            Hi Rollno {i}. You are present in {input_filename} lecture on {currDate}.
                            """
                            server.sendmail('ansarizahoor77@gmail.com',studEmail,message)

            except Exception as e :
                print(e)
                messagebox.showerror("Error  :(","Check your internet connection")
                Root.destroy(self)
            finally : 
                server.quit()
                self.progress_bar.stop()
                self.sendMailAb()
                

        def sendMailAb(self):
            global CSVfilename
            global input_filename
            global file_path

            path = f'Student_Records/{file_path}.csv'

            today = date.today()
            currDate = today.strftime(" %d-%b-%Y ")

            self.progress_bar.start()
            Font_btn = ('Cursive ', 10,'bold')
              
            attedanceFile = pd.read_csv(CSVfilename)
            classSheet = pd.read_csv(path)
            lstAtt = attedanceFile.Rollno.to_list()
            # print(lstAtt)

            dictClassSheet = dict(zip(list(classSheet.Rollno), list(classSheet.email)))
        
            def getList(dictClassSheet):
                list = []
                for key in dictClassSheet.keys():
                    list.append(key)     
                return list
            newClassList = getList(dictClassSheet)
            # print(newdict)

            for i in lstAtt:
                newClassList.remove(i)
            # print(newClassList)


            self.lbl=Label(self,text=f'Total number of absent students : {len(newClassList)}',font=Font_btn)
            self.lbl.place(x=10,y=170)

            self.progress_bar["maximum"] = len(newClassList)

            self.progress_bar["value"] = 0

            try :
                server = smtplib.SMTP_SSL('smtp.gmail.com',465)
                server.login("ansarizahoor77@gmail.com","Zahoor@ansari1")

                for i in newClassList:
                    for j in dictClassSheet.keys():
                        if i == j :
                            self.lbl=Label(self,text=f'Rollno : {i} ',font=Font_btn).place(x=10,y=10)
                            
                            self.progress_bar["value"] += len(lstAtt)
                            self.progress_bar.update()

                            studEmail = dictClassSheet[i]
                  
                            message = f"""\
                            K.C College

                            Hi Rollno {i}. You are absent in {input_filename} lecture on {currDate}.
                            """
                            server.sendmail('ansarizahoor77@gmail.com',studEmail,message)

            except Exception as e :
                print(e)
                messagebox.showerror("Error  :(","Check your internet connection")
                Root.destroy(self)
            finally : 
                server.quit()
                self.progress_bar.stop()
                messagebox.showinfo('Success  :)','Email has been sent successfully')
                Root.destroy(self)


    root = Root()
    root.mainloop()
