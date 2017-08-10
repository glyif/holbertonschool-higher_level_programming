#!/usr/bin/python3
"""
mysqldb select states
"""
import sys

import MySQLdb


def db_connection(user_name, password, db_name, host="localhost"):
    """
    db_connection - connects to db
    :param user_name: username
    :param password: password
    :param db_name: database name
    :param host: host - default to localhost
    :return: db
    """
    db = MySQLdb.connect(host=host,
                         user=user_name,
                         passwd=password,
                         db=db_name,
                         port=3306)
    return db


def db_query(db, query):
    """
    db_query - queries database
    :param db: database
    :param query: query
    :return: none
    """
    cur = db.cursor()
    cur.execute(query)
    data = cur.fetchall()

    for row in data:
        print(row)


if __name__ == "__main__":
    db = db_connection(sys.argv[1], sys.argv[2], sys.argv[3])
    db_query(db, "SELECT id, name FROM states ORDER BY states.id ASC")
