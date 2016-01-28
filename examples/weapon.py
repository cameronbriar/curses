class Weapon:
    def __init__(self):
        return

    def block(self, image="|", length=10, width=1):
        return '\n'.join([image * length] * width)

    def cube(self, image="|", size=5):
        return '\n'.join([image * size] * ((size/2)+1))
