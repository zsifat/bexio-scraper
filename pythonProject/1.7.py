class Restaurent:
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurent_name=restaurant_name
		self.cuisine_type=cuisine_type

	def describe_restaurant(self):
		print(f"{self.restaurent_name} has {self.cuisine_type}.")

	def open_restaurent(self):
		print(f"{self.restaurent_name} is now open.")

restaurent_1=Restaurent('Antalya','sweet')
restaurent_2=Restaurent('Skylight','drinks')
restaurent_3=Restaurent('BBQBLAST','fastfood')

restaurent_1.describe_restaurant()
restaurent_2.describe_restaurant()
restaurent_3.describe_restaurant()