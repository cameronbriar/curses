#!/usr/bin/env python

from field import Field
from sprite import Sprite
from weapon import Weapon
from key import Key

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
    

class Paddle:
    def __init__(self, start_x=0):
        self.sprite = Sprite()
        self.image = self.sprite.paddle()
        self.length = len(self.image)
        self.x = start_x 
        self.dx = 1
        return

    def move(self, direction):
        if direction == "LEFT":
             self.dx = -1
        else:
             self.dx = 1
        self.x += self.dx
        return

class Blocker:
    def __init__(self):
        print 'Blocker v1.0'

        self.field  = Field()
        self.weapon = Weapon()

        self.speed = 0.009
        self.running = False
        
        self.paddle_start_x = self.field.midx
        self.paddle_start_y = self.field.y - 1 
        self.paddle_x = self.field.midx
        
        self.paddle = Paddle(self.paddle_x)

        self.ball = Ball(x=52, y=5)

        self.key = Key().key
        return

    def add_paddle(self):
        coord = (self.paddle_start_y, self.paddle_start_x)
        self.field.addItem(self.paddle.image, coord)
        return

    def remove_paddle(self):
        coord = (self.paddle_start_y, self.paddle.x)
        blank = ' ' * len(self.paddle.image)
        self.field.addItem(blank, coord)
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
        return
    
    def walled(self, ball):
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

        if len(direction):
            return ' '.join(direction)
        return None
    
    def clearTrail(self, obj, remains=" ", centered=False):
        for i in range(len(obj.image)):
            self.field.addItem(remains, [obj.y, obj.x + i], centered)
        return

    def update(self, keystroke=0):
        self.remove_paddle()
        self.control(keystroke)
        paddle_coord = (self.paddle_start_y, self.paddle.x)
        self.field.addItem(self.paddle.image, paddle_coord)

        # ball
        hitWall = self.walled(self.ball)
        if hitWall:
            self.ball.bounce(hitWall)
        self.clearTrail(self.ball, " ")
        self.ball.move()
        self.field.addItem(self.ball.image, self.ball.getPosition())
        self.field.deploy()
        return 

    def run(self):
        if not self.running:
            self.init_game()
            self.running = True
        
        while self.running:
            c = self.field.display.getch()
            self.update(c)
            time.sleep(self.speed)
        self.field.destroy()
        return

game = Blocker()
game.run()
