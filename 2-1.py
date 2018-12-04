t1 = 0  #test1: how many boxIDs contain the same character twice
t2 = 0  #test2: how many boxIDs contain the same character three times
checksum = 0  #t1 * t2 gives a rudimentary checksum
print('\n')

file = open('2-1-input.txt', 'r')

for line in file.readlines():
  boxID = line.rstrip()
  charCount = {char:boxID.count(char) for char in boxID}
  print('boxID ' + str(boxID) + ':\n' + str(charCount))
  if 2 in list(charCount.values()):
    t1+=1
  if 3 in list(charCount.values()):
    t2+=1

checksum = t1*t2
print('\n' + str(t1)+' boxIDs with two of the same character in.')
print(str(t2)+' boxIDs with three of the same character in.')
print('checksum for this set of boxIDs = ' + str(checksum) + '\n')

