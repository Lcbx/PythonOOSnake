import main
import pygame
import direction

def play(event, board):
	# default used if timer expired
	decision = board.snake.direction
	# key pressed
	if event.type == pygame.KEYDOWN: 
		if event.key == pygame.K_LEFT:
			decision = direction.left()
		elif event.key == pygame.K_RIGHT:
			decision = direction.right()
		elif event.key == pygame.K_DOWN:
			decision = direction.down()
		elif event.key == pygame.K_UP:
			decision = direction.up()
	return decision

main.play = play
application = main.Game()
application.run()
