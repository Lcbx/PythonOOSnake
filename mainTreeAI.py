import gameloop
import random
import direction

import debug

DEPTH = 4

paths = {}

def expand(decision, depth, weight, board):
	#debug.say(paths.values())
	if depth == 0:
		if paths[decision] < weight :
			paths[decision] = weight
		return
	for probe in direction.ALL:
		addedWeight, newBoard = board.nextState(probe)
		newWeight = weight + addedWeight
		expand(decision, depth-1, newWeight, newBoard)

def findBestMove(board):
	paths.clear()
	#debug.say(paths.values())
	for decision in direction.ALL:
		paths[decision] = -200
		weight, newBoard = board.nextState(decision)
		expand(decision, DEPTH-1, weight, newBoard)
	
	#sorted(paths.items(), key=paths.get)
	priorityList = sorted(paths, key=paths.get)
	
	decision1 = priorityList[-1]
	decision2 = priorityList[-1]
	if(paths[decision1] == paths[decision2]):
		return decision2
	#debug.say(paths.values())
	#debug.say("best move " + str(paths[decision])+ " " + str(decision))
	return decision1

def play(event, board):
	return findBestMove(board)

gameloop.play = play
application = gameloop.Game()
application.run()