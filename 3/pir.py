#!/usr/bin/python

import time
import RPi.GPIO as GPIO

#print(GPIO.VERSION)

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)

def interrupt_fired(channel):
    print("interrupt fired")
    print(chaanel)

GPIO.add_event_detect(14, GPIO.FALLING, callback=interrupt_fired)

while (True):
    time.sleep(1)
    print("Timer Fired")
