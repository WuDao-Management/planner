import Tkinter as tk
from abstract_task import *
import task_disp

class study_task(abstract_task):
    

    def __init__(self, root ,*args, **kwargs):
        self.root = root
        abstract_task.__init__(self, root,  bd=2,   relief=tk.RAISED)
        self.init_args()
        self.furnish_options()
        
    def init_args(self):
        #subjecgts button and course choice
        self.subject_choice = tk.StringVar()
        self.subjects = ['Math', 'Udacity', 'Programming']
        self.courses= {'Math':[('Birchoff Algebra', 'B\n Algebra') 
                        ,('Kolmogorov Real Analysis', 'K\n Analysis')]
                , 'Udacity': [('Intro To Data Science','Intro\n Data')
                            , ('Data Wrangering with MangoDB', 'Data\n Wrangle')]
                , 'Programming':[('Monitor', 'Monitor')]}
        self.course_choice = tk.StringVar()
        self.detail = tk.StringVar()
        self.expTime = tk.StringVar()

    def furnish_options(self):
        self.specify_type('work',bg='#ffffBB', foreground = '#3333aa')
        self.add_subjects()
        self.duration_details(self.expTime, self.detail)

#####################################################################below are functionalities
#----------------------------------------------
    def add_subjects(self):
        self.subject_mb = tk.Menubutton(self, text = 'Choose Subject',width = 20)
        mb = self.subject_mb
        mymenu = tk.Menu(mb)
        mb['menu'] = mymenu
        for subject in self.subjects:
            mymenu.add_radiobutton(label=subject,variable = self.subject_choice , command = self.init_course)

        ##to implement selection functionality
        mb.grid(row = 0, column = 1)
        self.course_mb = tk.Menubutton(self, text = 'Choose Course', width = 20)
        self.course_mb.grid(row = 0, column = 2)

#------------------------------------init course selection
    def init_course(self):
        self.subject_mb.config(text = self.subject_choice.get())
        
        mb = self.course_mb
        mymenu = tk.Menu(mb)
        mb['menu'] = mymenu
        mycourses = self.courses[self.subject_choice.get()]
        for course in mycourses:
            mymenu.add_radiobutton(label=course,variable = self.course_choice , command = self.disp_info)
            
        

    def disp_info(self):
        self.course_mb.config(text = self.course_choice.get())
        pass


#-------------------------------------------------- custom info from xml 
    def pass_info(self):
        pass


#-------------------------------------------------- communication with mysql and task display
    
    


if __name__=="__main__":
    root = tk.Tk()
    root.geometry('1200x900')
    root.config(bg = 'grey')
    panA = Frame(root)
    panB = Frame(root)
    task_disp.pool = panB
    a = study_task(panA)
    panA.pack(side = 'left',anchor = 'nw')
    panB.pack(side = 'left', anchor = 'nw')
    root.mainloop()