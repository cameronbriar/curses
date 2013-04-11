"""
Simple animation for your shell
"""
from field import Field
import time

class Ball():
    def __init__(self, image="O", x=1, y=1):
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
        if direction in ['up', 'down']:
            self.dy *= -1
        elif direction in ['left', 'right']:
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
    def __init__(self, field=Field(), ball=Ball(), speed=0.009):
        self.field = field
        self.ball  = ball
        self.speed = speed
        return

    def update(self):
        hitWall = self.walled(self.ball)

        if hitWall:
            self.ball.bounce(hitWall)

        self.clearTrail(self.ball, " ", True)
        self.ball.move()


        self.field.addItem(self.ball.image, self.ball.getPosition())
        self.field.deploy()
        return

    def walled(self, ball):
        if ball.x < 1:
            return 'right'
        elif ball.x >= self.field.x-1:
            return 'left'

        if ball.y < 1:
            return 'down'
        elif ball.y >= self.field.y-1:
            return 'up'

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

s = Saver()
s.run()
