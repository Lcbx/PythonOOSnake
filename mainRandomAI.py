import gameloop
import random
import direction

import debug


class RandomPlayer:
	
	def __init__(self, board, timeStep):
		self.board = board
		self.decision = None
		self.paths = []
	
	def think(self):
		self.decision = None
		self.paths = []
		# if a snack is close gobble it
		for possibility in direction.ALL:
			result = self.board.potentialEndturnResult(possibility)
			if result == self.board.SNACK:
				self.decision = possibility
				return
			# check if there is no issue
			elif result == self.board.DEATH:
				pass
			# added to possible paths 
			else: self.paths.append(possibility)
		
		# random choice in remaining options 
		if self.paths : self.decision = random.choice(self.paths)

	def handleKey(self, event):
		pass
		
	def getDecision(self):
		return self.decision

def getPlayer(board, timeStep):
	return RandomPlayer(board, timeStep)
	
	
gameloop.getPlayer = getPlayer
application = gameloop.Game()
application.run()