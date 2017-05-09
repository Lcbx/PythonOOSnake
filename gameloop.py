#import sys
import pygame
import direction
import board
from threading import Thread


import debug

		
class PlayerThread(Thread):
	def __init__(self, board, timeStep):
		Thread.__init__(self)
		self.board = board
		self.timeStep = timeStep
		self.player = getPlayer(self.board, self.timeStep)
	
	def run(self):
		self.player.think()
		
	def handleKey(self, event):
		self.player.handleKey(event)
	
	def getDecision(self):
		return self.player.getDecision()
		

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
			
			# draw calls
			self.updateScreen()
			
			# thread to let the AIs begin computations
			thread = PlayerThread(self.board, self.timeStep)
			thread.start()
			
			# loop for interrupts
			while loop :
				
				# get events : clos window, key press or timer expired
				event = pygame.event.wait()
				
				# close window
				if event.type == pygame.QUIT: 
					pygame.quit()
					return 
				
				# handle key press
				elif event.type == pygame.KEYDOWN:
					thread.handleKey(event)
				
				# timer expired
				elif event.type == pygame.USEREVENT:
					# get decision of player (human or AI)
					decision = thread.getDecision()
					# act on it
					if decision!=None : self.board.command(decision)
					# update the board
					loop = self.board.endTurn() != self.board.DEATH
					break
		
		
		
		# Game over!
		self.updateScreen()
		pygame.time.wait(1000)
	
	
	
	
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
	

		
	
	
	
	
	
	