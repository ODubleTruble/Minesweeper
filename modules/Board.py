import random
try:
    from Tile import Tile
except ImportError:
    from modules.Tile import Tile



class TooManyBombsError(Exception):
	def __init__(self):
		self.message = "The number of bombs is greater than the number of tiles"
		super().__init__(self.message)


class Board:
	def __init__(self, rows, columns, num_bombs):
		if num_bombs > rows * columns: raise TooManyBombsError()
		
		self.grid = [[Tile() for _ in range(columns)] for _ in range (rows)]
		self.ROWS = rows
		self.COLUMNS = columns
		self.NUM_BOMBS = num_bombs
		
		self.generate_bombs()
		self.calc_adjacent_bombs()
		
		
	def generate_bombs(self):
		bomb_locations = set()
		
		while len(bomb_locations) < self.NUM_BOMBS:
			row = random.randint(0, self.ROWS-1)
			col = random.randint(0, self.COLUMNS-1)
			bomb_locations.add((row, col))
		
		for bomb_location in bomb_locations:
			row = bomb_location[0]
			col = bomb_location[1]
			self.set_bomb(row, col)
			
	
	def calc_adjacent_bombs(self):
		for this_row in range(self.ROWS):
			for this_col in range(self.COLUMNS):
				# This loop runs for every tile on the board once.
				
				this_tile = self.get_tile(this_row, this_col)
				
				adjacent_bombs = 0
				
				min_test_row = max(this_row - 1, 0)
				max_test_row = min(this_row + 1, self.ROWS-1)
				min_test_col = max(this_col - 1, 0)
				max_test_col = min(this_col + 1, self.COLUMNS-1)
				
				for test_row in range(min_test_row, max_test_row+1):
					for test_col in range(min_test_col, max_test_col+1):
						# This loop runs for all of the adjacent tiles.
						
						test_tile = self.get_tile(test_row, test_col)
						if test_tile.is_bomb:
							adjacent_bombs += 1
				
				this_tile.adjacent_bombs = adjacent_bombs
	
	
	def __str__(self):
		return_string = 'Minesweeper Board:\n'
		return_string += f'{self.ROWS} rows, '
		return_string += f'{self.COLUMNS} columns, '
		return_string += f'{self.NUM_BOMBS} bombs\n'
		
		for row_num in range(self.ROWS):
			this_row_str = ''
			
			for col_num in range(self.COLUMNS):
				tile = self.get_tile(row_num, col_num)
				this_row_str += str(tile)
				this_row_str += ' '
				
			return_string += this_row_str + '\n'
			
		return return_string
		
		
	def get_tile(self, row, col):
		return self.grid[row][col]
		
	
	def set_bomb(self, row, col):
		self.grid[row][col].is_bomb = True
		
	
	def set_flagged(self, row, col):
		self.grid[row][col].is_flagged = True
		
	
	def set_unflagged(self, row, col):
		self.grid[row][col].is_flagged = False
		
	
	def set_uncovered(self, row, col):
		self.grid[row][col].is_covered = False
		
	
	def set_adjacent_bombs(self, row, col, amount):
		self.grid[row][col].adjacent_bombs = amount


if __name__ == "__main__":
	my_board = Board(9, 9, 10)
	print(my_board)
	

