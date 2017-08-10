import MySQLdb
import os

def db_connection(host="localhost", user_name, password, db_name):
    db = MySQLdb.connect(host=host, user=user_name, passwd=password, db=db_name)
    return db

def db_query(db, query):
    cur = db.cursor()
    cur.execute(query)

if __name__ == "__main__":
    db = db_connection(user_name=os.argv[1], password=os.argv[2], db_name=os.argv[3])
    db_query(db, "SELECT * FROM states)
