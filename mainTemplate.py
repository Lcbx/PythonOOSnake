import gameloop
import pygame
import direction

# Template instance of a player
class ProtoPlayer:
	
	# constructor : receives the gamestate and turn time
	def __init__(self, board, timeStep):
		self.board = board
	
	# the AI computations should go here
	def think(self):
		pass
	
	# to handle keyStrokes
	def handleKey(self, event):
		pass
	
	# returns the player's decision
	def getDecision(self):
		return self.board.snake.direction

def getPlayer(board, timeStep):
	return ProtoPlayer(board, timeStep)
	
	
gameloop.getPlayer = getPlayer
application = gameloop.Game()
application.run()