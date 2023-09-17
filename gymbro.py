from modules import gui
from modules import db_handler
from modules import calculations

if __name__ == "__main__":
    #Initializing Database
    db_name = db_handler.Database_Intitialization('gymbro.db')
    db_name.create_gymbro_db()

    #Initializing db_handler for use in the Gymbro class
    db_handling = db_handler.Database_Handler('gymbro.db')
    app = gui.GymBro()
    app.mainloop()
