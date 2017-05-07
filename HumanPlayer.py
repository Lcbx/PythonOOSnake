import main
import pygame
import direction

def play(event, board):
	# default used if timer expired
	result = board.snake.direction
	# key pressed
	if event.type == pygame.KEYDOWN: 
		if event.key == pygame.K_LEFT:
			result = direction.left()
		elif event.key == pygame.K_RIGHT:
			result = direction.right()
		elif event.key == pygame.K_DOWN:
			result = direction.down()
		elif event.key == pygame.K_UP:
			result = direction.up()
	return result

main.play = play
application = main.Game()
application.run()