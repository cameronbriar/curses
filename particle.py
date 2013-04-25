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
        if a point is blank (whitespace) then it's considered an
        open space (mass-less) for other particles to exist
        """
        x, y = self.x, self.y
        dimensions = 1
        for part in self.image.split('\n'):
            for piece in part:
                mass = 1 if piece != " " else 0
                self.area.append((x, y, mass))
                x += 1
            x, y = self.x, self.y + dimensions
            dimensions += 1
        return

    def reset_area(self):
        self.area = []
        self.set_area()

class Ball(Particle):
    def init(self, image="O"):
        self.image = image
        self.set_area()

class Block(Particle):
    def init(self, image="|", length=1):
        self.length = length
        self.image = image * length
        self.set_area()

    def set_size(self, length=1):
        self.length = length
        self.image = self.image * length
        self.reset_area()

class Cube(Particle):
    def init(self, image="|", width=1, length=1):
        self.width = width
        self.length = length
        self.image = '\n'.join([image * length] * ((width/2)+1))
        self.set_area()

    def set_image(self):
        self.image = '\n'.join([self.image * self.length] * ((self.width/2)+1))

    def set_size(self, width=None, length=None):
        self.width = width or self.width
        self.length = length or self.length
        self.set_image()
        self.reset_area()

b = Ball()
b.init("o")
print b.area

b = Block()
b.init(length=1)
print b.area
b.set_size(5)
print b.area

c = Cube()
c.init()
print c.area
c.set_size(width=10, length=10)
print c.area
