import gameloop
import pygame
import direction

import random
import debug


#seed = random.randint(0, 1<<32 -1)
seedInt = 12
debug.say("seed : " + str(seedInt))
random.seed(seedInt)


WIDTH = 100

class Node:
	def __init__(self, value, board):
		self.value = float(value)
		self.board = board
		self.children = {}
		
	def _investigate(self, decision):
		if decision not in self.children :
			value, board = self.board.potentialEndturn(decision)
			child =  Node(value, board)
			self.children[decision] = child
			return (child, True) # a new Node was created
		return (self.children[decision], False) # found an existing Node
	
	def getValue(self):
		# mean of the children's value
		if(self.children):
			#debug.say(str(len(self.children)))
			value = 0.
			for child in self.children.values():
				value += child.getValue()
			value /= len(self.children) #direction.ALL) 
			value += self.value
			value /=2
			return value
		return self.value
	
	def investigate(self):
		depth = 0
		node = self
		path = []
		while True:
			depth += 1
			possibility = random.choice(direction.ALL)
			node, end = node._investigate(possibility)
			path.append(possibility)
			if end : break
		debug.say(" -> ".join(map(str, path)) + " : " + str(node.value))
		return node


class MCTSPlayer:
	
	# constructor : receives the gamestate and turn time
	def __init__(self, timeStep):
		self.timeStep = timeStep
		self.decision = None
	
	# the AI computations should go here
	def think(self, board):
		decision = None
		root = Node(0, board)
		
		debug.say("")
		
		for _ in xrange(WIDTH):
			root.investigate()
		
		if root.children:
			paths = {}
			for possibility, node in root.children.items():
				value = node.getValue()
				paths[possibility] = value
				debug.say(str(possibility) + " : " + str(value))
			list = sorted(paths, key = paths.get)
			decision = list[-1]
			
		debug.say("chosen : " + str(decision))
		self.decision =  decision
	
	# to handle keyStrokes
	def handleKey(self, event):
		pass
	
	# returns the player's decision
	def getDecision(self):
		return self.decision

def getPlayer(timeStep):
	return MCTSPlayer(timeStep)
	
	
gameloop.getPlayer = getPlayer
application = gameloop.Game()
application.run()