import gameloop
import random
import direction

import debug

DEPTH = 3

class Node:
	
	paths = []
	
	def __init__(self, parent, decision, weight):
		self.parent = parent
		self.decision = decision
		self.weight = weight
	
	def expand(self, depth, board):
		for decision in direction.ALL:
			result, clone = board.nextState(decision)
			child = Node(self, decision, self.weight + result)
			if(depth != 0): child.expand(depth-1, clone)
			else: self.paths.append(child)
	
def cmp(obj):
	return obj.weight

def findBestMove(board):
	Node.paths = []
	root = Node(None, None, 0)
	root.expand(DEPTH, board)
	Node.paths.sort(key=cmp)
	iterator = Node.paths[-1]
	while iterator.parent != root:
		iterator = iterator.parent
	debug.say("best move " + str(iterator.weight))
	return iterator.decision

def play(event, board):
	return findBestMove(board)

gameloop.play = play
application = gameloop.Game()
application.run()