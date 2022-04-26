import pygame
import sudoku
pygame.init()

win = pygame.display.set_mode((500,500))

def main():
	Sudoku = sudoku.Sudoku()
	Sudoku.set(3,(1,1))
	Sudoku.set(6,(3,1))
	Sudoku.set(5,(4,1))
	Sudoku.set(8,(6,1))
	Sudoku.set(4,(7,1))
	Sudoku.set(5,(1,2))
	Sudoku.set(2,(2,2))
	Sudoku.set(8,(2,3))
	Sudoku.set(7,(3,3))
	Sudoku.set(3,(8,3))
	Sudoku.set(1,(9,3))
	Sudoku.set(3,(3,4))
	Sudoku.set(1,(5,4))
	Sudoku.set(8,(8,4))
	Sudoku.set(9,(1,5))
	Sudoku.set(8,(4,5))
	Sudoku.set(6,(5,5))
	Sudoku.set(3,(6,5))
	Sudoku.set(5,(9,5))
	Sudoku.set(5,(2,6))
	Sudoku.set(9,(5,6))
	Sudoku.set(6,(7,6))
	Sudoku.set(1,(1,7))
	Sudoku.set(3,(2,7))
	Sudoku.set(2,(7,7))
	Sudoku.set(5,(8,7))
	Sudoku.set(7,(8,8))
	Sudoku.set(4,(9,8))
	Sudoku.set(5,(3,9))
	Sudoku.set(2,(4,9))
	Sudoku.set(6,(6,9))
	Sudoku.set(3,(7,9))

	clock = pygame.time.Clock()
	FPS = 1
	run = True
	while run:
		clock.tick(FPS)
		win.fill((255,255,255))
		
		Sudoku.draw(win, (10,10), (480,480))

		pygame.display.update()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				Sudoku.fillCell()

main()