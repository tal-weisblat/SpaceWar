
import sqlite3 


# DB 
def createGameDB():
    conn = sqlite3.connect("gameDB.db")
    cursor = conn.cursor()           
    return cursor, conn       

# TABLE 
def createGameTable():  
    cursor.execute(""" CREATE TABLE game_table (
                    username TEXT, 
                    password TEXT, 
                    number_of_games INTEGER, 
                    highest_score INTEGER
                    ) """)    
    conn.commit()


# PRINT 
def printGameTable():
    cursor.execute("SELECT * FROM game_table") 
    for instance in cursor.fetchall():
        print(instance)


cursor, conn = createGameDB()    






    








def checkPlayerInTable(username, password): 
    cursor.execute(" SELECT COUNT(1) FROM game_table WHERE (username,password) = ('{}','{}')".format(username, password) )    
    return cursor.fetchall()


def addPlayer(username, password):

    count = checkPlayerInTable(username, password)[0][0]
    if count == 0: # add to table 
        cursor.execute(" INSERT INTO game_table VALUES ('{}', '{}','{}','{}')".format(username, password, 0, 0))
        conn.commit()
    else:     
        print ('Enter new username & password')




print('-------------------------------')
addPlayer('moti','abcd')
printGameTable()
print('-------------------------------')


    


# cursor.execute(" SELECT COUNT(1) FROM game_table WHERE (username,password) = ('tal','abc') ")
# print(cursor.fetchall())
