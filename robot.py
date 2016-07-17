#!/usr/bin/env python
from hawk.controller import Controller


class Robot(Controller):

    def __init__(self):
        Controller.__init__(self)

    def update(self):
        print "delta: " + str(self.delta_time)


robot = Robot()



