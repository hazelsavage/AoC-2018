#Puzzle 2: Of all guards, which guard is most frequently asleep on the same minute?

#In the example, Guard #99 spent minute 45 asleep more than any other guard or minute - three times in total.
#(In all other cases, any guard spent any minute asleep at most twice.)

#What is the ID of that guard multiplied by that minute?


import re
from datetime import datetime, date, time, timedelta	#import some datetime modules so we can deal with the dates and times in the records.
from copy import copy					#I can't honestly remember what we need 'copy' for, maybe nothing.

#Example data (three variants):
# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up


#we need to load in all the records (which are all mixed up) and sort them into chronological order

records = []	#create a list called 'records'

file = open('4-1-input.txt', 'r')	#open the file containing the inputs provided by AoC

#--beginning of for loop--

for line in file.readlines():		#read the file, one line at a time

  getRecord = re.match('\[(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2})\]\s(\w)\w+\s#*(\d*)' , line.rstrip())	#regular expressions \o/

  if getRecord == None:		#if the regular expression does not find a match for in the line we read in
    print("'" + line.rstrip() + "'" + ' is not a valid record.')
  else:
    dt = datetime.strptime(getRecord[1],"%Y-%m-%d %H:%M")	#if we do find a match for the regular expression, turn the date and time part into a 'datetime' object

    if getRecord[3] is not '':		#if the 3rd part of the regular expression (the guard ID number) exists
      state = 'g'			#set the 'state' to 'g' (a guard begins a shift)
      guardID = getRecord[3]		#grab the ID of the guard who began the shift
    else:
      state = getRecord[2]		#if the guard ID did not exist on that line, set the 'state' to the 'f'(alls asleep) or 'w'(akes up) we picked up in the RE 
      guardID = None			#and set the guard ID to none (as there wasn't one in this line)
    
    record = [dt, state, guardID]	#create a list (basically an array) containing the 'datetime' object, the state [g(uard #x begins shift), f(alls asleep), or w(akes up)]
					#and the guardID [which is either a number-as-string or 'None'].
    records.append(record)		# and then append it to 'records', which is the list of records we created/initialised before we started the for loop

#--end of loop--
 					

records.sort(key=lambda element:element[0])	#sort the records list according to element 0, which is the datetime object



guardSleeps = {}			#create a dictionary called 'guardSleeps'; this will contain 'keys'(the guard IDs) and 'values'(the number of minutes
					#they slept for: we will increment this as we search the list of records.

guardRecords = []			#create a list(array) called 'guardRecords'


#--beginning of for loop

for record in records:			#for each record in our sorted-by-date-and-time 'records' list, look through them one-by-one;
  if record[1] is 'g': 			#if the second item in our record is a 'g' (denoting a guard coming on shift),
    g = record[2] 			#then get the guard ID from the record, and store it in a new variable g.
    continue				#Next we need to look at the records following this one, so stop this iteration of the loop and move to the next record.

  elif record[1] is 'f':		#if the letter is an 'f' instead, then this is denoting when the aforementioned guard fell asleep;
    f = record[0]			#So store the time from this record (the time the guard fell asleep) in the new variable f.
    continue				#Then jump out of the loop and go back to the top of it, looking at the next record. 

  elif record[1] is 'w':		#if the letter is a 'w', this denotes when the guard woke up;
    w = record[0]			#So take the time from the beginning of this record and store it in a new variable w.

    sleepAmount = w - f			#we can perform arithmetic on datetime objects, so get the length of the guard's sleep,
					#by subtracting the fellAsleep time from the wake time.

    if g not in guardSleeps:		#if the guardID is not already in our dictionary of guard sleep amounts,
      guardSleeps[g] = sleepAmount	#then create a new key&value pair, like:   guardID (as key): sleepAmount (as value)
    else:
      guardSleeps[g] += sleepAmount	#Otherwise (if we have already stored this guardID in our dictionary) add the sleepAmount to whatever value is already
					#stored against that guardID.

  guardRecord = [g,f,w]			#create a new record containing the guard ID [0], fall asleep time [1], woke up time [2] we have just found,
  guardRecords.append(guardRecord)	#and add them as a line in our 'guardRecords' list.

#--end of the for loop--

 
sorted_guardSleeps = sorted(guardSleeps.items(), key=lambda element: element[1], reverse = True)	#reverse-sort our dictionary of guardSleeps by element[1], 
													#which is the value, so that the highest value is at the top.
																					
sleepyGuard = sorted_guardSleeps[0][0]		#create a variable 'sleepyGuard' and set it to the key(the guardID) at the top of our sorted dictionary.
sG_sleepAmount = sorted_guardSleeps[0][1]	#create a variable 'sG_sleepAmount' and set it to the value at the top of our sorted dictionary.

print('\nThe guard who slept the most is guard ' + sleepyGuard + '.')	#Tell everyone on the commandline who the sleepiest guard is,
print('They slept for ' + str(sG_sleepAmount) + ' hours:minutes.\n')	#and how long they slept for in total.


#But we need to find out which minute this very sleepy guard is most often asleep in:

sgRecords = []		#make a new list called sgRecords (short for sleepguard Records)


for guardRecord in guardRecords:		#Loop through all our guard records,
    if guardRecord[0] == sleepyGuard:		#until we find one for our sleepy guard
      sgRecords.append(guardRecord)   		#Add any matching records that we find to the sgRecords list.

minuteFrequency = {}		#Create a new dictionary 'minuteFrequency'.
for i in range (0,59):		#loop through the range 0 to 59: these numbers represent the minutes of an hour.
  minuteFrequency[i] = 0	#for each of this range, create a key and value pair in the dictionary, as {minute number: 0}.

for sgRecord in sgRecords:					#loop through the sleep records of our sleepy guard;	
  for i in range (sgRecord[1].minute, sgRecord[2].minute):	#in each of the records, loop through the range of minutes from the 'f' minute to the 'w' minute.
    minuteFrequency[i] +=1					#for each minute in this range, increment the value of that 'minute' key in the dictionary by 1. 				

sorted_minuteFreq = sorted(minuteFrequency.items(), key=lambda element: element[1], reverse = True)	#reverse-sort the dictionary by the values (not the keys),
													#and store the resulting dictionary with a new name.

mostFreqMin = sorted_minuteFreq[0][0]		#Store the key that is at the top of our sorted dictionary as the variable 'mostFreqMin' (because it is).
puzzleAns = mostFreqMin * int(sleepyGuard)	#Make a new variable 'puzzleAns', and calculate the answer to Part 1 of the 'Day 4' puzzle.

print('\nThe minute the guard was most often asleep in was: ' + str(mostFreqMin) + '.')		#Print the minute our guard was most often asleep to the console.
print('The answer to the puzzle is: ' + str(puzzleAns) + '.\n')					#Print the puzzle answer to the console.

#--END--






