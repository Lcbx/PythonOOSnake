import gameloop
import random
import direction

import debug

from inliner import inline

# depth of investigation
DEPTH = 5

# width of investigation
WIDTH = 50

# value at which we drop investigation (death)
CUTOFF = -100

	
class TreePlayer:
	
	def __init__(self, timeStep):
		self.done = False
		#TODO: adapt DEPTH and WIDTH to timeStep
		
		# paths under investiagtion
		self.paths = {}
	
	def think(self, board):
		
		self.paths.clear()
		
		for decision in direction.ALL:
			
			decisionValue, newBoard = board.potentialEndturn(decision)
			
			debug.say(str(decision) +" : " + str(decisionValue))
			
			#if decisionValue > CUTOFF:
			for _ in xrange(WIDTH):
				testBoard  = newBoard.clone()
				for _ in xrange(DEPTH-1):
					possibility = random.choice(direction.ALL)
					value = testBoard.endTurnDecision(possibility)
					decisionValue += value
					#debug.say("investigate " + str(possibility) + " : " + str(value) + " -> " + str(decisionValue))
					#if value <= CUTOFF: break
				#decisionValue= float(decisionValue) / float(WIDTH)
			
			self.paths[decision] = decisionValue +  random.randint(0, 3) # randomize so at equal score different decision can be taken
			#debug.say("value : " + str(decisionValue) + " -> " + str(self.paths[decision]))
	
	def handleKey(self, event):
		pass
		
	def getDecision(self):
		self.done = True
		self.decision = None
		if self.paths:
			list = sorted(self.paths, key = self.paths.get)
			self.decision = list[-1]
		for test in self.paths.values():
			debug.say("end : " + str(test))
		debug.say("chosen : " + str(self.decision))
		return self.decision

def getPlayer(timeStep):
	return TreePlayer(timeStep)
	
	
gameloop.getPlayer = getPlayer
application = gameloop.Game()
application.run()
	
	
	
	
	
