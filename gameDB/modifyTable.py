

import sqlite3


# connect to DB & TABLE 
conn = sqlite3.connect("gameDB.db")
cursor = conn.cursor()           


# ADD TIME & SCORE 
def addGame(date,score):
    cursor.execute( " INSERT INTO game_time_table VALUES ('{}','{}')".format(date,score))
    conn.commit()


