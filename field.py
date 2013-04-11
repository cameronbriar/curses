#!/usr/bin/env python

import os
import sys
import time
import random

import curses

class Field():

    def __init__(self, size=None):
        self.display = curses.initscr()
        self.display.keypad(1)
        self.display.timeout(0)
        curses.noecho()
        curses.cbreak()

        self.dims = self.display.getmaxyx()
        self.size = size if size else [self.dims[0]-1, self.dims[1]-1]
        self.y = self.size[0]
        self.x = self.size[1]
        self.grid = [' '] * self.x * self.y

        self.midx = self.x / 2
        self.midy = self.y / 2
        self.midp = [self.midy, self.midx]
        return

    def destroy(self):
        curses.endwin()
        return

    def getField(self):
        return self.grid

    def setField(self, field):
        self.grid = field
        return

    def deploy(self):
        for x, i in enumerate(self.grid):
            y = x / self.x
            x = x % self.x
            self.display.addstr(y, x, i)
        self.display.refresh()

    def addItem(self, item, coords, centered=False):
        y = coords[0] * self.x
        x = coords[1]
        if centered:
            x -= len(item)/2
        for c, i in enumerate(item):
            spot = x + y + c
            self.grid[spot] = i

# Usage
#field = Field()
#grid = field.getField()
#grid = [random.choice(['|', '_']) for x in grid]
#field.setField(grid)
#field.addItem('X', field.midp)
#field.deploy()
#time.sleep(5)
#field.destroy()
