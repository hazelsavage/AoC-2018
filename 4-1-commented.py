import re
from datetime import datetime, date, time, timedelta
from copy import copy

#Example data (three variants):
# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up


records = []

#read the data in
file = open('4-1-input.txt', 'r')
for line in file.readlines():

  #regular expressions \o/
  getRecord = re.match('\[(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2})\]\s(\w)\w+\s#*(\d*)' , line.rstrip())

  if getRecord == None:
    print("'" + line.rstrip() + "'" + ' is not a valid record.')
  else:
    #use datetime.datetime.strptime to make a datetime object
    dt = datetime.strptime(getRecord[1],"%Y-%m-%d %H:%M")

    #if we found a guard ID number set the state variable to 'g'
    #and store the guardID
    if getRecord[3] is not '':
      state = 'g'
      guardID = getRecord[3]
    else:
      #otherwise set the state to the 'f'(alls asleep) or 'w'(akes up) we picked up with the regex
      #and store nothing in the guardID
      state = getRecord[2]
      guardID = None
    
    #make a list called 'record' and add it to a list of all the records
    record = [dt, state, guardID]
    records.append(record)

#sort the list of records by the first element (which is the datetime object)
records.sort(key=lambda element:element[0])

guardSleeps = {}
guardRecords = []
for record in records:
  #print(record[0].date(), record[0].time(), record[1], record[2])
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

  #collect all the fell asleep (f) and wake (w) pairs for guards and store them in a data structure (we will use this later)
  guardRecord = [g,f,w]
  guardRecords.append(guardRecord)
 

#sort the dictionary of guard sleep amounts
sorted_guardSleeps = sorted(guardSleeps.items(), key=lambda element: element[1], reverse = True)

#remember who the sleepiest guard is and their sleep amount
sleepyGuard = sorted_guardSleeps[0][0]
sG_sleepAmount = sorted_guardSleeps[0][1]

print('\nThe guard who slept the most is guard ' + sleepyGuard + '.')
print('They slept for ' + str(sG_sleepAmount) + ' hours:minutes.\n')
  


#collect all of the fell-asleep and woke-up times just for sleepyGuard
sgRecords = []
for guardRecord in guardRecords:
    if guardRecord[0] == sleepyGuard:
      sgRecords.append(guardRecord)   


#create a dictionary that has keys of 0 - 59 (minutes) and values that are int type
minuteFrequency = {}
for i in range (0,60):
  minuteFrequency[i] = 0


#run a loop for each pair of times that starts at f.minute and ends at w.minute, and increment minute:value in the dictionary we made
for sgRecord in sgRecords:
  for i in range (sgRecord[1].minute, sgRecord[2].minute):
    minuteFrequency[i] +=1

#sort the minuteFrequency dictionary so that the most frequent minute is the first element:
sorted_minuteFreq = sorted(minuteFrequency.items(), key=lambda element: element[1], reverse = True)

#find the key at the top of our sorted dictionary
mostFreqMin = sorted_minuteFreq[0][0]

#calculate the answer to the puzzle
puzzleAns = mostFreqMin * int(sleepyGuard)


print('\nThe minute the guard was most often asleep in was: ' + str(mostFreqMin) + '.')
print('The answer to the puzzle is: ' + str(puzzleAns) + '.\n')




  








