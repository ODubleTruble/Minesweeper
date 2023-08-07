from enum import Enum

class Game_State(Enum):
	WAITING_FOR_START = 0
	PLAYING = 1
	LOST = 2
	WON = 3
	

if __name__ == "__main__":
	'''
	If there's only one usage of the Enum, then the variable that uses it can just
	be called the Enum's name but in lower_snake_case rather than Upper_Snake_Case. 
	For Example: A variable that stores the Game_State Enum being called game_state.
	'''
	
	game_state = Game_State.PLAYING
	print(f'game_state = {game_state}')
	print(f'game_state.name = {game_state.name}')
	print(f'game_state.value = {game_state.value}')
	
