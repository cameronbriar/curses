"""
Manual inspection required... -0)0
"""
from player import Player

p = Player()

def test_player_appearance():
    for player in dir(p):
        if '__' not in player:
            image = getattr(p, player)()
            print image, ' ' * 10, player
            print '\n\n'
    return

print """
Player appearance test
----------------------
"""

test_player_appearance()
