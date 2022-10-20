

import sqlite3


# connection (db & table) 
conn = sqlite3.connect("game_db.db")
cursor = conn.cursor()           
    
# extract lines 
def getResults():
    table = cursor.execute("SELECT * FROM game_time_table").fetchall()
    return table


