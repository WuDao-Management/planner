import Tkinter as tk
from abstract_task import *
import task_disp 
from study_task import *
import waste_time_task


class Manager(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1040x900')
        self.root.config(bg = 'grey')
        self.create_left_panel()
        self.create_sperator()

        self.create_right_panel()
        self.root.mainloop()

    def create_left_panel(self):

        self.leftPlane = Frame(self.root, bg = '#B2ECFF', width = 500, height = 600)
        study_task(self.leftPlane)
        waste_time_task.waste_time(self.leftPlane)

        self.leftPlane.pack(side = tk.LEFT, anchor = 'nw',fill = tk.Y)


    def create_sperator(self):
        separator = Frame(self.root, width = 10,bg='orange')
        separator.pack(side = tk.LEFT, anchor = 'nw', fill = tk.Y, expand= True)


    def create_right_panel(self):
        rightPlane  = Frame(self.root, width = 530)
        rightPlane.pack(side = tk.LEFT, anchor = 'nw', fill = tk.Y, expand= True)
        #tk.Label(self.rightPlane,bg = 'orange').pack() #I am not sure what went wrong, appears to be a glitch of Tkinter
        task_disp.task_disp.pool = rightPlane


        # task_disp.task_disp.set_pool(rightPlane)
        print 'binding task pool'
       
 
if __name__=="__main__":
    Manager()