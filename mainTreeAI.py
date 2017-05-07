import gameloop
import random
import direction

import debug

from inliner import inline

# depth of investigation
DEPTH = 40
# threshold at which we expand only down a single random path
THRESHOLD = DEPTH-3

# dictionnary that associate a direction with a score
paths = {}

@inline
def commit(decision, weight, depth):
	if paths[decision] < weight :
		paths[decision] = weight
	#debug.say ("commiting a decision of value " + str(weight) + " and depth " + str(depth))

@inline
def _expand(decision, probe, depth, weight, board):
	addedWeight, newBoard = board.nextState(probe)
	newWeight = weight + addedWeight
	expand(decision, depth-1, newWeight, newBoard)
		
		
def expand(decision, depth, weight, board):
	#debug.say(paths.values())
	commit(decision, weight, depth)
	if depth == 0 or weight < board.DEATH: return
	elif depth > THRESHOLD :
		for probe in direction.ALL:
			_expand(decision, probe,  depth, weight, board)
	else :
		#probe = random.choice(direction.ALL)
		probe = decision
		_expand(decision, probe, depth, weight, board)
	
def findBestMove(board):
	paths.clear()
	#debug.say(paths.values())
	for decision in direction.ALL:
		paths[decision] = board.DEATH
		weight, newBoard = board.nextState(decision)
		expand(decision, DEPTH-1, weight, newBoard)
	
	#sorted(paths.items(), key=paths.get)
	priorityList = sorted(paths, key=paths.get)
	
	decision = priorityList[-1]
	
	#debug.say(paths.values())
	#debug.say("best move " + str(paths[decision])+ " " + str(decision))
	
	#decision2 = priorityList[-2]
	#if(paths[decision] == paths[decision2]): decision = decision2
	
	return decision

def play(event, board):
	return findBestMove(board)

gameloop.play = play
application = gameloop.Game()
application.run()