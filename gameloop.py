#import sys
import pygame
import direction
import board
#from threading import Thread


import debug

		

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
		self.timeStep = 250 # milliseconds per step
		pygame.time.set_timer(pygame.USEREVENT, self.timeStep)
	
	
	def run(self):
		
		# the player
		player = getPlayer(self.timeStep)
		
		loop = True
		while loop:
			
			# draw calls
			self.updateScreen()
			
			# thread to let the AIs begin computations
			player.think(self.board)
			
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
					player.handleKey(event)
				
				# timer expired
				elif event.type == pygame.USEREVENT:
					# get decision of player (human or AI)
					decision = player.getDecision()
					# act on it
					if decision!=None : self.board.command(decision)
					# update the board
					loop = self.board.endTurn() != self.board.DEATH
					break
		
		
		
		# Game over!
		self.updateScreen()
		pygame.time.wait(1500)
	
	
	
	
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
		self.drawRect(self.board.food.color, x, y )
	
	def drawSnake(self):
		color = ()
		length = len(self.board.snake.body)
		for i in range(0, length):
			if( i == 0 ): color = self.board.snake.headColor
			else:
				r, g, b = self.board.snake.color
				factor = (float(length - i) / length) * 0.7 + 0.3 # min 0.3, max 1, linear between
				color = int(r  * factor), int(g * factor), int(b * factor)
			(x, y) = self.board.snake.body[i]
			self.drawRect(color, x, y)
	

		
	
	
	
	
	
	