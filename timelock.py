#Phoenix Team

##DEPENDENCIES: pytz from python.
##pip install pytz

import sys 
from datetime import datetime, timedelta
import math
import time
import pytz
import hashlib
DEBUG = False
#the current timezone
serverTimeZone = pytz.timezone("US/Central")
#utc timezone
newTimeZone = pytz.utc
if (len(sys.argv)>= 7):
	#epoch = Epoch(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
	#print epoch
	#set the epoch time
	epoch = datetime(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
	#convert the epoch from the local time to UTC time
	epoch = serverTimeZone.localize(epoch).astimezone(newTimeZone)
	if DEBUG:
		print epoch
else:
	exit()
	
#currentTime = datetime.now()#datetime.utcnow()
if DEBUG:
	currentTime = datetime(int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9]), int(sys.argv[10]), int(sys.argv[11]), int(sys.argv[12]))
	currentTime=serverTimeZone.localize(currentTime).astimezone(newTimeZone)
	currentTimeRounded = currentTime
else:
	#grab the current date and time
	currentTime = datetime.now()
	currentTimeRounded = datetime(currentTime.year, currentTime.month, currentTime.day, currentTime.hour, currentTime.minute, int(math.floor(currentTime.second)))
	#print "CurrentTime: {}".format(currentTimeRounded)
	#convert that to UTC
	currentTimeRounded=serverTimeZone.localize(currentTime).astimezone(newTimeZone)
	#currentTimeRounded= currentTime.replace(second=int(math.floor(currentTime.second)))
	print "CurrentTime: {}".format(currentTimeRounded)


timeDifference = currentTimeRounded-epoch
secondsBetween = timeDifference.total_seconds()
#print secondsBetween	
#print int(secondsBetween)

secondsBetween = int(math.floor(secondsBetween))
secondsBetween = secondsBetween - (secondsBetween % 60)
secondBetweenString = str(secondsBetween)
print "Seconds Between: {} ".format(secondBetweenString)
if DEBUG:
	secondsOver = secondsBetween + 3600
	secondsUnder = secondsBetween - 3600
	secondsOverString = str(secondsOver)
	secondsUnderString = str(secondsUnder)

if DEBUG:
	print secondBetweenString

m1 = hashlib.md5()
m1.update(secondBetweenString)
m1output = m1.hexdigest()
#print m1output

m2 = hashlib.md5()
m2.update(m1output)
outputHash=m2.hexdigest()
print "CorrectHash: {}".format(outputHash)
alphaString="abcdefghijklmnopqrstuvwxyz"
shortCode=""
hashCounter=0
for c in outputHash:
	if (c in alphaString):
		shortCode+=c
		hashCounter+=1
	if (hashCounter==2):
		break
numString="0123456789"
for x in range(1,len(outputHash)):
	if (outputHash[len(outputHash)-x] in numString):
		shortCode+=outputHash[len(outputHash)-x]
	
	if (len(shortCode) == 4):
		break
print "Short Code: {}".format(shortCode)

if DEBUG:
	m3 = hashlib.md5()
	m3.update(secondsOverString)
	m3output = m3.hexdigest()
	#print m1output


	m4 = hashlib.md5()
	m4.update(m3output)
	print "HourOverHash: {}".format(m4.hexdigest())

	m5 = hashlib.md5()
	m5.update(secondsUnderString)
	m5output = m5.hexdigest()
	#print m1output

	m6 = hashlib.md5()
	m6.update(m5output)
	print "HourUnderHash: {}".format(m6.hexdigest())

	


