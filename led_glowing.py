#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

p = GPIO.PWM(17, 1000)     # set Frequece to 1KHz
p.start(0)

try:
    while True:
        for dc in range(0, 101, 5):  # Increase duty cycle: 0~100
            p.ChangeDutyCycle(dc)  # Change duty cycle
            time.sleep(0.05)
        for dc in range(100, -1, -5):  # Decrease duty cycle: 100~0
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)

except KeyboardInterrupt:
    GPIO.output(17, 0)
    GPIO.cleanup()