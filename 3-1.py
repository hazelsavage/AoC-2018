# **how many units of fabric are within 2 or more of the claims?** (puzzle answer)
# a,b is the offset from the fabric origin.
# x,y is the area of the rectangle to be drawn.
# fabric is >= 1000,1000.
#claim is in the format '#id_int @ a,b: (w)x(h)', e.g. '#123 @ 3,2: 5x4'

import re

def getFabricSize (a, b, w, h):

  if (a + w) > fabricSize[0]:
    fabricSize[0] = (a + w)

  if (b + h) > fabricSize[1]:
    fabricSize[1] = (b + h)

  return fabricSize


def markFabric (a, b, w, h, fabric):
  for x in range (a, (a + w)):
    for y in range (b, (b + h)):
      fabric[x][y] += 1



def findSquares (fabricSize, fabric):
  squares = 0
  for i in range(0,fabricSize[0]):
    for j in range(0,fabricSize[1]):
      if fabric[i][j] >= 2:
        squares += 1
  return squares
 

fabricSize = [0,0]

#read the data in
claims = []
file = open('3-1-input.txt','r')
for line in file.readlines():
  getClaim = re.search('(#\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)' , line.rstrip())
  if getClaim == None:
    print(line.rstrip() + ' is not a valid claim.')
  else:
    claimID = getClaim[1]
    a = int(getClaim[2])
    b = int(getClaim[3])
    w = int(getClaim[4])
    h = int(getClaim[5])
    
    claim = [claimID, a, b, w, h]
    claims.append(claim)

    #get the fabric max size
    fabricSize = getFabricSize(a, b, w, h)



fabric = [[0 for i in range (fabricSize[0])] for j in range (fabricSize[1])]

#mark the fabric
for claim in claims:
  markFabric(claim[1], claim[2], claim[3], claim[4], fabric)

#find squares with more than one claim
squares = findSquares(fabricSize, fabric)
  

print('\nThere are ' + str(len(claims)) + ' claims.')
print('The claims use fabric that is max. ' + str(fabricSize[0]) + ',' + str(fabricSize[1]) + ' square inches in size.')
print('There are ' + str(squares) + ' square inches of overlapping claims.\n')








