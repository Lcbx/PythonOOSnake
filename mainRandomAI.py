import gameloop
import random
import direction

import debug


class RandomPlayer:
	
	def __init__(self, timeStep):
		self.decision = None
		self.paths = []
	
	def think(self, board):
		self.decision = None
		self.paths = []
		# if a snack is close gobble it
		for possibility in direction.ALL:
			result = board.potentialEndturnResult(possibility)
			if result == board.SNACK:
				self.decision = possibility
				return
			# check if there is no issue
			elif result == board.DEATH:
				pass
			# added to possible paths 
			else: self.paths.append(possibility)
		
		# random choice in remaining options 
		if self.paths : self.decision = random.choice(self.paths)

	def handleKey(self, event):
		pass
		
	def getDecision(self):
		return self.decision

def getPlayer(timeStep):
	return RandomPlayer(timeStep)
	
	
gameloop.getPlayer = getPlayer
application = gameloop.Game()
application.run()