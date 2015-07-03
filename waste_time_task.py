import Tkinter as tk
from study_task import *
import task_disp

class waste_time(study_task):
    def __init__(self, root, *args, **kwargs):
        study_task.__init__(self, root, *args, **kwargs)

    def init_args(self):
        self.program_choice = tk.StringVar()

        data_fh = open('waste_time_info.txt')
        self.data = eval(data_fh.read())

        self.programs = self.data.keys()
        self.program_choice.set(self.programs[0])


    def furnish_options(self):
        self.specify_type('Wast', bg = "#F0B6F0", foreground = "#751975")
        self.add_programs()

    def add_programs(self):

        self.program_mb = tk.Menubutton(self, text = 'Choose Program',width = 20)
        mb = self.program_mb
        mymenu = tk.Menu(mb)
        mb['menu'] = mymenu
        
        for program in self.programs:
            mymenu.add_radiobutton(label=program,variable = self.program_choice, command = self.disp_info)
        mb.grid(row = 0, column = 1)
        Label(self, width = 21).grid(row=0, column = 2)
        ##to implement selection functionality

    def disp_info(self):

        self.myprogram = self.program_choice.get()
        self.passprogram = self.myprogram
        self.course_mb.config(text = self.myprogram)


    def get_label(self):
        #print "mysubject is %s"%(self.passsubject )
        #print "mycourse is %s"%(self.passcourse)
        try:
            return self.data[self.passprogram][0] #it appears to be a bug of python
        except AttributeError:
            return "Rubbish_Input"
            
    def get_subject_table_name(self):
        try:
            return self.data[self.passprogram][self.passcourse][1]
        except AttributeError:
            return "Rubbish_Input"

    def get_task_category(self):
        return 'waste_time'
   
#-------------------------------------------------- custom info from xml 
    def pass_info(self):
        pass

if __name__=="__main__":
    root = tk.Tk()
    root.geometry('1200x900')
    root.config(bg = 'grey')
    panA = Frame(root)
    panB = Frame(root)
    task_disp.task_disp.pool = panB
    a = waste_time(panA)
    panA.pack(side = 'left',anchor = 'nw')
    panB.pack(side = 'left', anchor = 'nw')
    root.mainloop()


