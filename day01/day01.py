import random, math

def load():
	with open('day01/day01Input.txt') as file:
		data = file.readlines()
		d = [line.strip() for line in data]
	return d

inpt = load()
def part1(inpt):
	prev_max = 0
	curr_max = 0
	for i in inpt:
		if i:
			curr_max += int(i)
		else:
			prev_max = max(curr_max, prev_max)
			curr_max = 0

	return prev_max

def part2(inpt):
	prev_max = 0
	curr_max = 0
	maxes = []
	for i in inpt:
		if i:
			curr_max += int(i)
		else:
			maxes.append(curr_max)
			curr_max = 0

	maxes.sort(reverse=True)
	return sum(maxes[0:3])
	

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')

