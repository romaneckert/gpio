#!/usr/bin/env python
import time


class Controller:

    fps = 4

    delta_time = 0
    start_time = 0
    loop = 0

    def __init__(self):
        self.start_time = time.time()
        self.run()

    def run(self):
        while True:
            self.loop = self.loop % self.fps + 1

            self.delta_time = (time.time() - self.start_time) % 1

            self.update()

            sleep_time = float(self.loop) / float(self.fps) - ((time.time() - self.start_time) % 1)

            time.sleep(sleep_time)

            #sleep_time = 1.0/self.fps - (time.time() - update_time)

            #if sleep_time > 0:


    def update(self):
        print 'must implement update function'


