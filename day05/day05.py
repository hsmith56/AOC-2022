import random, math

def load():
	with open('day05/day05Input.txt') as file:
		data = file.readlines()
		d = [line.rstrip() for line in data]
	return d

inpt = load()
def part1(inpt):
	board = []
	columns = {}
	moves = 0

	# look through the input and seperate the moves from the stacks
	for x, y in enumerate(inpt):
		if y.replace(" ", "").isdecimal():
			moves = x + 2
			break
		row = []
		for i in range(1, len(y), 4):
			if y[i].isalpha():
				row.append(y[i])
			else:
				row.append('_')
		board.append(row)
	board_len = max([len(x) for x in board])
	for row in board:
		if len(row) != board_len:
			row += (['_'] * (board_len - len(row)))

	for x, y in enumerate(board):
		for i in range(len(y)):
			try:
				columns[i].append(board[x][i])
			except:
				columns[i] = [board[x][i]]
	for column in columns:
		columns[column] = [x for x in columns[column] if x != '_']

	for x in inpt[moves::]:
		number, start, end = int(x.split(" ")[1]), int(x.split(" ")[3])-1, int(x.split(" ")[5])-1
		while number != 0:
			top = columns[start].pop(0)
			columns[end].insert(0, top)
			number -= 1

	ans = ""
	for x in columns:
		ans += columns[x][0]
	return ans

def part2(inpt):
	board = []
	columns = {}
	moves = 0
	for x, y in enumerate(inpt):
		if y.replace(" ", "").isdecimal():
			moves = x + 2
			break
		row = []
		for i in range(1, len(y), 4):
			if y[i].isalpha():
				row.append(y[i])
			else:
				row.append('_')
		board.append(row)
	board_len = max([len(x) for x in board])
	for row in board:
		if len(row) != board_len:
			row += (['_'] * (board_len - len(row)))

	for x, y in enumerate(board):
		for i in range(len(y)):
			try:
				columns[i].append(board[x][i])
			except:
				columns[i] = [board[x][i]]
	for column in columns:
		columns[column] = [x for x in columns[column] if x != '_']

	for x in inpt[moves::]:
		number, start, end = int(x.split(" ")[1]), int(x.split(" ")[3])-1, int(x.split(" ")[5])-1
		top = columns[start][0:number]
		del columns[start][0:number]
		columns[end] = top + columns[end]
		number -= 1

	ans = ""
	for x in columns:
		ans += columns[x][0]
	return ans

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')