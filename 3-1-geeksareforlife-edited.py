#this solution 'borrowed' from @geeksareforlife because I had absolutely no clue where to start.
#retrieved from https://github.com/geeksareforlife/advent-of-code/blob/master/2018/03/puzzle1.py on 04/12/18 @ ~6pm UTC.
#this version then edited as I try to figure out how bits of it works...


# a = claim_origin.x
# b = claim_origin.y
# w = claim_width
# h = claim_height

import re

def makeClaim(fabric, claimID, a, b, w, h):

  fabric = extendFabric(fabric, a, b, w, h)

  for x in range(a, (a + w)):
    for y in range(b, (b + h)):
      fabric[x][y].append(claimID)

  return fabric

#---

def extendFabric(fabric, a, b, w, h):

  while len(fabric) < (a + w):
    fabric.append([])

  for column in range(a, (a + w)):
    while len(fabric[column]) < (b + h):
      fabric[column].append([])

  return fabric

#---


# this will be a multi-dimensional array
# The first two dimensions will be columns and rows.
# Each cell will contain an array of the IDs that are claiming that square inch
fabric = []

with open('3-1-input.txt') as input:
  claims = list(input)

for claim in claims:
  match = re.search('(#\d+) @ (\d+),(\d+): (\d+)x(\d+)', claim.strip())
  if (match == None):
    print("Claim not matched: " + claim.strip())
  else:
    claimID = match[1]
    a = int(match[2])
    b = int(match[3])
    w = int(match[4])
    h = int(match[5])

    fabric = makeClaim(fabric, claimID, a, b, w, h)



# loop over the fabric and count square that have >1 claim
squares = 0
for column in fabric:
  for row in column:
    if len(row) > 1:
      squares += 1

print(str(squares) + " square inches have multiple claims")



