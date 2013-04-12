"""
Simple animation for your shell
"""
from field import Field
import time
import random

class Ball():
    def __init__(self, image=random.choice(["o", "O", "@", "( )"]), x=1, y=1):
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

class Saver():
    def __init__(self, balls=int(random.random() * 100), trail=" "):
        self.field = Field()
        self.balls = [Ball(x=int(random.random() * self.field.x-1)+1, y=int(random.random() * self.field.y-1)+1) for x in range(balls)]
        self.speed = 0.009
        self.trail = trail
        return

    def update(self):
        for ball in self.balls:
            hitWall = self.walled(ball)

            if hitWall: # wall collision
                ball.bounce(hitWall)

            # ball collision


            self.clearTrail(ball, self.trail, True)
            ball.move()


            self.field.addItem(ball.image, ball.getPosition())

        # clear the field randomly (1% chance)
        if random.choice(range(100)) == 1:
            self.field.clearField()
        self.field.deploy()
        return

    def walled(self, ball):
        direction = []
        if ball.x < 1:
            direction.append('right')
        elif ball.x >= self.field.x-1:
            direction.append('left')

        if ball.y < 1:
            direction.append('down')
        elif ball.y >= self.field.y-1:
            direction.append('up')

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

s = Saver(50, " ~ ")
s.run()

