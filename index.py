#!/usr/bin/python3

#
# Author: jun10000 (https://github.com/jun10000)
#

import os
import signal
import sys
import time
from collections import deque
from RPi import GPIO

import settings
import JunLib
import wave_signal
from DBController import DBController



db_controller = DBController()

def initialise():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(settings.INPUT_PIN, GPIO.IN)

    global db_controller
    db_controller.connect()



buffer = deque()

# noinspection PyUnusedLocal
def loop(signal_num, frame):
    global buffer
    buffer.append(GPIO.input(settings.INPUT_PIN))

    if len(buffer) > wave_signal.SIGNAL_MAX_LENGTH:
        buffer.popleft()

    for (name, value) in wave_signal.SIGNAL.items():
        if JunLib.contains_last_listitems(value, buffer):
            buffer.clear()

            global db_controller
            db_controller.insert_signal(name)
            break



is_status_term = False

# noinspection PyUnusedLocal
def set_status_term(signal_num, frame):
    global is_status_term
    is_status_term = True


def finalise():
    GPIO.cleanup()

    global db_controller
    db_controller.disconnect()


def run():
    try:
        initialise()
        signal.signal(signal.SIGALRM, loop)
        signal.setitimer(signal.ITIMER_REAL, settings.WAIT_TIME, settings.WAIT_TIME)
        signal.signal(signal.SIGTERM, set_status_term)

        global is_status_term
        while not is_status_term:
            time.sleep(1)
    finally:
        finalise()


def create_daemon(func):
    pid = os.fork()

    if pid > 0:
        with open('/var/run/OnkyoRIListener.pid', 'w') as file:
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
        run()
    else:
        create_daemon(run)
