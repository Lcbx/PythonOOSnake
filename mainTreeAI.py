import gameloop
import random
import direction

import debug

from inliner import inline

# depth of investigation
DEPTH = 4
		

def get(probe):
	return probe.weight

	
class TreePlayer:
	
	def __init__(self, board, timeStep):
		self.board = board
		self.decision = None
		
		#TODO: adapt DEPTH to timeStep
		
		# to avoid unnecessary computation
		self.done = False
		
		# possible immediate action
		self.paths = []
	
	def think(self):
		for i in xrange(DEPTH):
			pass
	
	
	def handleKey(self, event):
		pass
		
	def getDecision(self):
		self.done = True
		return self.decision

def getPlayer(board, timeStep):
	return TreePlayer(board, timeStep)
	
	
gameloop.getPlayer = getPlayer
application = gameloop.Game()
application.run()
	
	
	
	
	
