import gameloop
import random
import direction

import debug

decision = None

def startTurn(board):
	
	global decision
	
	# available paths
	paths = []
	
	# if a snack is close gobble it
	for i in range(0, len(direction.ALL)):
		decision = direction.ALL[i]
		result = board.potentialEndturnResult(decision)
		if result == board.SNACK:
			return
		# check if there is no issue
		elif result == board.DEATH:
			pass
		# added to possible paths 
		else: paths.append(decision)
		
	# random choice in remaining options 
	if paths : decision = random.choice(paths)

def handleKey(event):
	pass
	
def play():
	return decision

gameloop.startTurn = startTurn
gameloop.handleKey = handleKey
gameloop.play = play
application = gameloop.Game()
application.run()
