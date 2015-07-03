import Tkinter as tk
from Tkinter import *
from task_disp import task_disp
import tkFont
import MySQLdb as mbd
import sqlCom 

from copy import copy
sql = sqlCom.sqlCom()



class abstract_task(tk.Frame):

    # ft1 = tkFont.Font(font='Courier' ,size = 20, weight='Bold')
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.creat_start_button()
        self.pack(side = tk.TOP, fill = tk.Y)
        self.init_var()
        self.duration_details()

    def init_var(self):
        self.duration = tk.StringVar()
        self.duration.set('0')
        self.detail = tk.StringVar()
        self.detail.set('testing')
        
    def specify_type(self, label, rowspan = 2, **kwargs):
        self.labelname = label
        self.biglabel = tk.Label(self, text = self.labelname, font = "Courier 23 bold" ,**kwargs)
        self.biglabel.grid(row=0, column= 0, rowspan = 3, sticky= 'ns')

    def creat_start_button(self):
        button = tk.Button(self, text="Create Task", command = self.on_start)
        button.grid(row=2, column=3,sticky='e')

    def on_start(self):
        self.pack_forget()
        pasobj = copy(self)
        tsk = task_disp()
        tsk.set_task(pasobj)
        ##############################

        self.__init__(self.root, fill = tk.X)

#notice that timeVar is a String , will convert that to float
    def duration_details(self):

        timeVar = self.duration
        detailVar = self.detail
        Label(self, text ='Detail').grid(row=0,column=3)
        timeEntry = Entry(self, textvariable = detailVar, width=15)
        timeEntry.grid(column=4, row = 0)
        Label(self, text ='Time(Min)').grid(row=1,column=3)
        
        detailEntry = Entry(self,textvariable =  timeVar, width=15)
        detailEntry.grid(column=4, row= 1)
        #e = Entry(self, width=25)



###--------------------------------------communication with taks_disp
    
    def get_label(self):
        return 'Label \n djka'
    def get_subject_table_name(self):
        return "test_subject"
    def get_detail(self):
        self.duration_for_commit = int(self.duration.get())
        self.detail_for_commit = self.detail.get()
        return 'Details: ' + self.detail.get() +'\n' + "Expected Duration:" + self.duration.get() + 'min'
    def commit_detail(self):
        return self.detail_for_commit
    def on_pause_sql(self, start_time,end_time, cumper):
        #pass in a tuple consisting of start time, end time, duration in min
        def datetime_strf(date_time_obj):
            return date_time_obj.strftime("%Y-%m-%d %H:%M:%S")
        create_table = """create table if not exists %s(
                        start_time datetime not null ,
                        end_time datetime not null,
                        cumper int2 default 0,
                        key(start_time, end_time));"""%(self.get_subject_table_name())
        sql.excecute(create_table)
        insert_query = """insert into %s values('%s', '%s', %d);"""%(self.get_subject_table_name(), 
                                                                  datetime_strf(start_time),
                                                                  datetime_strf(end_time),
                                                                  cumper  )
        print insert_query
        
        sql.excecute(insert_query)
        pass
    def get_expected_duration(self):
        print "testing self duration: %s"%(self.duration.get())
        return self.duration_for_commit
    def on_commit(self):
        
        # pass in a tuple consisting of total time taken, percentage of work, difficulty and satisfaction

        pass
    def get_table_name(self):
        return self.get_subject_table_name()
    def get_task_category(self):
        return 'testing_commit'
        #e.grid(row=0, column=3, padx=2, pady=2, sticky='we')

##-------------------------------------------------------------------------first concrete class
#options     
