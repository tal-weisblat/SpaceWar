


import sqlite3 



# DB 
def createGameDB():
    conn = sqlite3.connect("gameDB.db")
    cursor = conn.cursor()           
    return cursor, conn       

# TABLE 
def createGameTable(conn, cursor):  

    # check if table exist 
    list_of_tables = cursor.execute( " SELECT name FROM sqlite_master WHERE type = 'table' AND name='game_time_table' ").fetchall()
    if list_of_tables[0][0] != 'game_time_table': 
        
        # create table (if not exist)
        cursor.execute(""" CREATE TABLE game_time_table (
                        time TEXT, 
                        score INTEGER
                        ) """)    
        conn.commit()
