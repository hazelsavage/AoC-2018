#by reddit user: MrSquigy
#retrieved from https://www.reddit.com/r/adventofcode/comments/a35j5v/2018_day_3_part_1_python_3_im_confused_at_why/ on 06/12/18 @ 6.20pm UTC
#this version edited as I try to figure out how bits of it work...

fabricSize = 1000

fabric = [[0 for i in range(fabricSize)] for n in range(fabricSize)]
overlap = 0

with open('3-1-input.txt', 'r') as f: # use test.txt for the testing stuff
	inpt = f.readlines()

max = len(inpt)

#pos[0] = claim origin x
#pos[1] = claim origin y
#size[0] = claim width w
#size[1] = claim height h


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


  #putting in some labels that I understand
  a = pos[0]
  b = pos[1]
  w = size[0]
  h = size[1]


  # Mark the fabric
  for x in range(a, (a + w)):
    for y in range(b, (b + h)):
      fabric[x][y] += 1

#find the squares with more than one claim
for i in range(fabricSize):
  for n in range(fabricSize):
    if fabric[i][n] > 1:
      overlap += 1

print('There are', overlap, 'overlaps.')



