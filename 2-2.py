from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#Find the two boxIDs that differ by exactly one character;
#What letters are common between both boxIDs? (This is the puzzle answer.)

boxIDs = []
highConf = []
pair = []
letters = ''

print('\n')

file = open('2-1-input.txt', 'r')

for line in file.readlines():
  boxIDs.append(line.rstrip())

for element in boxIDs:
  ratios = process.extract(element,boxIDs)  #spits out a list of tuples.
  highConf.append(ratios[1])

highConf.sort(key=lambda element: element[1],reverse=True)

for element in highConf:
  boxID = element[0]
  pair.append(boxID)
  if len(pair) is 2:
    break

print('The two boxIDs we need are: ' + str(pair) + '.')

for n in range(0,len(pair[0])):
  if pair[0][n] is pair[1][n]:
    letters = letters + pair[0][n]

print('The common letters between the two boxIDs are: ' + letters + '.')
print('\n')

 





