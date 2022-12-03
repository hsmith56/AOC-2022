import random, math, string

def load():
	with open('day03/day03Input.txt') as file:
		data = file.readlines()
		d = [line.strip() for line in data]
	return d

inpt = load()
def part1(inpt):
	score = 0
	for x in inpt:
		left, right = x[0:int(len(x)/2)], x[int(len(x)/2)::]
		same = set(left) & set(right)
		leftover = list(same)[0]
		if leftover in string.ascii_lowercase:
			score += ord(leftover)-96
		else:
			score += ord(leftover)-38
	return score

def part2(inpt):
	score = 0
	for x in range(0, len(inpt), 3):
		x,y,z = inpt[x:x+3]
		same = set(x) & set(y) & set (z)
		leftover = list(same)[0]
		if leftover in string.ascii_lowercase:
			score += ord(leftover)-96
		else:
			score += ord(leftover)-38
	return score

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')