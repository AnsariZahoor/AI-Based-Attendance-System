from tkinter import ttk,simpledialog,filedialog, messagebox
import tkinter.messagebox as tmsg
from collections import Counter
import pandas as pd
import csv



def gen_Per():
    global filepath
    global userFilename

    ClassNamelst = ['fy','FY','fY','Fy','sy','SY','sY','Sy','TY','ty','Ty','tY']
    filepath = simpledialog.askstring("","Enter Class FY/SY/TY : ")

    if filepath == '' or filepath is None or filepath not in ClassNamelst:
        messagebox.showerror("Error  :(","Invalid Class Name")

    else :
        userFilename= simpledialog.askstring("","Enter subject name : ")
        if userFilename == '' or userFilename is None:
            messagebox.showerror("Error  :(","Subject name not entered")

        else :
            defFilename = filedialog.askopenfilename(initialdir="Defaulter_List",
                                                title="Select A File",
                                                filetype=(("CSV files", "*.csv"),("All Files", "*.*")))
            if  defFilename == '' or defFilename == None :
                messagebox.showerror("Error  :(", "File not selected")

            else :

                totalOnOfLecture = simpledialog.askinteger("","Total no. of lecture : ")
                if  totalOnOfLecture == '' or totalOnOfLecture == None :
                    messagebox.showerror("Error  :(", "Please enter total no of lecture held")

                else :
                    try :

                        dbAttFile = pd.read_csv (f'{defFilename}') 
                        dbAttFile = dbAttFile['rollno'].tolist() 
                        dbAttFile.sort() 

                        # ---------------------------------------------------------------
                        #load student record csv file
                        studentRecord = pd.read_csv(f'Student_Records/{filepath}.csv')   
                        StudentData = dict(zip(studentRecord.Rollno,studentRecord.Name))
                        # print(StudentData)
                        #print name from dict
                        # print(StudentData.values())

                        #initialize rollno with empty list & Lecture attended pre student with dict
                        rollNo = []
                        lectureAttPreStud = {}

                        for x in range(1,dbAttFile[-1]+1):
                            #append present roll no in list
                            rollNo.append(x)
                            #count lecture attended by student through rollno of student 
                            d = Counter(dbAttFile)
                            # print(x, d[x])
                            #append counted no. in dict wiht rollno and total no. of lecture attend
                            lectureAttPreStud.update({x:d[x]}) 
                        # print(lectureAttPreStud)
                        # print(rollNo)


                        StudentDataName = []
                        for key in StudentData.keys():
                            if key in rollNo:
                                StudentDataName.append(StudentData[key])
                            else:
                                break
                        # print(StudentDataName)


                        i = 0 
                        Percent = {}
                        for numbers in lectureAttPreStud.values():
                            i += 1
                            Percent.update({ i : (numbers)/(totalOnOfLecture)*100})
                        # print(Percent)


                            # --------------------------------------------------------     


                        header = ['Rollno','Name','Attend','Percentage','Defaultor']

                        with open(f'Defaulter_List/{filepath}/{userFilename} defaulter.csv', "w", newline='') as f:
                            writer = csv.writer(f, delimiter=',')
                            writer.writerow(header)

                        Default = ['NaN'] * (dbAttFile[-1])


                        # dictionary of lists   
                        newDict = {'Rollno':rollNo, 'Name ': StudentDataName, 'Attend':lectureAttPreStud.values(),'Percentage': Percent.values(),'Defaulter':Default}   
                                            
                        newData = pd.DataFrame(newDict)  

                        # saving the dataframe  
                        newData.to_csv(f'Defaulter_List/{filepath}/{userFilename} defaulter.csv',index = False,header = True)
                        # print('Percentage File has been created...')
                        tmsg.showinfo('Success  :)','Percentage File has been created')
                    except Exception as e:
                        print('Error : ',e)
                        messagebox.showerror("Error  :(", "Something went wrong !")



def gen_Def():
    global filepath
    global userFilename
    global filename
    filename = filedialog.askopenfilename(initialdir="Defaulter_List",
                                          title="Select A File",
                                          filetype=(("CSV files", "*.csv"),("All Files", "*.*")))    
    if  filename == '' or filename == None :
        messagebox.showerror("Error  :(", "File not selected")
    else :
        try :

            df = pd.read_csv (filename)  
            df['Defaulter'] = df['Percentage'].apply(lambda x: 'True' if x >= 70 else 'False') 
            df.to_csv(f'Defaulter_List/{filepath}/{userFilename} defaulter.csv',index = False,header = True)
            # print('File has been created...')
            tmsg.showinfo('Success  :)','File has been updated')
        except:
            messagebox.showerror("Error  :(", "File not selected")




def gen_Def_newL():
    global filename
    global filepath
    global userFilename
    try :
        df = pd.read_csv (filename)  
        index_names = df[ df['Defaulter'] == True ].index 
    
        # drop these row indexes from dataFrame 
        df.drop(index_names, inplace = True)
        df.to_csv(f'Defaulter_List/{filepath}/{userFilename} defaulter.csv',index = False,header = True)

        df = pd.read_csv (filename)  
        df.drop(df.columns[4], axis = 1, inplace = True) 
        df.to_csv(f'Defaulter_List/{filepath}/{userFilename} defaulter.csv',index = False,header = True)
        # print('File File has been created...')
        tmsg.showinfo('Success  :)','Defaulter List has been created')

    except :
        messagebox.showerror("Error  :(", "File not selected")