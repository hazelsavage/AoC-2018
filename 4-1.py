import re
from datetime import datetime, date, time, timedelta
from copy import copy

#Example data (three variants):
# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up

records = []

file = open('4-1-input.txt', 'r')
for line in file.readlines():

  getRecord = re.match('\[(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2})\]\s(\w)\w+\s#*(\d*)' , line.rstrip())

  if getRecord == None:
    print("'" + line.rstrip() + "'" + ' is not a valid record.')
  else:
    dt = datetime.strptime(getRecord[1],"%Y-%m-%d %H:%M")

    if getRecord[3] is not '':
      state = 'g'
      guardID = getRecord[3]
    else:
      state = getRecord[2]
      guardID = None
    
    record = [dt, state, guardID]
    records.append(record)

records.sort(key=lambda element:element[0])

guardSleeps = {}
guardRecords = []
for record in records:
  if record[1] is 'g': 
    g = record[2] 
    continue

  elif record[1] is 'f':
    f = record[0]
    continue

  elif record[1] is 'w':
    w = record[0]

    sleepAmount = w - f

    if g not in guardSleeps:
      guardSleeps[g] = sleepAmount
    else:
      guardSleeps[g] += sleepAmount

  guardRecord = [g,f,w]
  guardRecords.append(guardRecord)
 
sorted_guardSleeps = sorted(guardSleeps.items(), key=lambda element: element[1], reverse = True)

sleepyGuard = sorted_guardSleeps[0][0]
sG_sleepAmount = sorted_guardSleeps[0][1]

print('\nThe guard who slept the most is guard ' + sleepyGuard + '.')
print('They slept for ' + str(sG_sleepAmount) + ' hours:minutes.\n')
  
sgRecords = []
for guardRecord in guardRecords:
    if guardRecord[0] == sleepyGuard:
      sgRecords.append(guardRecord)   

minuteFrequency = {}
for i in range (0,60):
  minuteFrequency[i] = 0

for sgRecord in sgRecords:
  for i in range (sgRecord[1].minute, sgRecord[2].minute):
    minuteFrequency[i] +=1

sorted_minuteFreq = sorted(minuteFrequency.items(), key=lambda element: element[1], reverse = True)

mostFreqMin = sorted_minuteFreq[0][0]
puzzleAns = mostFreqMin * int(sleepyGuard)

print('\nThe minute the guard was most often asleep in was: ' + str(mostFreqMin) + '.')
print('The answer to the puzzle is: ' + str(puzzleAns) + '.\n')




  








