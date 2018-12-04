import itertools


file = open('1-1-input.txt','r')

linesIn = []
freqChanges = []
currentFreq = 0
seen = set([0])


print('Reading-in the file line-by-line...')
for line in file.readlines():
  linesIn.append(line.rstrip())

print('Converting from strings to integers...')
for element in linesIn:
  freqChanges.append(int(element))


print('searching for the first duplicate frequency...')

for element in itertools.cycle(freqChanges):
  currentFreq = currentFreq + element
  if currentFreq in seen:
    print(currentFreq)
    break
  seen.add(currentFreq)

