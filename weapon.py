class Weapon:
    def __init__(self):
        return

    def block(self, image="|", length=10, width=1):
        return ''.join([image * length + '\n'] * width)[:-1]

    def cube(self, image="|", size=5):
        return ''.join([image * size + '\n'] * ((size/2)+1))[:-1]
