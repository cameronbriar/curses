"""
Simple animation for your shell
"""
from field import Field
import time
import random

class Drop():
    def __init__(self, image=random.choice(["o", "O", "@", "."]), x=1, y=1):
        self.image = image
        self.x = x
        self.y = y
        self.dx = 1
        self.dy = 1
        return

    def move(self):
        self.x += self.dx
        self.y += self.dy
        return

    def bounce(self, direction):
        if 'up' in direction or 'down' in direction:
            self.dy *= -1
        if 'right' in direction or 'left' in direction:
            self.dx *= -1
        return

    def getVelocity(self):
        return (self.dx, self.dy)

    def velocity(self, dx, dy):
        self.dx, self.dy = dx, dy
        return

    def getPosition(self):
        return (self.y, self.x)

    def position(self, x, y):
        self.x, self.y = x, y
        return


class Rain():
    def __init__(self, drops=int(random.random() * 100), trail=" "):
        self.field = Field()
        self.drops = [Drop(x=int(random.random() * self.field.x-1)+1, y=int(random.random() * self.field.y-1)+1) for x in range(drops)]
        self.speed = 0.009
        self.trail = trail
        self.wind  = random.choice((1, -1, 0))
        return

    def new_drop(self):
        newdrop = Drop(x=int(random.random() * self.field.x-1)+1, y=int(random.random() * self.field.y-1)+1)
        newdrop.dx = self.wind
        return newdrop

    def update(self):
        for drop in self.drops:
            hitWall = self.walled(drop)

            if hitWall: # wall collision
                drop.bounce(hitWall)

                if 'more' in hitWall:
                    self.drops.pop(self.drops.index(drop))
                    self.drops.append(self.new_drop())

            self.clearTrail(drop, self.trail, True)
            drop.move()

            self.field.addItem(drop.image, drop.getPosition(), color='blue')

        # clear the field randomly (.1% chance)
        #if random.choice(range(1000)) == 1:
        #    self.field.clearField()
        self.field.deploy()
        return

    def walled(self, drop):
        direction = []
        if drop.x < 1:
            direction.append('right')
        elif drop.x >= self.field.x-1:
            direction.append('left')

        if drop.y < 1:
            direction.append('down')
        elif drop.y >= self.field.y-1:
            direction.append('more')

        if len(direction):
            return ' '.join(direction)
        return None


    def run(self):
        run = 1
        while run:
            c = self.field.display.getch()
            if c == ord('q'):
                run = 0
            self.update()
            time.sleep(self.speed)
        self.field.destroy()
        return

    def clearTrail(self, obj, remains=" ", centered=False):
        for i in range(len(obj.image)):
            self.field.addItem(remains, [obj.y, obj.x + i], centered)
        return

#tails = lambda: random.choice([' >< ', ' # ', '*', ' * ', ' () ', ') (', '-_-', '[]', '][', '] ['])
#tails = lambda: "FREE"
tails = lambda: " "
r = Rain(5, tails())
r.run()

