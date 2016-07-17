#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

try:
    while True:

        print '...start...'
        GPIO.output(27, 1)
        time.sleep(0.1)
        GPIO.output(27, 0)
        time.sleep(0.1)
        GPIO.output(17, 1)
        time.sleep(0.1)
        GPIO.output(17, 0)
        time.sleep(0.1)
        GPIO.output(13, 1)
        time.sleep(0.1)
        GPIO.output(13, 0)
        time.sleep(0.1)
        GPIO.output(17, 1)
        time.sleep(0.1)
        GPIO.output(17, 0)
        time.sleep(0.1)
        # GPIO.output(LedPin, GPIO.HIGH)
        # time.sleep(0.5)
        # GPIO.output(LedPin, GPIO.LOW)
        # time.sleep(0.5)
        # GPIO.output(LedPin, GPIO.HIGH)
        # time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.output(27, 0)
    GPIO.output(17, 0)
    GPIO.output(13, 0)
    GPIO.cleanup()