class Tile:
	def __init__(self):
		self.is_bomb = False
		self.adjacent_bombs = 9
		self.is_flagged = False
		self.is_covered = True
		
	def __str__(self):
		'''
		The retun string has 3 characters:
		1) Either the number of adjacent bombs or B for bomb.
		2) C for covered or c for uncovered.
		3) F for flagged or f for unflagged.
		'''
		
		return_string = 'B' if self.is_bomb else str(self.adjacent_bombs)
		return_string += 'C' if self.is_covered else 'c'
		return_string += 'F' if self.is_flagged else 'f'
		
		return return_string
			

if __name__ == "__main__":
	my_tile = Tile()
	print(my_tile)
	
	my_tiles = [str(my_tile), my_tile]
	print(my_tiles)

