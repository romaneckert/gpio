#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

FPS = 60

lastFrameTime = time.time()
currentTime = time.time()
deltaTime = 0
sleepTime = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

p17 = GPIO.PWM(17, 1000)     # set Frequece to 1KHz
p17.start(0)
p17dc = 0
p17dc_direction = 1

p13 = GPIO.PWM(13, 1000)     # set Frequece to 1KHz
p13.start(0)
p13dc = 0
p13dc_direction = 1

def update():

    global p17dc_direction
    global p17dc

    global p13dc_direction
    global p13dc

    p17dc += deltaTime * 50 * p17dc_direction

    if p17dc < 0:
        p17dc = 0
        p17dc_direction *= -1

    if p17dc > 100:
        p17dc = 100
        p17dc_direction *= -1

    p17.ChangeDutyCycle(p17dc)

    p13dc += deltaTime * 50 * p13dc_direction * 3

    if p13dc < 0:
        p13dc = 0
        p13dc_direction *= -1

    if p13dc > 100:
        p13dc = 100
        p13dc_direction *= -1

    p13.ChangeDutyCycle(p13dc)

    print "%s %s" % (p17dc, p17dc_direction)

try:
    while True:

        currentTime = time.time()
        deltaTime = currentTime - lastFrameTime
        lastFrameTime = currentTime

        update()

        sleepTime = 1.0/FPS - deltaTime
        if sleepTime > 0:
            time.sleep(sleepTime)

#       p17.ChangeDutyCycle(deltaTime)


except KeyboardInterrupt:
    GPIO.output(17, 0)
    GPIO.output(13, 0)
    GPIO.cleanup()
