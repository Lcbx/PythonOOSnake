import gameloop
import random
import direction
import math

import debug

from inliner import inline

# depth of investigation
DEPTH = 5

# width of investigation
WIDTH = 100

# value at which we drop investigation (death)
CUTOFF = -100

# set random seed for deterministic outcome
random.seed(15) #12)

	
class TreePlayer:
	
	def __init__(self, timeStep):
		#TODO: adapt DEPTH and WIDTH to timeStep
		
		# paths under investiagtion
		self.paths = {}
	
	def think(self, board):
		
		self.paths.clear()
		
		for decision in direction.ALL:
			
			decisionValue, newBoard = board.potentialEndturn(decision)
			decisionValue *= WIDTH
			
			debug.say(str(decision) +" : " + str(decisionValue))
			
			#if decisionValue > CUTOFF:
			for _ in xrange(WIDTH):
				testBoard  = newBoard.clone()
				exp = 1
				for depth in range(1, DEPTH):
					exp *= len(direction.ALL)
					possibility = random.choice(direction.ALL)
					value = testBoard.endTurnDecision(possibility)
					addedValue = float(value) / float(exp)
					decisionValue += addedValue
					debug.say("it " + str(_) + ", depth " + str(depth) + " : val " + str(value) + ", addedVal " + str(addedValue) + ", decisionVal " + str(decisionValue))
					#debug.say("investigate " + str(possibility) + " : " + str(value) + " -> " + str(decisionValue))
					#if value <= CUTOFF: break
				#decisionValue= float(decisionValue) / float(WIDTH)
			
			self.paths[decision] = decisionValue #+  random.randint(0, 3) # randomize so at equal score different decision can be taken
			#debug.say("value : " + str(decisionValue) + " -> " + str(self.paths[decision]))
	
	def handleKey(self, event):
		pass
		
	def getDecision(self):
		self.decision = None
		if self.paths:
			#for i in xrange(len(self.paths)):
			#	debug.say("end : " + str(self.paths.keys()[i]) + " -> " +str(self.paths.values()[i]))
			list = sorted(self.paths, key = self.paths.get)
			self.decision = list[-1]
			
		debug.say("chosen : " + str(self.decision))
		return self.decision

def getPlayer(timeStep):
	return TreePlayer(timeStep)
	
	
gameloop.getPlayer = getPlayer
application = gameloop.Game()
application.run()
	
	
	
	
	
