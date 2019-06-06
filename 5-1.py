import re

myFile = open('5-1-input.txt', 'r')

polymer = myFile.read().rstrip()
  
newLength = len(polymer)
oldLength = len(polymer) + 1
counter = 0

while (newLength < oldLength):
  counter += 1
  oldLength = newLength
  polymer = re.sub('(?i:(.)\\1)(?<=[a-z][A-Z]|[A-Z][a-z])', '', polymer)
  newLength = len(polymer)
    

print("The fully reacted polymer contains " + str(len(polymer)) + " units.")
print("The polymer reacted over " + str(counter) +" iterations.")
