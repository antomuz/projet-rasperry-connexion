import sqlite3
#https://docs.python.org/2/library/sqlite3.html
#id INTEGER PRIMARY KEY, 
# date_connexion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
# login_infirmiere TEXT NOT NULL, 
# etape INTEGER NOT NULL, 
# message TEXT, 
# divers TEXT


conn = sqlite3.connect('casliemie.db')
c = conn.cursor()




def insertBD():
    c.execute("INSERT INTO logs (login_infirmiere, etape,message) VALUES ('test',1,'Aie')")
    conn.commit()

def insertLog(login,etape,message,divers=""):
    #c.execute("INSERT INTO LOGS(login_infirmiere,etape,message) values({0},{1},{2})".format(login, etape,message))
    c.execute("INSERT INTO LOGS(login_infirmiere,etape,message,divers) values('{0}','{1}','{2}','{3}')".format(login, etape,message,divers))
    conn.commit()


def showBD():
    c.execute("SELECT * FROM logs")
    print(c.fetchall())

#btssio-carcouet.fr/ppe4/public/connect2/fnightingale/fnightingale/infirmiere
#login/mdp