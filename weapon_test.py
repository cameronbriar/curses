"""
Manual inspection required... -0)0
"""
from weapon import Weapon

w = Weapon()

def test_weapon_appearance():
    for weapon in dir(w):
        if '__' not in weapon:
            image = getattr(w, weapon)()
            print image, ' ' * 10, weapon
            print '\n\n'
    return

print """
Weapon appearance test
----------------------
"""

test_weapon_appearance()
