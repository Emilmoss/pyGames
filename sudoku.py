#run in python 2

import argparse
from Tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

BOARDS = ['debug','n00b','l33t','error'] #Available sudoku boards
MARGIN = 20 #Pixels around the board
SIDE = 50 #Width of every board cell
WIDTH = HEIGHT = MARGIN * 2 * SIDE * 9 #Width and height of the whole board

class SudokuError(Exception):
	"""
	An application specific error.
	"""
	pass

class SudokuBoard(object):
	"""
	Sudoku Board representation
	"""
	def __init__(self, board_file):
		self.board = self.__create_board(board_file)

	def __create_board(self, board_file):
		# create an initial matrix
		board = []

		# iterate over each line
		for line in board_file:
			line = line.strip()


			#raise an error if line is longer or shorter than 9 characters
			if len(line) != 9:
				board = []
				raise SudokuError(
					"Each line in the sudoku puzzle must be 9 chars long.")

			# create a list for the line
			board.append([])	

			#then iterate over each character
			for c in line:
				# Raise an error if the character is not an integer
				if not c.isdigit():
					raise SudokuError("Valid characters for sudoku puzzle must be in 0-9")

				# Add to the latest list for the line
				board[-1].append(int(c))

		# Riase an error if there are not 9 lines
		if len(board) != 9:
			raise SudokuError("Each sudoku puzzle must be 9 lines long")

		# Return the constructed board
		return board 



test = SudokuBoard()





