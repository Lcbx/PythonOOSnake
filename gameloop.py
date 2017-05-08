#import sys
import pygame
import direction
import board
from threading import Thread, Timer

		
class ComputeThread(Thread):
	def __init__(self, board):
		Thread.__init__(self)
		self.board = board
	
	def run(self):
		startTurn(self.board)
		
		

class Game:

	def __init__(self):
		# Create the game board
		self.board = board.Board()
		
		#graphic size of cells
		self.blockSize = 60
		
		# Initialize pygame
		pygame.init()
		
		#window
		self.screenSize = (self.board.width * self.blockSize, self.board.height * self.blockSize)
		self.screen = pygame.display.set_mode(self.screenSize)
		
		#timeticks
		self.timeStep = 100 # milliseconds per step
		pygame.time.set_timer(pygame.USEREVENT, self.timeStep)
	
	
	def run(self):
		
		loop = True
		while loop:
			
			# thread to let the AIs begin computations
			thread = ComputeThread(self.board)
			thread.start()
			
			# get events : clos window, key press or timer expired
			event = pygame.event.wait()
			
			# close window
			if event.type == pygame.QUIT: 
				pygame.quit()
				return 
			
			# handle key press
			elif event.type == pygame.KEYDOWN:
				handleKey(event)
			
			# timer expired
			elif event.type == pygame.USEREVENT:
				# get decision of player (human or AI)
				decision = play()
				# act on it
				if decision!=None : self.board.command(decision)
				# update the board
				loop = self.board.endTurn() != self.board.DEATH
			
			# draw calls
			self.updateScreen()
			
		# Game over!
		for i in range(0, 10):
			self.updateScreen()
			pygame.time.wait(100)
	
	
	
	
	def updateScreen(self):
		self.screen.fill(self.board.color)
		self.drawSnake()
		self.drawFood();
		pygame.display.update()
	
	
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
	

		
	
	
	
	
	
	