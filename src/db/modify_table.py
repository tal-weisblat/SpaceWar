

import sqlite3


# connect to db & table
conn = sqlite3.connect("game_db.db")
cursor = conn.cursor()           

# add time & score 
def addGame(date,score):
    cursor.execute( " INSERT INTO game_time_table VALUES ('{}','{}')".format(date,score))
    conn.commit()


