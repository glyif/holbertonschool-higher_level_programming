#!/usr/bin/env python3
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
    db = MySQLdb.connect(host=host, user=user_name, passwd=password, db=db_name)
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

    print(", ".join(row[0] for row in data))


if __name__ == "__main__":
    db = db_connection(sys.argv[1], sys.argv[2], sys.argv[3])
    db_query(db, """SELECT cities.name FROM cities
    INNER JOIN states
    WHERE states.id = cities.state_id AND states.name = '{:s}'""".format(sys.argv[4].split(' ')[0].split(';')[0]))
