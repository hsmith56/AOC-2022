import random, math

def load():
	with open('day02/day02Input.txt') as file:
		data = file.readlines()
		d = [line.strip() for line in data]
	return d

inpt = load()
def part1(inpt):
	score = 0
	for i in inpt:
		x = (i.replace("A",'1').replace("B",'2').replace("C",'3').replace("X",'1').replace("Y",'2').replace("Z",'3').split(" "))
		left, right = int(x[0]), int(x[1])
		#print(left, right)
		if abs(left - right) == 1 and left < right:
			score += 6 + right
		elif abs(left - right) == 1 and left > right:
			score += right
		elif left == 1 and right == 3:
			score += right
		elif left == 3 and right == 1:
			score += 6 + right
		else:
			score += 3 + right
	return score

def part2(input):
	# 1 = lose, 2 = win, 3 = tie
	score = 0
	for i in input:
		x = (i.replace("A",'1').replace("B",'2').replace("C",'3').replace("X",'1').replace("Y",'2').replace("Z",'3').split(" "))
		left, right = int(x[0]), int(x[1])
		if right == 1:
			if left == 1:
				score += 3
				continue
			score += left - 1
		elif right == 2:
			score += left + 3
		else:
			if left == 3:
				score += 7
				continue
			score += left + 7
	return score

print(f'Part1: {part1(inpt)}\nPart2: {part2(inpt)}')