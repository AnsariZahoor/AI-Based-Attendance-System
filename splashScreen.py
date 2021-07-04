from tkinter import *
from tkinter import ttk
import time



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        width = 1250
        height = 730
        self.overrideredirect(True)
        self.geometry('%dx%d+%d+%d' % (width*0.6, height*0.55, width*0.25, height*0.20))
        self.resizable(0,0)
        self.overrideredirect(True)

        self.frame=Frame(self,bg=None)
        self.frame.place(x=0,y=-2,relwidth=1,relheight=1)

        self.screen = PhotoImage(file="tkinter_image/SplashScreen.png")
        screen = Label(self.frame,image=self.screen,bg='#EFEFF6').place(x=0,y=0)

        self.progressBar()
       
        
    def progressBar(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("grey.Horizontal.TProgressbar", background='#0E0C28', troughcolor='white',bordercolor='white',lightcolor='#0E0C28')
        self.progress_bar = ttk.Progressbar( self.frame, orient = 'horizontal', length = 750, mode = 'determinate',style='grey.Horizontal.TProgressbar')
        self.progress_bar.place(x=0,y=392)



    def run_progressbar(self):
        
        self.progress_bar["maximum"] = 100
        for i in range(100):
            time.sleep(0.1)
            self.progress_bar["value"] = i
            self.progress_bar.update()
        self.progress_bar["value"] = 0

        Root.destroy(self)
        import main    
     

root = Root()
root.run_progressbar()
root.mainloop()