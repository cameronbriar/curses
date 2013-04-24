#!/usr/bin/env python

from field import Field
from sprite import Sprite
from weapon import Weapon

import time
import random

class Blocker:
    def __init__(self):
        print 'Blocker v1.0'

        self.field  = Field()
        self.sprite = Sprite()
        self.weapon = Weapon()

        self.paddle = self.sprite.paddle()
        self.paddle_start_x = self.field.midx
        self.paddle_start_y = self.field.y - 1 
        return

    def add_paddle(self):
        coord = (self.paddle_start_y, self.paddle_start_x)
        self.field.addItem(self.paddle, coord)
        return

    def run(self):
        self.add_paddle()
        self.field.deploy()
        time.sleep(5)
        self.field.destroy()
        return

game = Blocker()
game.run()
