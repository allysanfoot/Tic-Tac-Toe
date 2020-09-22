test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
import random

def display_board(board):
	print(board[1:4])
	print(board[4:7])
	print(board[7:])

def player_input():

	player1_marker = 'INVALID'
	player2_marker = 'INVALID'
	valid_marker = ['X', 'O']

	while player1_marker not in valid_marker:
		player1_marker = input("Player 1: Please choose a marker (X or O): ").upper()

		if player1_marker not in valid_marker:
			print("Please enter a valid response.")

	if player1_marker == 'X':
		player2_marker == 'O'
	else:
		player2_marker == 'X'

	print(f"Player 1's marker is: {player1_marker}")
	print(f"Player 2's marker is: {player2_marker}")

	return ['#', player1_marker, player2_marker]

def place_marker(board, marker, position):

	board[position] = marker

	return board

def win_check(board, mark):

	return ((mark == board[1] == board[2] == board[3]) or
		(mark == board[4] == board[5] == board[6]) or
		(mark == board[7] == board[8] == board[9]) or
		(mark == board[1] == board[4] == board[7]) or
		(mark == board[2] == board[5] == board[8]) or
		(mark == board[3] == board[6] == board[9]) or
		(mark == board[7] == board[5] == board[3]) or
		(mark == board[1] == board[5] == board[9]))

def choose_first():
	players = ['#', 'Player 1', 'Player 2']

	goes_first = random.randint(1, 2)

	if goes_first == 1:
		print(f'{players[1]} goes first!')
	else:
		print(f'{players[2]} goes first!')

	return goes_first

def space_check(board, position):

	return board[position] == ' '

def full_board_check(board):

	marker_values ['#', 'X', 'O']

	for i in range(len(board)):
		if board[i] not in marker_values:
			return False
	return True

def player_choice(board):
	position_choice = 'INVALID'
	valid_position_range = range(1, 10)
	within_range = False
	position_available = False

	while position_choice.isdigit() == False or within_range == False or position_available == False:

		position_choice = input("Please enter the choice for your next move (1-9): ")

		if position_choice.isdigit() == False:
			print("Please enter an integer for your answer")

		if position_choice.isdigit() == True:
			if int(position_choice) in valid_position_range:
				within_range = True
			else:
				print("Please choose a number that is within the range of 1 and 9.")

		if position_available == False:
			if space_check(board ,int(position_choice)):
				position_available = True
			else:
				print("Please choose a free spot on the board.")

	return int(position_choice)

def replay():

	answer = 'INVALID'
	valid_answers = ['Y', 'N']

	while not in valid_answers:
		answer = input("Do you want to keep playing? Yes(Y) or No(N)").upper()

		if answer not in valid_answers:
			print("Please enter a valid response.")

	if answer == 'Y':
		return True
	else:
		return False