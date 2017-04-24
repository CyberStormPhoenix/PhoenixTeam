##########################################
##Matthew Louque
##Covert Channel for ftp
##4/10/17
##Written in python 2.7
##########################################




from os import listdir
import sys
import ftplib

mode = 0
address = ""
directory = ""

#this is to make the lab easier
#basically sets variables entered as parameters at the command line for the address, directory and mode
if (len(sys.argv) > 1):
	for x in range(0,len(sys.argv)):
		if (sys.argv[x] == "-7"):
			mode = 7
		if (sys.argv[x] == "-10"):
			mode = 10
		if (sys.argv[x] == "-h"):
			print "Usage:"
			print "-7 or -10 for decryption in 7 bit or 10 bit format."
			print "-a <address> where address is the address of the ftp server."
			print "-d <directory> where directory is the directory you wish to fetch the message from."
			print "Example: ftpcovert.py -7 -a ftp.google.com -d /example/Documents would fetch a message from the directory /example/Documents at ftp.google.com using the 7 bit communication mode. "
			exit()
		if (sys.argv[x] == "-a"):
			address = sys.argv[x+1]
		if (sys.argv[x] == "-d"):
			directory = sys.argv[x+1]
else:
	print "No arguments supplied. Enter -h for help."
	exit()
		


#ftpServer = ftplib.FTP('jeangourd.com')
#create a new ftp server on the default port 21 at the address
ftpServer = ftplib.FTP(address)
#login as anonymous
ftpServer.login()
files = []

#if we are using the 7-bit method of covert communication
if (mode == 7):
	#navigate to the correct directory and append the text produced from running dir to files
	ftpServer.dir(directory,files.append)
	outputBinString = ""
	outputString = ""
	#iterate through the lines of the files list (retrieved using dir)
	for line in files:
		#grab only the first ten bits of the line
		line = line[:10]
		binaryNum = ""
		counter = 0
		#for each of the characters of the first 10 bits
		for char in line:
			#if one of the first 3 characters is a 1 disregard the line
			if (counter <3):
				if (char != "-"):
					#disregard this line
					break
				
			#otherwise
			else:
				#if the char is a - it is a 0, otherwise its a 1 and add it to the current binary number
				if (char == "-"):
					binaryNum+="0"
				else:
					binaryNum+="1"
			counter +=1
		#add the binaryNum string to the outputBinString
		outputBinString += binaryNum
		
	#as long as the outputBinString still has characters left
	while (len(outputBinString) >0):
		#grab the next 7 bits
		currentBinNumber = outputBinString[:7]
		outputBinString = outputBinString[7:]
		#convert to ascii
		value = chr(int(currentBinNumber, 2))
		#append the ascii character to the output string
		outputString += value
	#print the outputString	
	print outputString

#if the mode is 10
elif (mode == 10):
	#ftpServer.dir("//10", files.append)
	#navigate to the correct directory and append the text produced from running dir to files
	ftpServer.dir(directory,files.append)
	outputBinString = ""
	outputString = ""
	#iterate through each line in the files list
	for line in files:
		#we only want the first ten characters
		line = line[:10]
		binaryNum = ""
		#for each of the 10 characters
		for char in line:
			#if it is a - its a 0
			if (char == "-"):
				binaryNum+="0"
			#otherwise its a 1
			else:
				binaryNum+="1"
		#add that binary number string to the outputBinString
		outputBinString += binaryNum
	
	#as long as the outputBinString isnt empty
	while (len(outputBinString) >0):
		#grab the first 7 characters
		currentBinNumber = outputBinString[:7]
		outputBinString = outputBinString[7:]
		#convert the 7 bit binary number to ascii
		value = chr(int(currentBinNumber, 2))
		#append the ascii character to the outputString
		outputString += value
	#print the outputString	
	print outputString
	