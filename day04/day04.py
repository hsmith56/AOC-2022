import random, math

def load():
	with open('day04/day04Input.txt') as file:
		data = file.readlines()
		d = [line.strip() for line in data]
	return d

inpt = load()
def part1(inpt):
	counter = 0
	for x in inpt:
		l,r = x.split(",")
		l1,l2 =l.split("-")
		r1,r2 = r.split("-")
		l1, l2, r1, r2 = int(l1), int(l2), int(r1), int(r2)
		if l1 >= r1 and l2 <= r2:
			counter += 1
		elif r1 >= l1 and r2 <= l2:
			counter += 1
		else:
			pass
	return counter

def part2(inpt):
	counter = 0
	for x in inpt:
		l,r = x.split(",")
		l1,l2 =l.split("-")
		r1,r2 = r.split("-")
		l1, l2, r1, r2 = int(l1), int(l2), int(r1), int(r2)
		left = [x for x in range(l1, l2+1)]
		right = [x for x in range(r1, r2+1)]
		if set(left) & set(right):
			counter += 1
	return counter
	
print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')