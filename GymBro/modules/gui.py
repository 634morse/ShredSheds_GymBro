from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from ttkwidgets import tooltips
from modules import db_handler
from modules import exercises

class GymBro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.w = 650
        self.h = 400
        self.title('SHRED SHED Presents - GymBro')
        #self.iconbitmap('data\images\logo.ico')
        self.geometry(f"{self.w}x{self.h}")
        self.notebook = ttk.Notebook(self, width= self.w, height= self.h)
        self.notebook.grid()
        self.tab_weight_maxes = WeightMaxesTab(self.notebook)
        self.tab_est_weights = EstWeightsTab(self.notebook)
        self.notebook.add(self.tab_weight_maxes, text='Weight Maxes')
        self.notebook.add(self.tab_est_weights, text= "Estimated Weights")

class ReusableFunctions():
    def __init__(self):
        pass

class WeightMaxesTab(ttk.Frame):
    def __init__(self, notebook):
        super().__init__(notebook)

        self.db_handler = db_handler

        self.create_maxes_insertions()
        self.create_maxes_treeview()
        self.refresh_maxes_treeview()
        self.create_pr_track_treeview()
        self.schedule_refresh(self.refresh_maxes_treeview)

    def create_maxes_insertions(self):
        self.Entry_frame = ttk.Frame(self)
        self.Entry_frame.grid(row = 0, column = 0, sticky = tk.W, pady = 10, padx=10)

        self.exercise_label = ttk.Label(self.Entry_frame, text='Exercise')
        self.exercises = exercises.exercises
        self.exercise_combobox = ttk.Combobox(self.Entry_frame, values=self.exercises, width=22, state="readonly")
        self.exercise_label.grid(row = 0, column = 0, sticky = tk.W, pady = 10, padx=10)
        self.exercise_combobox.grid(row = 0, column = 1, sticky = tk.W, pady = 10, padx=10)


        self.weight_label = ttk.Label(self.Entry_frame, text='Weight')
        self.weight_entry = ttk.Entry(self.Entry_frame, tooltip="Enter your PR weight", width=25)
        self.weight_label.grid(row= 1, column= 0, sticky= tk.W, pady = 10, padx=10)
        self.weight_entry.grid(row= 1, column= 1, sticky=tk.W, pady = 10, padx=10)

        self.reps_label = ttk.Label(self.Entry_frame, text='Reps')
        self.reps_entry = ttk.Entry(self.Entry_frame, tooltip="Enter your reps for PR", width=25)
        self.reps_label.grid(row= 2, column= 0, sticky= W, pady = 10, padx=10)
        self.reps_entry.grid(row= 2, column= 1, sticky= W, pady = 10, padx=10)

        self.max_button = ttk.Button(self.Entry_frame, tooltip="Inserts above data into PR table", text="Insert Data", command=lambda: db_handler.Database_Handler.insert_maxes(self.exercise_combobox, self.weight_entry, self.reps_entry))
        self.max_button.grid(row=3, column= 1, sticky= W, pady = 10, padx=10)

    def create_maxes_treeview(self):
        self.Treeview_Frame = ttk.Frame(self)
        self.Treeview_Frame.grid(row= 0, column= 1, rowspan=5, padx=0, pady=8, sticky=(N, S, E, W))
        self.Treeview = ttk.Treeview(self.Treeview_Frame, height=8, column=("column1","column2","column3", "column4"), show='headings', tooltip="This table pulls stored PR's from the GymBro Weight_maxes table")
        self.Treeview.grid(row= 0, column=3)

        # Set the column headings
        self.Treeview.heading("#1", text="Exercise")
        self.Treeview.heading("#2", text="Weight")
        self.Treeview.heading("#3", text="Reps")
        self.Treeview.heading('#4', text="Date")

        #Define the column widths
        self.Treeview.column("#1", width=150)
        self.Treeview.column("#2", width=50)
        self.Treeview.column("#3", width=50)
        self.Treeview.column("#4", width=100)

    def create_pr_track_treeview(self):
        self.pr_track_rb_frame = ttk.Frame(self)
        self.pr_track_rb_frame.grid(row= 4, column= 1, padx=0, pady=10, sticky=(N, S, E, W))
        self.Title_Label = ttk.Label(self.pr_track_rb_frame, text="Weight Progession (Months)")
        self.Title_Label.grid(row= 1, column= 0, sticky=(W), pady=0, padx=5)
        self.rbvar = tk.StringVar()
        self.radiobutton_3_months = ttk.Radiobutton(self.pr_track_rb_frame, tooltip='3 months progression', text='3', value='-3', variable=self.rbvar, command=lambda: WeightMaxesTab.refresh_pr_progression_treeview(self, self.rbvar.get()))
        self.radiobutton_3_months.grid(row=1, column=1, sticky=W, padx=5)
        self.radiobutton_6_months = ttk.Radiobutton(self.pr_track_rb_frame, tooltip='6 months progression', text='6', value='-6', variable=self.rbvar, command=lambda: WeightMaxesTab.refresh_pr_progression_treeview(self, self.rbvar.get()))
        self.radiobutton_6_months.grid(row=1, column=3, sticky=W, padx=5)
        self.radiobutton_9_months = ttk.Radiobutton(self.pr_track_rb_frame, tooltip='9 months progression', text='9', value='-9', variable=self.rbvar, command=lambda: WeightMaxesTab.refresh_pr_progression_treeview(self, self.rbvar.get()))
        self.radiobutton_9_months.grid(row=1, column=4, sticky=W, padx=5)
        self.radiobutton_12_months = ttk.Radiobutton(self.pr_track_rb_frame, tooltip='12 months progression', text='12', value='-12', variable=self.rbvar, command=lambda: WeightMaxesTab.refresh_pr_progression_treeview(self, self.rbvar.get()))
        self.radiobutton_12_months.grid(row=1, column=5, sticky=W, padx=5)

        self.PR_Track_Treeview_Frame = ttk.Frame(self)
        self.PR_Track_Treeview_Frame.grid(row= 5, column= 1, rowspan=2, padx=0, pady=0, sticky=(N, S, E, W))
        self.treeview_tooltip = 'This table displays pr improvments over a period of time (selected by the radio buttons)'
        self.PR_Track_Treeview = ttk.Treeview(self.PR_Track_Treeview_Frame, tooltip=self.treeview_tooltip, height=5, column=("column1","column2", "column3"), show='headings')
        self.PR_Track_Treeview.grid(row= 4, column=0)

        # Set the column headings
        self.PR_Track_Treeview.heading("#1", text="Exercise")
        self.PR_Track_Treeview.heading("#2", text="Reps")
        self.PR_Track_Treeview.heading("#3", text="Progression")

        #Define the column widths
        self.PR_Track_Treeview.column("#1", width=150)
        self.PR_Track_Treeview.column("#2", width=100)
        self.PR_Track_Treeview.column("#3", width=100)

    def refresh_maxes_treeview(self):
        for i in self.Treeview.get_children():
            self.Treeview.delete(i)
        result = db_handler.Database_Handler.get_maxes()
        for row in result:
            self.Treeview.insert("", "end", values=(row[0], row[1], row[2], row[3]))
    
    def refresh_pr_progression_treeview(self, months):
        for i in self.PR_Track_Treeview.get_children():
            self.PR_Track_Treeview.delete(i)
        result = db_handler.Database_Handler.get_weight_pr_progression_months(self, months)
        for row in result:
            self.PR_Track_Treeview.insert("", "end", values=(row[0], row[1], row[2]))

    def schedule_refresh(self, object_refresh):
        self.object_refresh = object_refresh
        self.after(10000, self.object_refresh)
        self.after(10000, self.perform_refresh)

    def perform_refresh(self):
        self.object_refresh()
        self.after(10000, self.perform_refresh)

class EstWeightsTab(ttk.Frame):
    def __init__(self, notebook):
        super().__init__(notebook)
        
        self.create_est_weight()
        self.create_est_weight_treeview()
        
    def create_est_weight(self):
        self.Entry_frame = ttk.Frame(self)
        self.Entry_frame.grid(row = 0, column = 0, sticky = tk.W, pady = 10, padx=10)

        self.exercises = exercises.exercises
        self.est_weight_exercise_label = ttk.Label(self.Entry_frame, text='Exercise')
        self.est_weight_exercise_label.grid(row = 0, column = 0, sticky = tk.W, pady = 10, padx=10)
        self.est_weigt_exercise_combobox = self.exercise_combobox = ttk.Combobox(self.Entry_frame, values=self.exercises, width=22, state='readonly')
        self.est_weigt_exercise_combobox.grid(row = 0, column = 1, sticky = tk.W, pady = 10, padx=10)

        self.rep_range_label = ttk.Label(self.Entry_frame, text="Rep Range")
        self.rep_range_label.grid(row = 1, column = 0, sticky = tk.W, pady = 10, padx=10)
        self.rep_range_entry = ttk.Entry(self.Entry_frame, tooltip="Enter rep range to calculate. EX: 1-5", width=25)
        self.rep_range_entry.grid(row= 1, column= 1, sticky= tk.W, pady = 10, padx=10)

        self.button = ttk.Button(self.Entry_frame, text="Calculate Weight", command=self.insert_calculations)
        self.button.grid(row=3, column= 1, sticky= W, pady = 10, padx=10)

    def create_est_weight_treeview(self):
        self.Treeview_Frame = ttk.Frame(self)
        self.Treeview_Frame.grid(row= 0, column= 1, rowspan=5, padx=0, pady=10, sticky=(N, S, E, W))
        self.Treeview = ttk.Treeview(self.Treeview_Frame, height=8, column=("column1","column2"), show='headings')
        self.Treeview.grid(row= 0, column=3)

        # Set the column headings
        self.Treeview.heading("#1", text="Reps")
        self.Treeview.heading("#2", text="Weight")
         
        #Define the column widths
        self.Treeview.column("#1", width=75)
        self.Treeview.column("#2", width=75)

    def insert_calculations(self):
        result = db_handler.Get_Est_Rep_Weights(self.exercise_combobox.get(), self.rep_range_entry.get())
        result = result.est_weights
        
        for i in self.Treeview.get_children():
            self.Treeview.delete(i)
        for key, value in result.items():
            self.Treeview.insert("", "end", values=(key, value))

        print(result)
