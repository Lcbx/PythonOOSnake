import gameloop
import pygame
import direction

import debug

decision = None

def startTurn(board):
	pass

def handleKey(event):
	global decision
	if event.key == pygame.K_LEFT:
		decision = direction.left()
	elif event.key == pygame.K_RIGHT:
		decision = direction.right()
	elif event.key == pygame.K_DOWN:
		decision = direction.down()
	elif event.key == pygame.K_UP:
		decision = direction.up()
	
def play():
	return decision

gameloop.startTurn = startTurn
gameloop.handleKey = handleKey
gameloop.play = play
application = gameloop.Game()
application.run()
