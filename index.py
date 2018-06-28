#!/usr/bin/python3

#
# Author: jun10000 (https://github.com/jun10000)
#

import os
import sys

from arduinoserial import ArduinoSerial
from ridatabase import RIDatabase


def main():
    with RIDatabase() as db, ArduinoSerial() as ser:
        while True:
            result = ser.readsignal()
            db.insert_signal(result)


def create_daemon(func):
    pid = os.fork()
    if pid > 0:
        with open('/var/run/OnkyoRIListener2.pid', 'w') as file:
            file.write(str(pid))
        sys.exit()
    elif pid == 0:
        func()


#---------------------------------------------------------------#
#------------------------- Entry Point -------------------------#
#---------------------------------------------------------------#


if __name__ == '__main__':
    mode = '' if len(sys.argv) == 1 else sys.argv[1]
    if mode == 'debug':
        main()
    else:
        create_daemon(main)
