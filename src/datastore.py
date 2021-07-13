#!/usr/bin/python3

import mysql.connector

class Datastore():
    database=None
    
    mysql=None
    mysqlcursor=None

    @classmethod
    def __init__(cls):
        return None

    @staticmethod
    def __add__(email, scopes, auth_id, auth_key):
        statement = 'INSERT INTO {Datastore.database} SET email=%s, scopes=%s, auth_id=%s, auth_key=%s'
        try:
            mysqlcursor.execute( statement, [email, scopes, auth_id, auth_key])
            mydb.commit( )
        except Exception as error:
            raise Exception(error)

    @classmethod
    def init_db(cls, host, user, database, password):
        cls.mysql = mysql.connector.connect( host= host, user= user, password= password, database=database, auth_plugin='mysql_native_password')
        cls.mysqlcursor = mydb.cursor()
        cls.database = database
