#!/usr/bin/env python


class Pet:

    def __init__(self):
        self.talk()

    def talk(self):
        print 'talk pet'


class Dog(Pet):

    def __init__(self):
        Pet.__init__(self)

    def talk(self):
        print 'talk dog'

d = Dog()
