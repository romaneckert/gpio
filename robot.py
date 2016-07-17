#!/usr/bin/env python
from hawk.controller import Controller
import RPi.GPIO as GPIO


class Robot(Controller):

    motor = None

    def __init__(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        self.motor = GPIO.PWM(17, 50)
        self.motor.start(5)

        self.activate()

    def update(self):

        print "delta: " + str(self.delta_time)


robot = Robot()



