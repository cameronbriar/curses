"""
Manual inspection required... -0)0
"""
from sprite import Sprite

s = Sprite()

def test_sprite_appearance():
    for sprite in dir(s):
        if '__' not in sprite:
            image = getattr(s, sprite)()
            print image, ' ' * 10, sprite
            print '\n\n'
    return

print """
Sprite appearance test
----------------------
"""

test_sprite_appearance()
