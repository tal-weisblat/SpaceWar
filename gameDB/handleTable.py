

#from initDB import *  
from xml.etree.ElementTree import tostring


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



cursor, conn = createGameDB()   
createGameTable(conn, cursor) 


# CHECK 
def checkPlayerInTable(username, password): 
    cursor.execute(" SELECT COUNT(1) FROM game_table WHERE (username,password) = ('{}','{}')".format(username, password) )    
    return cursor.fetchall()


# ADD PLAYER 
def addPlayer(username, password):

    count = checkPlayerInTable(username, password)[0][0]
    if count == 0: # add to table 
        cursor.execute(" INSERT INTO game_table VALUES ('{}', '{}','{}','{}')".format(username, password, 0, 0))
        conn.commit()
    else:     
        print ('Enter new username & password')


# PRINT 
def printGameTable():
    cursor.execute("SELECT * FROM game_time_table") 
    for instance in cursor.fetchall():
        print(instance)



def deleteAllRows():
    cursor.execute( " DELETE FROM game_time_table " ) 
    conn.commit()





# convert to string 
#date_time = datetime.now().strftime("%d/%m/%Y, %H:%m:%S")
def addGame(date,score):
    cursor.execute( " INSERT INTO game_time_table VALUES ('{}','{}')".format(date,score))
    conn.commit()

#deleteAllRows()


print('-------------------------------')
printGameTable()
print('-------------------------------')





    


