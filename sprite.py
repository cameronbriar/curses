class Sprite:
    def __init__(self):
        return

    def little_biker(self):
        return "( ) \n/_\\ \n{ }"

    def paddle(self):
        return "[--------]"

    def stick(self): # paddle was taken
        return "|[]|\n|  |\n|  |\n|  |\n|  |\n|[]|\n"


    def kirby(self, direction="front"):
        if direction == "front":
            return "<(-_-)>"
        elif direction == "left":
            return "<(-_-<)"
        elif direction == "right":
            return "(>-_-)>"
