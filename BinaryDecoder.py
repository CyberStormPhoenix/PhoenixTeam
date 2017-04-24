##########################################
##Matthew Louque
##Binary decoder in python3
##3/27/17
##########################################


#grabs the raw input
rawInput=input()
#print(len(rawInput))
#NOTE if it divisible by 7 and 8, print both and then look at it to determine which is the correct message.
#if it is divisible by 7 its in 7 bit binary
if (len(rawInput) % 7 == 0):
	#make an outputString
	outputString = ''
	#repeat until the string is empty
	while (len(rawInput) >0):
		#grab the first 7 characters
		currentBinNumber = rawInput[:7]
		#remove the first 7 characters from the input string
		rawInput = rawInput[7:]
		#print(currentBinNumber)
		#print(rawInput)
		#convert that to an integer in base 2
		int(currentBinNumber, 2)
		#convert that integer to an ASCII character
		value = chr(int(currentBinNumber, 2))
		#print(value)
		#add the ASCII character to the output string
		outputString+=value
	#once we have read all of the input output it to stdout
	print(outputString)
#if it is divisible by 8 its in 8 bit binary
if (len(rawInput) % 8 ==0):
	#make an outputString
	outputString = ''
	#repeat until the string is empty
	while (len(rawInput) >0):
		#grab the first 8 characters
		currentBinNumber = rawInput[:8]
		#remove the first 8 characters from the input string
		rawInput = rawInput[8:]
		#print(currentBinNumber)
		#print(rawInput)
		#convert that to an integer in base 2
		int(currentBinNumber, 2)
		#convert that integer to an ASCII character
		value = chr(int(currentBinNumber, 2))
		#print(value)
		outputString+=value
		#add the ASCII character to the output string
	#once we have read all of the input output it to stdout
	print(outputString)
#if not divisible by 7 or 8 its an invalid input
else:
	print("Not a Valid input")
	


	