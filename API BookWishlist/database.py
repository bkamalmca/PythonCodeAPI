import sqlite3
from sqlite3 import Error
from flask import jsonify, abort


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_wishlist(conn, wishlist):
    sql = ''' INSERT INTO wishlist(wishlist_id, user_id, book_id, is_available)
                  VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, wishlist)
    conn.commit()
    return cur.lastrowid


def db_create():
    database = "wishlist.db"

    sql_create_wishlist_table = """ CREATE TABLE IF NOT EXISTS wishlist (
                                        wishlist_id integer PRIMARY KEY,
                                        user_id text NOT NULL,
                                        book_id text NOT NULL,
                                        is_available text
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create table
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_wishlist_table)

    else:
        print("Error! cannot create the database connection.")


def get_json_fmt(res):
    payload = []
    content = {}
    for result in res:
        content = {'wishlist_id': result[0], 'user_id': result[1], 'book_id': result[2], 'is_available': result[3]}
        payload.append(content)
        content = {}
    return jsonify(payload)


def get_all_wishlists(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM wishlist")
    rv = cur.fetchall()
    return get_json_fmt(rv)


def check_wishlist(conn, wishlist_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM wishlist where wishlist_id = (?)", wishlist_id)
    if cur.fetchone() is None:
        return 0
    else:
        return 1


def get_wishlist(conn, wishlist_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM wishlist where wishlist_id = (?)", wishlist_id)
    rv = cur.fetchall()
    if rv is not None:
        return get_json_fmt(rv)
    else:
        return None


def ins_wishlist(conn, wishlist):
    cur = conn.cursor()
    cur.execute("INSERT INTO wishlist VALUES(?, ?, ?, ?)", (wishlist['wishlist_id'], wishlist['user_id'], wishlist['book_id'], wishlist['is_available'], ))
    conn.commit()
    return 0


def upd_wishlist(conn, wishlist):
    cur = conn.cursor()
    cur.execute("UPDATE wishlist set is_available = (?) where wishlist_id = (?)", (wishlist['is_available'], wishlist['wishlist_id'], ))
    conn.commit()
    return 0


def del_wishlist(conn, wishlist_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM wishlist where wishlist_id = (?)", wishlist_id)
    conn.commit()
    return 0
