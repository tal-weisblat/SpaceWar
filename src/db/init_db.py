
import sqlite3



def createGameDB():

    # database 
    conn = sqlite3.connect("gameDB.db")
    cursor = conn.cursor()           
    
    # table 
    table_list = cursor.execute( " SELECT name FROM sqlite_master WHERE type = 'table' AND name='game_time_table' ").fetchall()
    if table_list[0][0] != 'game_time_table': # create table (if not exist)
        cursor.execute(" CREATE TABLE game_time_table ( time TEXT, score INTEGER) ")    
        conn.commit()

    return conn, cursor 
