#import sys
import pygame
import direction
import board


class Game:

	def __init__(self):
		# Create the game board
		self.board = board.Board()
		
		#graphic size of cells
		self.blockSize = 30
		
		# Initialize pygame
		pygame.init()
		
		#window
		self.screenSize = (self.board.width * self.blockSize, self.board.height * self.blockSize)
		self.screen = pygame.display.set_mode(self.screenSize)
		
		#timeticks
		self.timeStep = 70 # milliseconds per step
		pygame.time.set_timer(pygame.USEREVENT, self.timeStep)
	
	
	
	def drawRect(self, color, x, y):
		size = self.blockSize
		rect = (x * size, y * size, size, size)
		pygame.draw.rect(self.screen, color, rect, 0)
	
	def drawFood(self):
		(x, y) = self.board.food.position
		self.drawRect(self.board.food.color, x, y  )
	
	def drawSnake(self):
		for i in range(0, len(self.board.snake.body)):
			if i == 0:
				color = self.board.snake.headColor
			else:
				color = self.board.snake.bodyColor
			(x, y) = self.board.snake.body[i]
			self.drawRect(color, x, y)
	
	def updateScreen(self):
		self.screen.fill(self.board.color)
		self.drawSnake()
		self.drawFood();
		pygame.display.update()
	
	
	
	def run(self):
		result = True
		while result:
			event = pygame.event.wait()
			
			# close window
			if event.type == pygame.QUIT: 
				pygame.quit()
				return #sys.quit(0)
			
			# get decision of player (human or AI)
			decision = play(event, self.board)
			# act on it
			self.board.command(decision)
			
			# turn ended, update
			if event.type == pygame.USEREVENT:
				result = self.board.update() != self.board.DEATH
			self.updateScreen()
			
		# Game over!
		for i in range(0, 10):
			self.updateScreen()
			pygame.time.wait(100)
	
	
	
	
	
	
	
