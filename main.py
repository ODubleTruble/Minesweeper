from modules.Board import Board

# The number of rows, or height of the board.
ROWS = 9
# The number of columns, or width of the board.
COLUMNS = 9
# The number of bombs.
BOMBS = 10


my_board = Board(ROWS, COLUMNS, BOMBS)

print(my_board)

'''
TODO:
1) Make a way to display the board and interact with the tiles.
2) Make a way to expose a tile, which exposes nearby tiles if the tile has no adjacent bombs.
3) Make it so that the first tile clicked is never a bomb.
4) Add chording.
5) Change flagging to be a toggle.
6) Add functionaily for the Game_State Enum.
7) Create presets for the board size and number of bombs.
'''
