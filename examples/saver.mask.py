"""
Simple animation for your shell
"""
from field import Field
import time
import random
from saver import Ball, Saver

class MaskSaver(Saver):

    def __init__(self, balls=int(random.random() * 100), trail=" ", mask=None):
        self.field = Field(title="Term Saver")
        self.balls = [Ball(x=int(random.random() * self.field.x-1)+1, y=int(random.random() * self.field.y-1)+1) for x in range(balls)]
        self.speed = 0.009
        self.trail = trail
        self.addMask(mask)

    def addMask(self, mask):
        """
        Given a 2D array depciting some image to mask out
        e.g. a box or a name or a picture of peeve
        shrink or fatten it up to fit the shape of our field/grid
        dimensions must be at least.... 4 x 4 ? e.g.
        
        . . . .
        . x x .
        . x x .
        . . . .

        The players on the field should never write to 
        the 'x'd out areas.

        but our grid will probably be larger than this...
        so what is the maths behind making this fit properly?
        e.g. a 4 x 4 mask supplied for a 64 x 64 grid
        let's start small and just double it
        
        . . . . . . . .      . . . . . . . .      . . . . . . . .
        . . . . . . . .      . x x x x x x .      . . . . . . . .
        . . . . . . . .      . x x x x x x .      . . x x x x . .
        . . . . . . . .      . x x x x x x .      . . x x x x . .
        . . . . . . . .  =>  . x x x x x x .  or  . . x x x x . .
        . . . . . . . .      . x x x x x x .      . . x x x x . .
        . . . . . . . .      . x x x x x x .      . . . . . . . .
        . . . . . . . .      . . . . . . . .      . . . . . . . .
                                  bad                  good

        I think the result where we look at the proportionality works best.
        The first transformation has a single border like the original,
        and the second maintains the proportions (e.g. 50%).

        What happens when it's more awkward?

        . . . . . .      . . . . . .      . . . . . .
        . . . . . .  =>  . x x x x .  or  . . x x . .
        . . . . . .      . . . . . .      . . . . . .
                             bad              good

        I still like the second transformation.
        So I guess when taking 1/2 of an odd, round down?
        """
        pass

    def update(self):
        for ball in self.balls:
            hitWall = self.walled(ball)

            if hitWall: # wall collision
                ball.bounce(hitWall)

            # ball collision

            self.clearTrail(ball, self.trail, True)
            ball.move()

            self.field.write_at(item=ball.image, coords=ball.getPosition())

        # clear the field randomly (.1% chance)
        if random.choice(range(1000)) == 1:
            self.field.clear()

        self.field.deploy()

tails = lambda: random.choice([' >< ', ' # ', '*', ' * ', ' () ', ') (', '-_-', '[]', '][', '] ['])
s = MaskSaver(50, tails())
s.run()

