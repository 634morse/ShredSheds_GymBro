from modules import gui
from modules import db_handler

if __name__ == "__main__":
    #Initializing Database
    db_handler.Database_Intitialization('gymbro.db')

    #Initializing db_handler for use in the Gymbro class
    db_handling = db_handler.Database_Handler('gymbro.db')

    #Running the application
    app = gui.GymBro()
    app.mainloop()
