#!/usr/bin/python3

import mysql.connector

class Datastore():
    database=None
    
    mysql=None
    mysqlcursor=None

    @classmethod
    def __init__(cls):
        return None

    @classmethod
    def __add__(cls, email, scopes, auth_id, auth_key):
        statement = f'INSERT INTO {cls.database} SET email=%s, scopes=%s, auth_id=%s, auth_key=%s'
        try:
            cls.mysqlcursor.execute( statement, [email, scopes, auth_id, auth_key])
            cls.mysql.commit( )
        except mysql.connector.errors.IntegrityError as error:
            print(error.msg)
            # print(error._full_msg)
            if error.errno == 1062:
                print('dev already exist')
                # raise Exception(error._full_msg)
            else:
                raise Exception(error)
        except Exception as error:
            raise Exception(error)

    @classmethod
    def init_db(cls, host, user, database, password):
        print(f'host={host}, user={user}, database={database}, password={password}')
        cls.mysql = mysql.connector.connect( host= host, user= user, password= password, database=database, auth_plugin='mysql_native_password')
        # cls.mysql = mysql.connector.connect( host= host, user= user, password= password, database=database)
        cls.mysqlcursor = cls.mysql.cursor()
        cls.database = database
