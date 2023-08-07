import pygame, sys
from pygame.locals import *

from modules.Board import Board
from modules.Image import Image


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


def init():
    # The number of rows, or height of the board.
    ROWS = 9
    # The number of columns, or width of the board.
    COLUMNS = 9
    # The number of bombs.
    BOMBS = 10
    
    my_board = Board(ROWS, COLUMNS, BOMBS)
    print(my_board)


def update(dt):
    '''
    This function is called every frame.
    Handles all of the logic and updates all of the variables.
    '''
    
    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1: # Left mouse button.
                print(event.pos)


def draw(screen):
    '''
    This function is called every frame.
    Draws everything on the screen and updates the display.
    '''
    
    # Clears everything on the screen by making it black. 
    screen.fill((192,192,192))
    
    Image.tile_size = 100
    screen.blit(Image.mine(), (0,0))
    screen.blit(Image.number(1), (100,0))

    # Updates the display. 
    pygame.display.update()


def runPyGame():
    init()
    
    pygame.init()
    
    FPS = 120
    fpsClock = pygame.time.Clock()
    
    desktop_size = pygame.display.get_desktop_sizes()[0]
    WINDOW_SIZE = (desktop_size[0]/1.5, desktop_size[1]/1.5)
    screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
    pygame.display.set_caption('Minesweeper')

    # The time since the last frame.
    dt = 0
    
    # The main game loop.
    while True:
        update(dt)
        draw(screen)

        # dt is time since the last frame.
        # Pauses the program to create the correct FPS. 
        dt = fpsClock.tick(FPS)


if __name__ == '__main__':
    runPyGame()