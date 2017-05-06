import copy
import snake
import food

#contains all the game state
class Board:
	
	#state constants
	DEATH = -1
	NORMAL = 0
	SNACK = 1
	
	#background
	color = (50, 30, 10)
	
	def __init__(self):
		
		#dimensions
		self.width = 20 # size of field width in blocks
		self.height = 20
		
		#actors
		self.snake = snake.Snake()
		self.food = food.Food(self.width, self.height)
	
	def command(self, input):
		self.snake.direction = input
	
	#state manipulation
	def update(self):
		snakeCollidesSnake = not self.snake.move()
		x, y = self.snake.body[0]
		snakeCollidesWall = x < 0 or x >= self.width or y < 0 or y >= self.height
		if snakeCollidesSnake or snakeCollidesWall:
			return self.DEATH
		if self.snake.body[0] == self.food.position:
			self.snake.grow()
			self.food = food.Food(self.width, self.height)
			return self.SNACK
		return self.NORMAL
	
	def clone(self):
		return copy.deepcopy(self)