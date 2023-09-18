import sqlite3
import datetime
#import calculations

class Database_Intitialization:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = sqlite3.connect(database_name)
        self.create_tables()

    def __del__(self):
        self.connection.close()

    def create_tables(self):
        self.create_table_weightmaxes()
        self.create_table_exercises()

    def create_table_weightmaxes(self):
        with self.connection:
            cursor = self.connection.cursor()
            table = """ CREATE TABLE IF NOT EXISTS WEIGHT_MAXES (
                    Exercise VARCHAR(100),
                    Weight INT,
                    Reps INT,
                    Date DATETIME
                    );
                    """
            cursor.execute(table)

    def create_table_exercises(self):
        with self.connection:
            cursor = self.connection.cursor()
            table = """ CREATE TABLE IF NOT EXISTS EXERCISES (
                    Exercise VARCHAR(100)
                    );
                    """
            cursor.execute(table)

class Database_Handler:
    def __init__(self, db_file):
        self.db_file = db_file

    def insert_maxes (exercise_combobox, weight_entry, reps_entry):
        exercise = exercise_combobox.get()
        weight = weight_entry.get()
        reps = reps_entry.get()
        date = datetime.date.today()

        connection = sqlite3.connect('gymbro.db')
        cursor = connection.cursor()
        insert_sql = "INSERT INTO WEIGHT_MAXES (exercise, weight, reps, date) VALUES (?, ?, ?, ?)"
        cursor.execute(insert_sql, (exercise, weight, reps, date))
        connection.commit()
        connection.close

    def get_maxes ():
        connection = sqlite3.connect('gymbro.db')
        cursor = connection.cursor()
        data = """
                Select * 
                FROM WEIGHT_MAXES
                order by Date DESC
               """
        cursor.execute(data)
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result

class Get_Est_Rep_Weights:
    def __init__(self, exercise, rep_range):
        self.exercise_max_data = self.get_maxes(exercise)
        self.exercise_max_data = self.exercise_max_data
        self.exercise_max = self.exercise_max_data[0]
        self.exercise_reps = self.exercise_max_data[1]

        self.est_weights = self.Epley_Est_Calc(self.exercise_max, self.exercise_reps, rep_range)


    def get_maxes (self, exercise):
        connection = sqlite3.connect('gymbro.db')
        cursor = connection.cursor()
        query = """
                SELECT Weight, reps, date
                FROM WEIGHT_MAXES
                WHERE Exercise = ?
                order by Date DESC, reps ASC
                LIMIT 1
                """
        cursor.execute(query, (exercise,))
        result = cursor.fetchone()
        connection.close()
        if result is not None:
            return result
        else:
            return None
    
    def Epley_Est_Calc(self, weightmax, reps, rep_range):
        start_str, end_str = rep_range.split('-')
        start = int(start_str)
        end = int(end_str)
        rep_range = (start_str, end_str)
        est_weights = {}

        # Getting est 1rm if max weight is for more than 1 rep  
        if reps != 1:
            weightmax = weightmax * (1 + reps / 30)

        #Calculating weight estimates
        for rep in range(start, end + 1):
            est_weight = weightmax / (1 + 0.0333 * rep)
            est_weights[rep] = round(est_weight)
        
        return est_weights
