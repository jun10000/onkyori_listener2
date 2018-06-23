#
# Author: jun10000 (https://github.com/jun10000)
#

from datetime import datetime
import pymysql

import settings

class RIDatabase:
    __con = None

    def connect(self):
        self.__con = pymysql.Connect(
            host=settings.common['Database']['Host'],
            user=settings.common['Database']['User'],
            password=settings.common['Database']['Password'],
            cursorclass=pymysql.cursors.DictCursor)

    def disconnect(self):
        if self.__con is not None:
            self.__con.close()

    def insert_signal(self, name):
        with self.__con.cursor() as cursor:
            cursor.execute(
                'INSERT INTO onkyori.signals(clock, name) VALUES (%s, %s)',
                (datetime.now(), name))
        self.__con.commit()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
        return True
