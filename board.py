import copy
import snake
import food

#contains all the game state
class Board:
	
	#state constants
	DEATH = -999
	NORMAL = 0
	SNACK = 200
	
	#background
	color = (50, 30, 10)
	
	def __init__(self):
		
		#dimensions
		self.width = 7
		self.height = 7
		
		#actors
		self.snakeIsdead = False
		self.snake = snake.Snake()
		self.food = food.Food(self.width, self.height)
	
	def command(self, decision):
		self.snake.direction = decision
	
	#state manipulation
	def endTurn(self):
		# if the snake is dead, state is DEAD
		if self.snakeIsdead : return self.DEATH
		# move the snake
		self.snake.move()
		# position of snake's head
		x, y = self.snake.getHead()
		# does the snake collide with itself?
		snakeCollidesSnake = (x, y) in self.snake.body[1:]
		# does the snake collide with a wall?
		snakeCollidesWall = x < 0 or x >= self.width or y < 0 or y >= self.height
		# if so it's dead KAPUT
		if snakeCollidesSnake or snakeCollidesWall:
			self.snakeIsdead =True
			return self.DEATH
		# it's a different story with food
		if (x, y) == self.food.position:
			# the snake grows
			self.snake.grow()
			# new food somewhere else
			self.food = food.Food(self.width, self.height)
			return self.SNACK
		# nah just usual snaky stuff
		return self.NORMAL
	
	def endTurnDecision(self, decision):
		self.command(decision)
		return self.endTurn()
	
	def clone(self):
		return copy.deepcopy(self)
	
	#important for the AI
	def potentialEndturn(self, decision):
		clone = self.clone()
		clone.command(decision)
		result = clone.endTurn()
		return result, clone
	
	def potentialEndturnResult(self, decision):
		result, clone = self.potentialEndturn(decision)
		return result
	
	
	
	
	
	