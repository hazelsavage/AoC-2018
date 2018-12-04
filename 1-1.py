file = open('1-1-input.txt','r')

linesIn = []
frequencies = []
total = 0


print('Reading-in the file line-by-line...')
for line in file.readlines():
  linesIn.append(line.rstrip())

print('Converting from strings to integers...')
for element in linesIn:
  frequencies.append(int(element))

print('Adding everything up...')
for element in frequencies:
  total = total + element

print('The final total is ' + str(total))



  

