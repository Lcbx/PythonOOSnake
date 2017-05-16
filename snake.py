import direction


class Snake:
	
	headColor = (100,60,150)
	color = (100,150,20)
		
	def __init__(self, x = 5, y = 3, length = 3):
		self.direction = direction.right()
		self.body = []
		self.growLength = 0
		for i in range(0, length):
			self.body.append((x - i, y))
	
	def getHead(self):
		return self.body[0]
	
	def grow(self, length = 1):
		self.growLength += length
	
	def move(self):
		# get old position of head
		position = self.getHead()
		# calculate new position of head
		x, y = self.direction.addTo(position) 
		# insert new position of head
		self.body.insert(0, (x, y)) 
		# if the snake isn't growing, get rid of last tail
		if self.growLength == 0:
			self.body.pop()
		# otherwise decrease grow count
		else: 
			self.growLength -= 1