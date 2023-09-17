import sqlite3
import datetime
#import calculations

class Database_Intitialization:
    def __init__(self, database_name):
        self.database_name = database_name
        self.create_table_weightmaxes()

    def create_gymbro_db(self):
        database = sqlite3.connect(self.database_name)
        cursor = database.cursor()
        database.commit()
        database.close()

    def create_table_weightmaxes(self):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        table = """ CREATE TABLE IF NOT EXISTS WEIGHT_MAXES (
                Exercise VARCHAR(100),
                Weight INT,
                Reps INT,
                Date DATETIME
                );
                """
        cursor.execute(table)
        connection.commit()
        connection.close()



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
        self.exercise_max = self.get_maxes(exercise)
        self.exercise_max = self.exercise_max

        self.est_weights = self.Epley_Est_Calc(self.exercise_max, rep_range)


    def get_maxes (self, exercise):
        connection = sqlite3.connect('gymbro.db')
        cursor = connection.cursor()
        query = """
                SELECT Weight
                FROM WEIGHT_MAXES
                Where Reps = 1
                AND Exercise = ?
                LIMIT 1
                """
        cursor.execute(query, (exercise,))
        result = cursor.fetchone()
        connection.close()
        if result is not None:
            return result[0]
        else:
            return None
    
    def Epley_Est_Calc(self, weightmax, rep_range):
        start_str, end_str = rep_range.split('-')
        start = int(start_str)
        end = int(end_str)
        rep_range = (start_str, end_str)
        est_weights = {}

        for rep in range(start, end + 1):
            est_weight = weightmax / (1 + 0.0333 * rep)
            est_weights[rep] = round(est_weight)
        
        return est_weights
# # est_weights = calculations.Epley_Est_Calc(result[0], "1-5")

test = Get_Est_Rep_Weights("Bench Press", "1-3")
print(test.est_weights)

    

