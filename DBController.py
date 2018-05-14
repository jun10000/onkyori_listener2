#
# Author: jun10000 (https://github.com/jun10000)
#

import settings

from datetime import datetime
import pymysql

class DBController:
    __db_connector = None

    def __init__(self):
        pass

    def connect(self):
        self.__db_connector = pymysql.Connect(
            host=settings.common['Database']['Host'],
            user=settings.common['Database']['User'],
            password=settings.common['Database']['Password'],
            cursorclass=pymysql.cursors.DictCursor)

    def disconnect(self):
        self.__db_connector.close()

    def insert_signal(self, name):
        with self.__db_connector.cursor() as db_cursor:
            db_cursor.execute(
                'INSERT INTO onkyori.signals(clock, name) VALUES (%s, %s)',
                (datetime.now(), name))
        self.__db_connector.commit()
