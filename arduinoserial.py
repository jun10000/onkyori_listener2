#!/usr/bin/python3

#
# Author: jun10000 (https://github.com/jun10000)
#

import serial

class ArduinoSerial:
    __ser = None

    def connect(self):
        self.__ser = serial.Serial('/dev/ttyACM0', 9600)

    def disconnect(self):
        if self.__ser is not None:
            self.__ser.close()

    def readbits(self):
        bits = self.__ser.readline().decode().rstrip()
        return bits

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
        return True
