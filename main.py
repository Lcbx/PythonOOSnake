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
		self.timeStep = 200 # milliseconds per step
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
		while True:
			event = pygame.event.wait()

			if event.type == pygame.QUIT: # window closed
				pygame.quit()
				return #sys.quit(0)

			if event.type == pygame.USEREVENT: # timer elapsed
				res = self.board.update()
				if res == self.board.DEATH: break
			
			self.updateScreen()
			
			#case of a human player
			if event.type == pygame.KEYDOWN: # key pressed
				if event.key == pygame.K_LEFT:
					input = direction.left()
				elif event.key == pygame.K_RIGHT:
					input = direction.right()
				elif event.key == pygame.K_DOWN:
					input = direction.down()
				elif event.key == pygame.K_UP:
					input = direction.up()
				self.board.command(input)
			
			#case of AI
			#TODO: call the AI
				
		# Game over!
		for i in range(0, 10):
			self.updateScreen()
			pygame.time.wait(100)
			

application = Game()
application.run()