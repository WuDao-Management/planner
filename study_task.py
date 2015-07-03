import Tkinter as tk
from abstract_task import *
import task_disp


class study_task(abstract_task):
    

    def __init__(self, root ,*args, **kwargs):
        self.root = root
        abstract_task.__init__(self, root,  bd=2,   relief=tk.RAISED)
        self.init_args()
        self.furnish_options()
        self.pack(fill = tk.X)
        
    def init_args(self):
        #subjecgts button and course choice
        self.subject_choice = tk.StringVar()
        
        data_fh = open('study_info.txt','r')
        self.catalog = eval(data_fh.read())
        self.subjects = self.catalog.keys()
        self.mycourse = ''
        self.mysubject = ''
        self.course_choice = tk.StringVar()

        self.course_choice.set('Birchoff Algebra')
    def furnish_options(self):
        self.specify_type('work',bg='#ffffBB', foreground = '#3333aa')
        self.add_subjects()


#####################################################################below are functionalities
#----------------------------------------------
    def add_subjects(self):
        self.subject_mb = tk.Menubutton(self, text = 'Choose Subject',width = 20)
        mb = self.subject_mb
        mymenu = tk.Menu(mb)
        mb['menu'] = mymenu
        self.subject_choice.set('Math')
        for subject in self.subjects:
            mymenu.add_radiobutton(label=subject,variable = self.subject_choice , command = self.init_course)

        ##to implement selection functionality
        mb.grid(row = 0, column = 1)
        self.course_mb = tk.Menubutton(self, text = 'Choose Course', width = 20)
        self.course_mb.grid(row = 0, column = 2)

#------------------------------------init course selection
    def init_course(self):
        self.mysubject = self.subject_choice.get()
        self.passsubject = self.mysubject
        self.subject_mb.config(text = self.mysubject)
        
        mb = self.course_mb
        mymenu = tk.Menu(mb)
        mb['menu'] = mymenu
        
        courses = self.catalog[self.mysubject]
        for course in courses.keys():
            mymenu.add_radiobutton(label=course,variable = self.course_choice , command = self.disp_info)
            
        

    def disp_info(self):

        self.mycourse = self.course_choice.get()
        self.passcourse = self.mycourse
        self.course_mb.config(text = self.mycourse)


    def get_label(self):
        #print "mysubject is %s"%(self.passsubject )
        #print "mycourse is %s"%(self.passcourse)
        try:
            return self.catalog[self.passsubject][self.passcourse][0] #it appears to be a bug of python
        except AttributeError:
            return "Rubbish_Input"
            
    def get_subject_table_name(self):
        try:
            return self.catalog[self.passsubject][self.passcourse][1]
        except AttributeError:
            return "Rubbish_Input"

    def get_task_category(self):
        return 'study'
   
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