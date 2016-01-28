#!/usr/bin/env python

import sys
import random

import curses

"""
The FIELD Class

-- In charge of writing, reading and displaying to your terminal window.

"""

class Field(object):

    def __init__(self, title="[..]", size=None):
        self.title = title
        sys.stdout.write(''.join(('\x1b]2;', title, '\x07')))

        self.display = curses.initscr()
        self.display.keypad(1)
        self.display.timeout(0)

        curses.noecho()
        curses.cbreak()
        curses.start_color()
        curses.use_default_colors()
        curses.curs_set(0)

        curses.init_pair(1, curses.COLOR_BLACK,   -1)
        curses.init_pair(2, curses.COLOR_BLUE,    -1)
        curses.init_pair(3, curses.COLOR_CYAN,    -1)
        curses.init_pair(4, curses.COLOR_GREEN,   -1)
        curses.init_pair(5, curses.COLOR_MAGENTA, -1)
        curses.init_pair(6, curses.COLOR_RED,     -1)
        curses.init_pair(7, curses.COLOR_WHITE,   -1)
        curses.init_pair(8, curses.COLOR_YELLOW,  -1)

        self.colors = {
            'black'   : lambda: curses.color_pair(1),
            'blue'    : lambda: curses.color_pair(2),
            'cyan'    : lambda: curses.color_pair(3),
            'green'   : lambda: curses.color_pair(4),
            'magenta' : lambda: curses.color_pair(5),
            'red'     : lambda: curses.color_pair(6),
            'white'   : lambda: curses.color_pair(7),
            'yellow'  : lambda: curses.color_pair(8),
        }
        
        
        
        self.dims = self.display.getmaxyx()
        self.size = size if size else (self.dims[0], self.dims[1])
        self.y = self.size[0] -1
        self.x = self.size[1] -1
        self.length = self.x * self.y
        
        self.field = [' ' for x in range(self.length)]

        self.midx = self.x / 2
        self.midy = self.y / 2
        self.midp = [self.midx, self.midy]

    def destroy(self):
        curses.endwin()

    def refresh(self):
        self.display.refresh()

    def get(self):
        return self.field

    def set(self, field):
        self.field = field

    def clear(self):
        self.field = [" " for x in self.field]

    def write(self, character=" ", x=0, y=0, color=None):
        if color:
            self.display.addstr(y, x, character, self.colors[color]())
        else:
            self.display.addstr(y, x, character)

    def deploy(self):
        for x, spot in enumerate(self.field):
            py = x / self.x
            px = x % self.x
            color = 0
            if len(spot) == 2:
                spot, color = spot
            self.write(spot, px, py, color)
        self.refresh()

    def location_of(self, item=None, x=0, y=0, coords=None, centered=False):
        item = item.split('\n')
        x, y = (x, y) if not coords else coords
        px = x if not centered else x - len(item[0])/2
        py = y * self.x
        location = []
        for pieces in item:
            for x, bit in enumerate(pieces):
                spot = px + py + x
                if spot < 0 or spot >= self.length:
                    spot = 0
                location.append(spot)
            py += self.x
        return location

    def item_at(self, x=0, y=0, coords=None):
        px, py = (x, y) if not coords else coords
        py *= self.x
        spot = px + py
        return self.field[spot]
        
    def remove(self, x=0, y=0, coords=None, replacement=" ", item=None, centered=False, color=None):
        px, py = (x, y) if not coords else coords
        replacement = replacement if not item else (" " * len(item))
        self.write_at(replacement, px, py, None, centered, None)

    def write_at(self, item=" ", x=0, y=0, coords=None, centered=None, color=None):
        px, py = (x, y) if not coords else coords
        area_to_write = self.location_of(item, px, py, None, centered)
        item = item.replace('\n', '')
        for i, area in enumerate(area_to_write):
            self.field[area] = (item[i], color)

# Usage
#field = Field()
#grid = field.getField()
#grid = [random.choice(['|', '_']) for x in grid]
#field.setField(grid)
#import weapon
#w = weapon.Weapon().cube(size=60)
#field.write_at(item=w, coords=field.midp, centered=True)
#field.deploy()
#curses.napms(5000)
#field.destroy()
