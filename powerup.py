import random
class Powerup:
    def __init__(self, type):
        self.type = type

powerup_proportion = 0.1

def random_powerup():
    return Powerup(random.randrange(3))
