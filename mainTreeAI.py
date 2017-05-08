import gameloop
import random
import direction

import debug

from inliner import inline
import time

# depth of investigation
DEPTH = 40

# threshold at which we expand only down a single random path
THRESHOLD = DEPTH-2

# dictionnary that associate a direction with a score
paths = {}

# signal to stop computation
done = False

@inline
def commit(decision, weight, depth):
	if paths[decision] and paths[decision] < weight :
		paths[decision] = weight
	#debug.say ("commiting a decision of value " + str(weight) + " and depth " + str(depth))

@inline
def _expand(decision, probe, depth, weight, board):
	if(done): return
	addedWeight, newBoard = board.potentialEndturn(probe)
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
		
		
		
		
def startTurn(board):
	paths.clear()
	
	global done
	done = False
	
	#debug.say(paths)
	
	for decision in direction.ALL:
		paths[decision] = board.DEATH
		weight, newBoard = board.potentialEndturn(decision)
		expand(decision, DEPTH-1, weight, newBoard)

def handleKey(event):
	pass
	
def play():
	
	global done
	done = True
	
	time.sleep(0.001)
	
	decision = None
	
	# sort moves by worth
	priorityList = sorted(paths, key=paths.get)
	
	#get the best
	if priorityList: decision = priorityList[-1]
	
	#debug.say(paths.values())
	#debug.say(priorityList)
	#debug.say(paths)
	#debug.say("best move " + str(paths[decision])+ " " + str(decision))
	
	return decision

gameloop.startTurn = startTurn
gameloop.handleKey = handleKey
gameloop.play = play
application = gameloop.Game()
application.run()
	
	
	
	
	
