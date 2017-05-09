import gameloop
import pygame
import direction

import debug


class HumanPlayer:
	
	def __init__(self, board, timeStep):
		self.board = board
		self.decision = None
	
	def think(self):
		pass
	
	def handleKey(self, event):
		if event.key == pygame.K_LEFT:
			self.decision = direction.left()
		elif event.key == pygame.K_RIGHT:
			self.decision = direction.right()
		elif event.key == pygame.K_DOWN:
			self.decision = direction.down()
		elif event.key == pygame.K_UP:
			self.decision = direction.up()
		
	def getDecision(self):
		return self.decision

def getPlayer(board, timeStep):
	return HumanPlayer(board, timeStep)
	
	
gameloop.getPlayer = getPlayer
application = gameloop.Game()
application.run()
