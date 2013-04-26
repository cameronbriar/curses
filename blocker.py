#!/usr/bin/env python

from field import Field
from sprite import Sprite
from weapon import Weapon
from key import Key

import time
import random

class Ball():
    def __init__(self, image=random.choice(["o", "O", "@"]), x=1, y=1):
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
        return (self.x, self.y)

    def position(self, x, y):
        self.x, self.y = x, y
        return

class Paddle:
    def __init__(self, start_x=0):
        self.sprite = Sprite()
        self.image = self.sprite.paddle()
        self.length = len(self.image)
        self.half = self.length/2
        self.x = start_x
        self.dx = 1

        self.rx = (0, 0)
        return

    def move(self, direction):
        if direction == "LEFT":
             self.dx = -1
        else:
             self.dx = 1
        if self.x > self.rx[0] and self.x < self.rx[1]:
            self.x += self.dx
        else:
            if self.x <= self.rx[0] and direction == "RIGHT":
                self.x += self.dx
            elif self.x >= self.rx[1] and direction == "LEFT":
                self.x += self.dx
        return

class Blocker:
    def __init__(self):
        print 'Blocker v1.0'

        self.field  = Field(title="Blocker")
        self.weapon = Weapon()

        self.speed = 0.001
        self.running = False

        self.paddle_start_x = self.field.midx
        self.paddle_start_y = self.field.y - 1
        self.paddle_x = self.field.midx

        self.paddle = Paddle(self.paddle_x)
        self.paddle.rx = (1, self.field.x - len(self.paddle.image))

        self.ball = Ball(x=self.field.midx-5, y=1)

        self.key = Key().key

        self.collidables = []
        return

    def add_paddle(self):
        coord = (self.paddle_start_x, self.paddle_start_y)
        self.field.write_at(item=self.paddle.image, coords=coord)
        return

    def add_blocks(self, size=5):
        for x in range(size, (self.field.x-size), size*2):
            for row in range(3):
               coord = (x, 5*(row+1))
               block = self.weapon.block(length=size)
               self.field.write_at(item=block, coords=coord)
               self.collidables.append((coord, block))
        return

    def remove_paddle(self):
        coord = (self.paddle.x, self.paddle_start_y)
        blank = ' ' * len(self.paddle.image)
        self.field.write_at(item=blank, coords=coord)
        return

    def control(self, keystroke):
        if keystroke == self.key['left']:
            self.paddle.move('LEFT')
        elif keystroke == self.key['right']:
            self.paddle.move('RIGHT')
        elif keystroke == self.key['q']:
            self.running = False
        return

    def init_game(self):
        self.add_paddle()
        self.add_blocks()
        return

    def collision(self, ball):
        direction = []
        if ball.x < 1:
            direction.append('right')
        elif ball.x >= self.field.x-1:
            direction.append('left')

        if ball.y < 1:
            direction.append('down')
        elif ball.y >= self.field.y-2:
            if ball.x >= self.paddle.x and ball.x <= (self.paddle.x + self.paddle.length):
                direction.append('up')
            else:
                self.running = False

        # collidables
        if self.collidables != []:
            for item in self.collidables:
                x, y = item[0]
                if ball.y in (y, y+1, y-1):
                    if ball.x >= x and ball.x <= (x + len(item[1])):
                        if ball.y == y:
                            ball.dx *= -1
                        else:
                            ball.dy *= -1
                        self.field.remove(coords=item[0], item=item[1])
                        self.collidables.pop(self.collidables.index(item))
        if direction != []:
            return ' '.join(direction)
        if self.collidables == []:
            self.add_blocks()
        return None

    def clearTrail(self, obj, remains=" ", centered=False):
        for i in range(len(obj.image)):
            x, y = obj.x + i, obj.y
            self.field.write_at(item=remains, coords=(obj.x+i, obj.y), centered=centered)
        return

    def play(self, paddle, ball):
        x = paddle.x
        paddle.x = ball.x - paddle.half
        if paddle.x < 1 or paddle.x > (self.field.x - len(paddle.image)):
            paddle.x = x
        return

    def update(self, keystroke=0, timer=0):
        self.remove_paddle()
        self.play(self.paddle, self.ball)    # uncomment for AI
        self.control(keystroke)
        paddle_coord = (self.paddle.x, self.paddle_start_y)
        self.field.write_at(item=self.paddle.image, coords=paddle_coord)

        if timer % 10 == 1:
            # ball
            bounce = self.collision(self.ball)
            if bounce:
                self.ball.bounce(bounce)
            self.clearTrail(self.ball, " ")
            self.ball.move()
            self.field.write_at(item=self.ball.image, coords=self.ball.getPosition())
        self.field.deploy()
        return

    def run(self):
        if not self.running:
            self.init_game()
            self.running = True
        timer = 0
        while self.running:
            c = self.field.display.getch()
            self.update(c, timer)
            time.sleep(self.speed)
            timer += 1
        self.field.destroy()
        return

game = Blocker()
game.run()
