#!/usr/bin/env python

class Particle(object):
    def __init__(self):
        self.x  = 0
        self.y  = 0
        self.dx = 0
        self.dy = 0
        self.vx = 0
        self.vy = 0
        self.area  = []
        self.image = ""

    def set_xy(self, x, y):
        self.x, self.y = x, y

    def get_xy(self):
        return (self.x, self.y)

    def set_area(self):
        """
        a particle's area is similar to its bounding area
        if a point is blank (" ") then it's considered an
        open space for other particles to exist in
        """
        return
