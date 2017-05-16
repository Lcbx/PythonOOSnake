import gameloop
import pygame
import direction

# Template instance of a player
class ProtoPlayer:
	
	# constructor : receives the gamestate and turn time
	def __init__(self, timeStep):
		self.timeStep = timeStep
	
	# the AI computations should go here
	def think(self, board):
		pass
	
	# to handle keyStrokes
	def handleKey(self, event):
		pass
	
	# returns the player's decision
	def getDecision(self):
		return None

def getPlayer(timeStep):
	return ProtoPlayer(timeStep)
	
	
gameloop.getPlayer = getPlayer
application = gameloop.Game()
application.run()