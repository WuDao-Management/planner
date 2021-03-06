import Tkinter as tk
from abstract_task import *
from datetime import *
import sqlCom 
sql = sqlCom.sqlCom()
import ttk


#todo total time required to make it more clear during planning and excecution of task
#todo implement reconstructing from historical records

miliseconds = 1000
seconds = 60
class task_disp(tk.Frame):
    time_refresh_interval = seconds*miliseconds;
    
    pool = None

    width = 580
    passive_bg = '#D1E7E0'
    active_bg = '#FFB585'
    timeformat = lambda self,sec: sec/seconds;

    def __init__(self ,*args, **kwargs):
        #task an instance of abstract task
        # self.root = task_disp.pool

        tk.Frame.__init__(self, task_disp.pool,  width = task_disp.width,relief = tk.SUNKEN, bg= task_disp.passive_bg,bd = 2, **kwargs)
        
        self.pack(fill = tk.X, side = 'top')
        #  self.pack( side = tk.TOP, fill = tk.X,  anchor = 'nw')
    def set_task(self, task):
        self.task = task
        self.create_resume_button()
        self.init_var()
        self.furnish_options()
        self.create_progress_bar()
        
        print "packing display widget"

    def init_var(self):
        self.curStart = None
        self.curEnd = None
        self.cumTime = 0  # saved in terms of seconds
        self.cumcompleted = tk.StringVar()
        self.cumcompleted.set('0')
        self.deltacompleted = 0
        self.timeLabel = tk.Label(self,text = '0 min',font = 'Times  14 bold', bg = self.passive_bg, foreground = 'blue')
        self.timeLabel.grid(row = 1, column = 7)
        self.active = False

    def furnish_options(self):
        self.resume_task()
        pass

    #display text information
    def resume_task(self):
        #will enable customization of the widget
        self.l1 =Label(self, text = self.task.get_label(), font='Helvetica 15 bold', bg = task_disp.passive_bg, foreground ='#5B8340')
        self.l1.grid(row=0, column=0, rowspan=3, sticky='ns')
        self.l2 = Label(self, text = self.task.get_detail(), font = 'Times 12 ', bg = task_disp.passive_bg)
        self.l2.grid(row=0, column=1, rowspan=2,sticky='ns')

    #------------------------------------------------------------------------- functions for button press

    #------------------------------------------------------------------------ 
    def change_color(self,color):
        self.configure(bg = color)
        self.l1.config(bg = color)
        self.l2.config(bg = color)
        self.timeLabel.config(bg = color)

    def create_resume_button(self):
        self.resume_button = Button(self,text = 'Resume', command = self.on_resume)
        self.resume_button.grid(row = 1, column = 3)
        self.commit_button = Button(self, text = 'Commit', command = self.on_commit)
        self.commit_button.grid(row=1, column = 4)

    def on_resume(self):
        self.active = True
        #print 'on resume'
        self.after(task_disp.time_refresh_interval,lambda:self.display_time())
        self.change_color(task_disp.active_bg)
        self.curStart = datetime.now()
        self.resume_button.config(text = 'Pause ', command = self.on_pause)
        self.commit_button.config(state = 'disabled')
        # self.pause_button = Button(self, text= 'Pause', command = self.on_pause)
        # self.pause_button.grid(row = 1, column = 3)

    def on_pause(self):
        self.active = False
        self.change_color(task_disp.passive_bg)
        self.curEnd = datetime.now()
        self.cumTime += (self.curEnd - self.curStart).seconds
        self.ask_percent_completion()
#        self.pause_button.grid_forget()
        self.resume_button.config(text = 'Resume', command = self.on_resume)
        self.commit_button.config(state = 'normal')
        # self.resume_button.grid(row = 1, column = 4)

#------------------------------------------------------------------------------commit functionality universal among all    
    def on_commit(self):

        t3 = tk.Toplevel(self)
        t3.title('Commit')
        t3.geometry('400x120+300+300')
        t3.transient(self)
        #completion scale bar
        
        self.commit_completeion = tk.IntVar()
        self.commit_completeion.set(self.cumcompleted.get())
        tk.Label(t3 , text='Completion:').grid(row=0, column=0)
        tk.Scale(t3, from_=0, to=100,variable = self.commit_completeion, orient=tk.HORIZONTAL, showvalue = True, bg = task_disp.passive_bg).grid(row=0,column=1)


        self.commit_difficulty = tk.IntVar()
        tk.Label(t3 , text='Difficulty:').grid(row=1, column=0)
        tk.Scale(t3, from_=0, to=10,variable = self.commit_difficulty, orient=tk.HORIZONTAL, showvalue = True, bg = task_disp.passive_bg).grid(row=1,column=1)

        
        self.commit_satisfaction = tk.IntVar()
        tk.Label(t3 , text='Satisfaction:').grid(row=2, column=0)
        tk.Scale(t3, from_=0, to=10,variable = self.commit_satisfaction, orient=tk.HORIZONTAL, showvalue = True, bg = task_disp.passive_bg).grid(row=2,column=1)


        self.text = tk.Text(t3,width= 30,height = 3, padx = 4,borderwidth = 2, bg = '#ffffBB')
        self.text.grid(row=0, column = 2, rowspan = 2,columnspan =3, sticky = 'ns')
        self.text.insert(tk.END, 'testing')

        tk.Button(t3, text="Confirm", underline=0, command = lambda: self.on_sql_commit(t3) ).grid(row=2, column=3, sticky='e')
        tk.Button(t3, text='I Regret', command = lambda: t3.destroy()).grid(row = 2, column=4,sticky ='w')
        #remove the task from pool
        
        #to do implement commit functionality

    def on_sql_commit(self,t3):
        self.pack_forget()
        
        if self.text.get('1.0',tk.END).strip() == 'testing':
            print 'task cancelled cancel'
            t3.destroy()
            return
        tablename = self.task.get_task_category()
        if self.active:
            self.cumTime += (self.curEnd - self.curStart).seconds
        self.cumTime = task_disp.timeformat(self,self.cumTime)
        def today():
            return datetime.now().strftime("%Y-%m-%d")
        create_table_query = """create table if not exists %s(
                                curdate date not null ,
                                actual_duration int3 not null,
                                expected_duration int3 not null,
                                difficulty int2 not null,
                                satisfaction int2 not null,
                                per_completed int3 not null,
                                comments text,
                                course varchar(40),
                                detail varchar(100),

                                key(curdate, course, detail));"""%(tablename)
        sql.excecute(create_table_query)
        insert_query = """insert into %s values('%s' , %d, %d, %d, %d, %d, '%s', '%s', '%s');
                                                """%(tablename
                                                    ,today(), self.cumTime ,self.task.get_expected_duration()
                                                    ,self.commit_difficulty.get(), self.commit_satisfaction.get(), self.commit_completeion.get()
                                                    ,self.text.get('1.0',tk.END), self.task.get_table_name(), self.task.commit_detail())
        print insert_query
        sql.excecute(insert_query)
        t3.destroy()
        



        #to do implement insert into database
   
    def ask_percent_completion(self):
        #return delta completion
        t2 = tk.Toplevel(self)
        t2.title('Cumulative Completion Percentage')
        t2.geometry('360x40+500+300')
        t2.transient(self)
        # tk.Label(t2, text=self.cumcompleted.get()+'-').grid(row=0, column=0, sticky='e')
        
        
        
        tk.Label(t2 , text='Completion:').grid(row=0, column=0)
        tk.Scale(t2, from_=0, to=100,variable = self.cumcompleted, orient=tk.HORIZONTAL, showvalue = True, bg = task_disp.passive_bg).grid(row=0,column=1)

        # e = tk.Entry(t2, width=10, textvariable = self.cumcompleted)
        # e.grid(row=0, column=1, padx=2, pady=2, sticky='we')
        # e.focus_set()
        tk.Button(t2, text="Confirm", underline=0,  command=lambda: self.on_pause_completion_sql(t2) ).grid(row=0, column=2, sticky='e'+'w', padx=2, pady=2)
        t2.bind('<Return>',lambda event: self.on_pause_completion_sql(t2) )
        
    def on_pause_completion_sql(self, t2):
        
        self.task.on_pause_sql(self.curStart,self.curEnd,int(self.cumcompleted.get()))
        t2.destroy()
    #-------------------------------------------------------------------------------------time display module
    def display_time(self):
        #print "in display time"
        cumTime =  self.cumTime
        if self.curStart == None: return
        cumTime += (datetime.now() - self.curStart).seconds 
        cumTime = task_disp.timeformat(self,cumTime) #convert to min
        self.float_cur_progress = cumTime/float(self.maxtime) * 100 
        
        # print cumTime
        if self.active:
            #print self.float_cur_progress
            self.timeLabel.config(text = "%s min"%(cumTime))
            self.curprogress.set(self.float_cur_progress)
            self.after(task_disp.time_refresh_interval,lambda:self.display_time())

    def create_progress_bar(self):
        interval = task_disp.time_refresh_interval
        root = self
        self.maxtime = int(self.task.get_expected_duration()) #duration in min
        self.float_cur_progress = 0
        self.curprogress = tk.IntVar()
        self.curprogress.set(0)
        progressbar = ttk.Progressbar(root, length = 100,  variable=self.curprogress)
        progressbar.grid(row=1, column = 20)


