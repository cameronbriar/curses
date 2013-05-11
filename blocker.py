#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from field import Field
from sprite import Sprite
from weapon import Weapon
from key import key

import time
import random


LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'


class Ball(object):
    def __init__(self, image=random.choice(["o", "O", "@"]), x=1, y=1):
        self.image = image
        self.length = len(image)
        self.x = x
        self.y = y
        self.dx = 1
        self.dy = 1

    def bounce(self, directions):
        if UP in directions or DOWN in directions:
            self.dy *= -1
        if RIGHT in directions or LEFT in directions:
            self.dx *= -1

        self.x += self.dx
        self.y += self.dy

    @property
    def position(self):
        return (self.x, self.y)


class Paddle(object):
    def __init__(self, startX=0):
        self.sprite = Sprite()
        self.image = self.sprite.paddle()
        self.length = len(self.image)
        self.half = self.length / 2
        self.x = startX
        self.dx = 1
        self.boundary = (0, 0)

    def move(self, direction):
        self.dx = -1 if direction == LEFT else 1
        if self.can_move(direction):
            self.x += self.dx

    def can_move(self, direction):
        if self.x in range(*self.boundary):
            return True
        if direction == RIGHT and self.x <= self.boundary[0]:
            return True
        if direction == LEFT and self.x >= self.boundary[1]:
            return True
        return False

    def hit(self, ball):  # should probably just be an int
        return ball.x in range(self.x, self.x + self.length + 1)

    def set_boundary(self, coords):
        self.boundary = coords


class BlockerGame(object):
    def __init__(self):
        self.field = Field(title="Blocker")
        self.weapon = Weapon()

        self.speed = 0.0001
        self.running = False

        self.paddleStartX = self.field.midx
        self.paddleStartY = self.field.y - 1
        self.paddleX = self.field.midx

        self.paddle = Paddle(self.paddleX)
        xMax = self.field.x - len(self.paddle.image)
        self.paddle.set_boundary((1, xMax))

        self.ball = Ball(x=self.field.midx - 5, y=10)

        self.key = key

        self.collidables = []

    def add_paddle(self):
        coord = (self.paddleStartX, self.paddleStartY)
        self.field.write_at(item=self.paddle.image, coords=coord)

    def add_blocks(self, size=5, rows=4, marginY=None, marginX=None):
        marginY = size if marginY is None else marginY
        marginX = size * 2 if marginX is None else marginX
        for x in range(size, (self.field.x - size), marginX):
            for row in range(rows):
                coord = (x, marginY * (row + 1))
                block = self.weapon.block(length=size)
                self.field.write_at(item=block, coords=coord)
                self.collidables.append((coord, block))

    def remove_paddle(self):
        coord = (self.paddle.x, self.paddleStartY)
        blank = ' ' * len(self.paddle.image)
        self.field.write_at(item=blank, coords=coord)

    def control(self, keystroke):
        if keystroke == self.key[LEFT]:
            self.paddle.move(LEFT)
        elif keystroke == self.key[RIGHT]:
            self.paddle.move(RIGHT)
        elif keystroke == self.key['q']:
            self.running = False

    def init_game(self):
        self.add_paddle()
        self.add_blocks()

    def move_ball(self):
        ball = self.ball

        ballDirections = []

        if ball.x < 1:
            ballDirections.append(RIGHT)
        elif ball.x >= self.field.x - 1:
            ballDirections.append(LEFT)

        if ball.y < 1:
            ballDirections.append(DOWN)
        elif ball.y >= self.field.y - 2:
            if self.paddle.hit(ball):
                ballDirections.append(UP)
            else:
                self.running = False  # we lost right?, let's rub it in somehow

        self.ball.bounce(ballDirections)

    def check_collisions(self):
        ball = self.ball

        if self.collidables:  # check if we hit anything
            for block in self.collidables:
                x, y = block[0]
                # margin of error
                if ball.y in (y, y + 1, y - 1):
                    if ball.x in range(x, x + len(block[1]) + 1):
                        if ball.y == y:
                            ball.dx *= -1
                        else:
                            ball.dy *= -1
                        self.field.remove(coords=block[0], item=block[1])
                        self.collidables.remove(block)
        if not self.collidables:
            raise Exception("Impossible!")  # you won!

    def clear_trail(self, obj, remains=" ", centered=False):
        for i in range(obj.length):
            x, y = obj.x + i, obj.y
            self.field.write_at(item=remains, coords=(x, y), centered=centered)

    def autoplay(self, paddle, ball):
        x = paddle.x
        paddle.x = ball.x - paddle.half
        if paddle.x < 1 or paddle.x > (self.field.x - len(paddle.image)):
            paddle.x = x

    def update(self, keystroke=0, timer=0):
        self.remove_paddle()
        #  self.autoplay(self.paddle, self.ball)  # AI
        self.control(keystroke)
        paddleCoord = (self.paddle.x, self.paddleStartY)
        self.field.write_at(item=self.paddle.image, coords=paddleCoord)

        if timer % 10 == 1:
            # ball movement
            self.clear_trail(self.ball, " ")
            self.move_ball()
            self.check_collisions()
            self.field.write_at(
                item=self.ball.image,
                coords=self.ball.position
            )
        self.field.deploy()

    def run(self):
        if not self.running:
            self.init_game()
            self.running = True
        timer = 0
        while self.running:
            c = self.field.display.getch()
            self.update(c, timer)
            time.sleep(self.speed)
            timer = (timer + 1) % 100
        self.field.destroy()

    def quit(self):
        self.field.destroy()


if __name__ == '__main__':
    try:
        print 'Blocker v1.0'
        game = BlockerGame()
        game.run()
    except KeyboardInterrupt:
        game.quit()
