import direction


class Snake:

	headColor = (10, 255, 10)
	bodyColor = (0, 100, 30)
		
	def __init__(self, x = 10, y = 10, length = 3):
		self.direction = direction.right()
		self.body = []
		self.growLength = 0
		for i in range(0, length):
			self.body.append((x - i, y))

	def move(self):
		"""Move the snake in the given direction."""
		position = self.body[0] # get old position of head
		x, y = self.direction.addTo(position) # calculate new position of head
		if self.growLength > 0:
			self.growLength -= 1 # grow
		else:
			self.body.pop() # remove tail
		self.body.insert(0, (x, y)) # insert new position of head
		if self.body[0] in self.body[1:]: # does the head collide with the rest of the body?
			return False # yes, then this is an invalid move
		return True # no

	def grow(self, length = 1):
		self.growLength = length
