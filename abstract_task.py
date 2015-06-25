import Tkinter as tk
from Tkinter import *
import task_disp
import tkFont



class abstract_task(tk.Frame):

    # ft1 = tkFont.Font(font='Courier' ,size = 20, weight='Bold')
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.creat_start_button()
        self.pack(side = tk.TOP, fill = tk.Y)

    def specify_type(self, label, rowspan = 2, **kwargs):
        self.labelname = label
        self.biglabel = tk.Label(self, text = self.labelname, font = "Courier 23 bold" ,**kwargs)
        self.biglabel.grid(row=0, column= 0, rowspan = 3, sticky= 'ns')

    def creat_start_button(self):
        button = tk.Button(self, text="Create Task", command = self.on_start)
        button.grid(row=2, column=3,sticky='e')

    def on_start(self):
        self.pack_forget()
        self.__init__(self.root)
        task_disp.task_disp(self)

#notice that timeVar is a String , will convert that to float
    def duration_details(self, timeVar, detailVar):
        timeVar.set('Duration')
        timeEntry = Entry(self, textvariable = timeVar, width=25)
        timeEntry.grid(column=3, row = 0)
        detailVar.set('Details')
        detailEntry = Entry(self,textvariable =  detailVar, width=25)
        detailEntry.grid(column=3, row= 1)
        #e = Entry(self, width=25)



###--------------------------------------communication with taks_disp

    def get_label(self):
        return 'Label \n djka'
    def get_detail(self):
        return 'Details: '
    def on_pause(self, times):
        #pass in a tuple consisting of start time, end time, duration in min
        pass
    def on_commit(self):
        # pass in a tuple consisting of total time taken, percentage of work, difficulty and satisfaction

        pass


        #e.grid(row=0, column=3, padx=2, pady=2, sticky='we')

##-------------------------------------------------------------------------first concrete class
#options     
