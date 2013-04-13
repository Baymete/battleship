from random import randrange

board = []

aircraft_carrier = 5
battleship = 4
submarine = 3
destroyer = 3
patrol_boat = 2

ships = [aircraft_carrier, battleship, submarine, destroyer, patrol_boat]

def GetShipCoordinates(ship):
	vertical = randrange(2)
	if vertical:
		rand_row = randrange(10-ship)
		rand_col = randrange(10)
	else:
		rand_row = randrange(10)
		rand_col = randrange(10-ship)
	return ship, rand_row, rand_col, vertical

def PrintBoard(board):
	for i in board:
		print i

def ShipOverlaps(ship, board):
	ship, row, col, vertical = ship
	try:
		if vertical:
			for s in range(ship):
				if board[row+s][col] == "S":
					break
			else:
				return True
			return False
		else:
			for s in range(ship):
				if board[row][col+s] == "S":
					break
			else:
				return True
			return False
	except IndexError:
		PrintBoard(board)
		print "Row %s Col %s Vertical %s" %(row, col, vertical)


def PositionShip(ship, board):
	ship, row, col, vertical = ship
	print "Positioning ship %s" %ship
	if vertical:
		for i in range(ship):
			print "Updating %s %s" %(row+i,col)
			board[row+i][col] = "S"
	else:
		for i in range(ship):
			print "Updating %s %s" %(row,col+i)
			board[row][col+i] = "S"
	print "---------------"

def MakeBoard():
	global board
	board = []
	for i in range(1,11):
		board.append(["O"]*10)
	for s in ships:
		ship = GetShipCoordinates(s)
		while not ShipOverlaps(ship, board):
			print "Ship overlapped"
			ship = GetShipCoordinates(s)
		PositionShip(ship,board)

def Do():
	MakeBoard()
	PrintBoard(board)
