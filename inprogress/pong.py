#!/usr/bin/env python
"""
Pong | .    |

"""

import field
import weapon
import sprites
import key

class Game(object):
    def __init__(self):
        self.time = 0
        self.tick = 0
        self.is_running = False

        self.players = []
        self.zombies = []
        self.scores  = []
        self.collidables = {}
        for x in range(4):
            self.collidables['quadrant_%d' % (x+1)] = []

        self.key = key.Key.key # err..


class Pong(Game):
    def __init__(self):
        pass

    def rules(self):
        return """
PONG

A player on each side of the screen is able to go up and down
in order to prevent the opposing player from bouncing
the one ball on the field into their side.

               |                                  |                 
     player 1  | |                                |       player 1's
         ----> | |                                |  <----    goal 
               | |      o                         |                 
               |                                | |                 
               |                                | | <-----                
 player 2's    |                                | |   player 2    
   goal ---->  |                                  |       
               |                                  |                 
               |                                  |                 
               |                                  |
"""

    def setup_game(self, players=1):
        for x in range(players):
            paddle = self.new_paddle()
            self.players.append(paddle)

        for x in range(players, 2):
            enemy_paddle = self.new_paddle()
            self.zombies.append(enemy_paddle)

        self.scores = [0 for x in range(2)]  # these twos might change

        self.zombies.append(new_ball())

        

    def new_paddle(self):
        return particle.Block(image="[]", width="5")

    def new_ball(self):
        return particle.Ball()

    def paddle_control(self, paddle, keystroke=None):
        current_x = paddle.x
        current_y = paddle.y

        if keystroke:
            if keystroke == self.key['up']:
                paddle.y -= 1
            elif keystroke == self.key['down']:
                paddle.y += 1

        if self.collided(paddle):
            paddle.y = current_y

    def ball_control(self, ball):
        current_x = ball.x
        current_y = ball.y

        bounce = self.collided(ball)
        if bounce:
            # bounce is a point
            pass 

# .... pause

# .... need to do work work
