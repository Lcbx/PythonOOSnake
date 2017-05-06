import copy
import snake
import food

#contains all the game state
class Board:
	
	#state constants
	DEATH = -100
	NORMAL = -1
	SNACK = 10
	
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
		# does the snake collide with itself?
		snakeCollidesSnake = not self.snake.move()
		x, y = self.snake.getHead()
		# does the snake collide with a wall?
		snakeCollidesWall = x < 0 or x >= self.width or y < 0 or y >= self.height
		# if so it's dead KAPUT
		if snakeCollidesSnake or snakeCollidesWall:
			return self.DEATH
		#i t's a different story with food
		if (x, y) == self.food.position:
			# the snake grows
			self.snake.grow()
			# new food somewhere else
			self.food = food.Food(self.width, self.height)
			return self.SNACK
		# nah just usual snaky stuff
		return self.NORMAL
	
	def clone(self):
		return copy.deepcopy(self)
	
	#important for the AI
	def nextState(self, input):
		clone = self.clone()
		clone.command(input)
		clone.update()
		return clone
	
	
	
	