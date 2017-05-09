import gameloop
import random
import direction

import debug

from inliner import inline

# depth of investigation
DEPTH = 20

# threshold at which we expand only down a single random path
THRESHOLD = DEPTH-3

# new way of investigation, use it in next version
class Probe:
	def __init__(self, decision):
		self.decision = decision
		self.weight = 0
	
	@inline
	def testPossibility(self, board, possibility, currentWeight):
		result, newBoard = board.potentialEndturn(possibility)
		newWeight = currentWeight + result
		if newWeight < self.weight : self.weight = newWeight
		return (newWeight, newBoard)
	
	@inline
	def _expand(self, board, currentWeight, depth):
		for possibility in direction.ALL:
			newWeight, newBoard = testPossibility(possibility)
			if depth == 0 or newWeight < board.DEATH: return
			self._expand(newBoard, newWeight, depth-1)
	
	def expand(self, board):
		newWeight, newBoard = testPossibility(board, self.decision, 0)
		self._expand(newBoard, newWeight, DEPTH)


		
	
class TreePlayer:
	
	def __init__(self, board, timeStep):
		self.board = board
		#TODO: adapt DEPTH and THRESHOLD to timeStep
		
		# to avoid unnecessary computation
		self.done = False
		
		# dictionnary that associate a direction with a score
		self.paths = {}
	
	
	def think(self):
		for decision in direction.ALL:
			self.paths[decision] = self.board.DEATH
			weight, newBoard = self.board.potentialEndturn(decision)
			self.expand(decision, DEPTH-1, weight, newBoard)
		
		
	@inline
	def commit(self, decision, weight, depth):
		if self.paths[decision] and self.paths[decision] < weight :
			self.paths[decision] = weight
		#debug.say ("commiting a decision of value " + str(weight) + " and depth " + str(depth))

	@inline
	def _expand(self, decision, probe, depth, weight, board):
		if(self.done): return
		addedWeight, newBoard = board.potentialEndturn(probe)
		newWeight = weight + addedWeight
		self.expand(decision, depth-1, newWeight, newBoard)
	
	def expand(self, decision, depth, weight, board):
		#debug.say(paths.values())
		self.commit(decision, weight, depth)
		if depth == 0 or weight < board.DEATH: return
		elif depth > THRESHOLD :
			for probe in direction.ALL:
				self._expand(decision, probe,  depth, weight, board)
		else :
			probe = random.choice(direction.ALL)
			#probe = decision
			self._expand(decision, probe, depth, weight, board)
	
	
	def handleKey(self, event):
		pass
		
	def getDecision(self):
		decision = None
		
		# sort moves by worth
		priorityList = sorted(self.paths, key=self.paths.get)
		
		#get the best
		if priorityList:
			decision = priorityList[-1]
			same = []
			for possibility in priorityList :
				if self.paths[decision] == self.paths[possibility] :
					same.append(possibility)
			if len(same)>=2 :
				decision = random.choice(same)
		
		#debug.say(paths.values())
		#debug.say(priorityList)
		#debug.say(paths)
		#debug.say("best move " + str(paths[decision])+ " " + str(decision))
		
		return decision

def getPlayer(board, timeStep):
	return TreePlayer(board, timeStep)
	
	
gameloop.getPlayer = getPlayer
application = gameloop.Game()
application.run()
	
	
	
	
	
