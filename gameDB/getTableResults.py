

import sqlite3


# connection (db & table) 
conn = sqlite3.connect("gameDB.db")
cursor = conn.cursor()           
    

# extract lines 
def getResults():
    table = cursor.execute("SELECT * FROM game_time_table").fetchall()
    return table

table = getResults()



# def printGameTable():
#     cursor.execute("SELECT * FROM game_time_table") 
#     for instance in cursor.fetchall():
#         print(instance)
# printGameTable()


