from random import randint

class Die:
    """A class representing a die."""

    def __init__(self,num_sides=6):
        """asume six sided die."""
        self.num_sides=num_sides

    def roll(self):
        """return a random value"""
        return  randint(1,self.num_sides)


