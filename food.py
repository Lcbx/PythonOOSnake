import random

class Food:
	color = (255, 255, 0)
	# used to be an array
	#foodColors = [(255, 255, 0),] # yellow
	#(0, 255, 255), # cyan
    #(255, 0, 255), # magenta
    #(128, 128, 255), # light blue

	def __init__(self, width, height):
		self.position = (random.randint(0, width - 1), random.randint(0, height - 1))
		#self.color = random.choice(self.foodColors)