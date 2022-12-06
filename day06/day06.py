import random, math

def load():
	with open('day06/day06Input.txt') as file:
		data = file.readlines()
		d = [line.strip() for line in data]
	return d

inpt = load()
def part1(inpt, size):
	inpt = inpt[0]
	for i in range(0,len(inpt)-size):
		if len(set(inpt[i:i+size])) == size:
			return i + size
	return inpt

def part2(inpt):
	return inpt

print(f'Part1: {part1(inpt, 4)}\nPart2: {part1(inpt, 14)}')