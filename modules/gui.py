from tkinter import *
from tkinter import ttk
import tkinter as tk
from modules import db_handler

class GymBro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.w = 650
        self.h = 400
        self.title('SHRED SHED Presents - GymBro')
        self.geometry(f"{self.w}x{self.h}")
        self.notebook = ttk.Notebook(self, width= self.w, height= self.h)
        self.notebook.grid()
        self.tab_weight_maxes = WeightMaxesTab(self.notebook)
        self.tab_est_weights = EstWeightsTab(self.notebook)
        self.notebook.add(self.tab_weight_maxes, text='Weight Maxes')
        self.notebook.add(self.tab_est_weights, text= "Estimated Weights")

class WeightMaxesTab(ttk.Frame):
    def __init__(self, notebook):
        super().__init__(notebook)

        self.db_handler = db_handler

        self.create_maxes_insertions()
        # self.create_est_weight()
        self.create_maxes_treeview()
        self.refresh_maxes_treeview()
        self.schedule_refresh(self.refresh_maxes_treeview)

    def create_maxes_insertions(self):
        self.Entry_frame = ttk.Frame(self)
        self.Entry_frame.grid(row = 0, column = 0, sticky = tk.W, pady = 10, padx=10)

        self.exercise_label = ttk.Label(self.Entry_frame, text='Exercise')
        self.exercises = ['Barbell Bench Press', 'Barbell Squat', 'Barbell Deadlift']
        self.exercise_combobox = ttk.Combobox(self.Entry_frame, values=self.exercises, width=22, state='readonly')
        self.exercise_label.grid(row = 0, column = 0, sticky = tk.W, pady = 10, padx=10)
        self.exercise_combobox.grid(row = 0, column = 1, sticky = tk.W, pady = 10, padx=10)

        self.weight_label = ttk.Label(self.Entry_frame, text='Weight')
        self.weight_entry = ttk.Entry(self.Entry_frame, width=25)
        self.weight_label.grid(row= 1, column= 0, sticky= tk.W, pady = 10, padx=10)
        self.weight_entry.grid(row= 1, column= 1, sticky=tk.W, pady = 10, padx=10)

        self.reps_label = ttk.Label(self.Entry_frame, text='Reps')
        self.reps_entry = ttk.Entry(self.Entry_frame, width=25)
        self.reps_label.grid(row= 2, column= 0, sticky= W, pady = 10, padx=10)
        self.reps_entry.grid(row= 2, column= 1, sticky= W, pady = 10, padx=10)

        self.max_button = ttk.Button(self.Entry_frame, text="Insert Data", command=lambda: db_handler.Database_Handler.insert_maxes(self.exercise_combobox, self.weight_entry, self.reps_entry))
        self.max_button.grid(row=3, column= 1, sticky= W, pady = 10, padx=10)

    def create_maxes_treeview(self):
        self.Treeview_Frame = ttk.Frame(self)
        self.Treeview_Frame.grid(row= 0, column= 1, rowspan=5, padx=0, pady=10, sticky=(N, S, E, W))
        self.Treeview = ttk.Treeview(self.Treeview_Frame, height=8, column=("column1","column2","column3", "column4"), show='headings')
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

    def refresh_maxes_treeview(self):
        for i in self.Treeview.get_children():
            self.Treeview.delete(i)
        result = db_handler.Database_Handler.get_maxes()
        for row in result:
            self.Treeview.insert("", "end", values=(row[0], row[1], row[2], row[3]))

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
        self.Entry_frame.grid(row = 25, column = 0, sticky = tk.W, pady = 10, padx=10)

        self.exercises = ['Barbell Bench Press', 'Barbell Squat', 'Barbell Deadlift']
        self.est_weight_exercise_label = ttk.Label(self.Entry_frame, text='Exercise')
        self.est_weight_exercise_label.grid(row = 0, column = 0, sticky = tk.W, pady = 10, padx=10)
        self.est_weigt_exercise_combobox = self.exercise_combobox = ttk.Combobox(self.Entry_frame, values=self.exercises, width=22, state='readonly')
        self.est_weigt_exercise_combobox.grid(row = 0, column = 1, sticky = tk.W, pady = 10, padx=10)

        self.rep_range_label = ttk.Label(self.Entry_frame, text="Rep Range")
        self.rep_range_label.grid(row = 1, column = 0, sticky = tk.W, pady = 10, padx=10)
        self.rep_range_entry = ttk.Entry(self.Entry_frame, width=25)
        self.rep_range_entry.grid(row= 1, column= 1, sticky= tk.W, pady = 10, padx=10)

    def create_est_weight_treeview(self):
        self.Treeview_Frame = ttk.Frame(self)
        self.Treeview_Frame.grid(row= 0, column= 1, rowspan=5, padx=0, pady=10, sticky=(N, S, E, W))
        self.Treeview = ttk.Treeview(self.Treeview_Frame, height=8, column=("column1","column2","column3", "column4"), show='headings')
        self.Treeview.grid(row= 0, column=3)


    