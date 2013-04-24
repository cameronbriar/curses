#!/usr/bin/env python

from field import Field
from sprite import Sprite
from weapon import Weapon
from key import Key

import time
import random

class Paddle:
    def __init__(self, start_x=0):
        self.sprite = Sprite()
        self.image = self.sprite.paddle()
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

    def update(self, keystroke=0):
        self.remove_paddle()
        self.control(keystroke)
        paddle_coord = (self.paddle_start_y, self.paddle.x)
        self.field.addItem(self.paddle.image, paddle_coord)
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
