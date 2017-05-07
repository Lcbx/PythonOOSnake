import main
import random
import direction

import debug

def play(event, board):
	# avoid infinite loop
	deathPaths = 0
	
	# if a snack is close gobble it
	for i in range(0, len(direction.ALL)):
		decision = direction.ALL[i]
		result = board.decisionResult(decision)
		if result == board.SNACK: return decision
		# check if there is no issue
		elif result == board.DEATH: deathPaths += 1
	
	debug.say(deathPaths)
	
	# die a brave death if no escape
	if deathPaths == len(direction.ALL): return random.choice(direction.ALL)
	
	# otherwise, happy go lucky
	while True:
		decision = random.choice(direction.ALL)
		if board.decisionResult(decision) != board.DEATH: return decision

main.play = play
application = main.Game()
application.run()