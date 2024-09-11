from random import randint
class Die:
	def __init__(self, sides=6):
		self.sides=sides

	def roll_die(self):
		random_number=randint(1,self.sides)
		print(random_number)

dies=Die(8)
dies.roll_die()


