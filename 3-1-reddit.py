#by reddit user: MrSquigy
#retrieved from https://www.reddit.com/r/adventofcode/comments/a35j5v/2018_day_3_part_1_python_3_im_confused_at_why/ on 06/12/18 @ 6.20pm UTC
#this version edited as I try to figure out how bits of it work...

SIZE = 1000

def disp(fabric):
	for i in range(len(fabric)):
		for n in range(len(fabric[i])):
			print(fabric[i][n], end = '')
		print()

fabric = [[0 for i in range(SIZE)] for n in range(SIZE)]
overlap = 0

with open('3-1-input.txt', 'r') as f: # use test.txt for the testing stuff
	inpt = f.readlines()

max = len(inpt)

for i in range(len(inpt)):
	# Format #123 @ 3,2: 5x4 3 units from left, 2 units from top, 5 units wide, 4 units tall
	perc = i / max * 100
	print('%d %d/%d' % (perc, i, max)) # Show progress through claims
	claim = inpt[i].split()
	id = claim[0][1:] # Remove the # from id
	pos = claim[2].split(',') # Split along ,
	pos[1] = int(pos[1][:-1]) # Remove : from end of pos y
	pos[0] = int(pos[0]) # Convert to int
	size = claim[3].split('x') # Split along x
	size[0] = int(size[0]) # Convert to int
	size[1] = int(size[1]) # Convert to int

	# Mark the fabric
	for x in range(pos[0], (pos[0] + size[0])):
		for y in range(pos[1], (pos[1] + size[1])):
			fabric[x][y] += 1

for i in range(SIZE):
	for n in range(SIZE):
		if fabric[i][n] > 1:
			overlap += 1

print('There are', overlap, 'overlaps.')



