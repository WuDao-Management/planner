import Tkinter as tk
from abstract_task import *
import time

class task_disp(tk.Frame):

    pool = None;
    passive_bg = '#D1E7E0'
    active_bg = '#FFB585'
    def __init__(self, task,  *args, **kwargs):
        #task an instance of abstract task

        tk.Frame.__init__(self, relief = tk.SUNKEN, bg= task_disp.passive_bg, width = 200,bd = 2, *args, **kwargs)
        self.task = task
        self.create_resume_button()
        self.pack(task_disp.pool, side = tk.TOP, fill = tk.X,  anchor = 'n')
        self.furnish_options()

    def init_var(self):
        self.curStart = None;
        self.curEnd = None;
        self.cumTime = None;

    def furnish_options(self):
        self.resume_task()
        pass

    #display text information
    def resume_task(self):
        #will enable customization of the widget
        self.l1 =Label(self, text = self.task.get_label(), font='Helvetica 20 bold', bg = task_disp.passive_bg)
        self.l1.grid(row=0, column=0, rowspan=3, sticky='ns')
        self.l2 = Label(self, text = self.task.get_detail(), bg = task_disp.passive_bg)
        self.l2.grid(row=0, column=1)

    #------------------------------------------------------------------------- functions for button press

    #------------------------------------------------------------------------ 
    def change_color(self,color):
        self.configure(bg = color)
        self.l1.config(bg = color)
        self.l2.config(bg = color)


    def create_resume_button(self):
        self.resume_button = Button(self,text = 'Resume', command = self.on_resume)
        self.resume_button.grid(row = 1, column = 2)
        self.commit_button = Button(self, text = 'Commit', command = self.on_commit)
        self.commit_button.grid(row=1, column = 3)

    def on_resume(self):
        self.change_color(task_disp.active_bg)
        self.curStart = time.localtime()
        self.resume_button.grid_forget()
        self.commit_button.grid_forget()
        self.pause_button = Button(self, text= 'Pause', command = self.on_pause)
        self.pause_button.grid(row = 1, column = 2)
    
    def on_commit(self):
        self.pack_forget()
        #to do implement commit functionality
        pass

    def on_pause(self):
        self.change_color(task_disp.passive_bg)
        self.pause_button.grid_forget()
        self.commit_button.grid(row=1, column = 3)
        self.resume_button.grid(row = 1, column = 2)
        #to do implement insert into database
   
