import pygame

import strategies

class Cell:
	def __init__(self):
		self.val = None
		self.opts = [i for i in range(1,10)]
		
		self.SmallFont = pygame.font.SysFont("comicsansms", 15)
		self.BigFont = pygame.font.SysFont("comicsansms", 40)

	def pop(self, val):
		if val in self.opts: self.opts.remove(val)
	
	def draw(self, win, pos, dims):

		if self.val != None:
			txtval = self.BigFont.render(
				str(self.val),
				True,
				(0,0,0))
			win.blit(txtval, (
				pos[0] + dims[0]/2-txtval.get_width()/2,
				pos[1] + dims[1]/2-txtval.get_height()/2))
			
		else:
			for opt in self.opts:
				p = ((opt-1)%3)/3,((opt-1)//3)/3
				txt = self.SmallFont.render(
					str(opt),
					True,
					(0,0,0))
				win.blit(txt, (
					int(pos[0] + dims[0]/9 + p[0]*dims[0] + dims[0]/18-txt.get_width()/2),
					int(pos[1] + dims[1]/9 + p[1]*dims[1] + dims[1]/18-txt.get_height()/2)
				))


class Sudoku:
	def __init__(self):
		self.cells = [Cell() for i in range(81)]
		self.strats = [
			strategies.ForcedEntries
		]

	def getIndex(self, pos):
		return pos[0]-1+(pos[1]-1)*9
	def getPos(self, index):
		return index%9+1, index//9+1
	
	def updateSquare(self, val, pos):
		sq = (((pos[0]-1)//3)+1)*3-2, (((pos[1]-1)//3)+1)*3-2
		for i in range(3):
			for j in range(3):
				self.cells[self.getIndex((sq[0]+i, sq[1]+j))].pop(val)
			
	def updateRow(self, val, pos):
		for i in range(9):
			self.cells[self.getIndex((i+1, pos[1]))].pop(val)
	
	def updateColumn(self, val, pos):
		for i in range(9):
			self.cells[self.getIndex((pos[0], i+1))].pop(val)
	
	def set(self, val, pos):
		self.cells[self.getIndex(pos)].val = val
		self.updateSquare(val, pos)
		self.updateRow(val, pos)
		self.updateColumn(val, pos)

	
	def draw(self, win, pos, dims):
		for i in range(9):
			for j in range(9):
				pygame.draw.rect(win, (0,0,0), ((pos[0]+i*dims[0]/9,pos[1]+j*dims[1]/9),(dims[0]/9,dims[1]/9)), True)
		for i in range(3):
			for j in range(3):
				pygame.draw.rect(win, (0,0,0), ((pos[0]+i*dims[0]/3,pos[1]+j*dims[1]/3),(dims[0]/3,dims[1]/3)), True, 5)
				
		for i, cell in enumerate(self.cells):
			p = (i%9)/9,(i//9)/9
			cell.draw(win, (pos[0] + p[0]*dims[0], pos[1] + p[1]*dims[1]), (dims[0]/9, dims[1]/9))

	def isSolved(self):
		solved = True
		for cell in self.cells:
			if cell.val == None:
				solved = False
		return solved

	def fillCell(self):
		for strat in self.strats:
			filledCell = strat.fill(self)
			if filledCell >= 0:
				break
		if filledCell < 0:
			print("could not fill a cell")
			return False
		print(f"filled cell at {self.getPos(filledCell)}, using {strat.name}")
		return True