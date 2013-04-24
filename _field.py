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
        curses.start_color()
        curses.use_default_colors()

        curses.init_pair(1, curses.COLOR_BLACK,   -1)
        curses.init_pair(2, curses.COLOR_BLUE,    -1)
        curses.init_pair(3, curses.COLOR_CYAN,    -1)
        curses.init_pair(4, curses.COLOR_GREEN,   -1)
        curses.init_pair(5, curses.COLOR_MAGENTA, -1)
        curses.init_pair(6, curses.COLOR_RED,     -1)
        curses.init_pair(7, curses.COLOR_WHITE,   -1)
        curses.init_pair(8, curses.COLOR_YELLOW,  -1)

        self.colors = {
            'black'   : 1,
            'blue'    : 2,
            'cyan'    : 3,
            'green'   : 4,
            'magenta' : 5,
            'red'     : 6,
            'white'   : 7,
            'yellow'  : 8,
        }

        self.random_color = lambda: curses.color_pair(self.colors[random.choice(self.colors.keys())])

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

    def clearField(self):
        self.grid = [' '] * self.x * self.y
        return

    def deploy(self):
        for x, i in enumerate(self.grid):
            y = x / self.x
            x = x % self.x
            self.display.addstr(y, x, i, curses.color_pair(self.colors['blue']))
        self.display.refresh()

    def addItem(self, item, coords, centered=False):
        y = coords[0] * self.x
        x = coords[1]
        if centered:
            x -= len(item)/2
        for c, i in enumerate(item):
            spot = x + y + c
            try:
                self.grid[spot] = i
            except:
                continue

# Usage
#field = Field()
#grid = field.getField()
#grid = [random.choice(['|', '_']) for x in grid]
#field.setField(grid)
#field.addItem('X', field.midp)
#field.deploy()
#curses.napms(5000)
#field.destroy()
