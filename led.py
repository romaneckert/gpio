#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

LedPin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPin,GPIO.OUT)
GPIO.output(LedPin,GPIO.HIGH)

try:
    while True:

        print '...start...'
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(2)
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()