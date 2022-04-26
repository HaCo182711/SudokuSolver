class Fill:
	name = "Fill"
	def fill(sudoku):
		return False

class ForcedEntries(Fill):
	name = "ForcedEntries"
	def fill(sudoku):
		for i, cell in enumerate(sudoku.cells):
			if cell.val == None and len(cell.opts) == 1:
				sudoku.set(cell.opts[0], sudoku.getPos(i))
				return i
		return -1


class Eliminate:
	name = "Eliminate"
	def eliminate(sudoku):
		return False