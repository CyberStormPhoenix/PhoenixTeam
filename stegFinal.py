import sys
import binascii
import time

DEBUG = False
byteMethod = False
bitMethod= False

store = False
retrieve = False
offsetValue = 0
intervalValue = 1
wrapperFileValue = 0
hiddenFileValue = 0
sentinel = ["0x0", "0xff","0x0", "0x0","0xff", "0x0"]
sentinelByteList = [0, 255, 0, 0, 255, 0]

#handles all of the arguments
if (len(sys.argv) == 7):
	#setup for values
	#print "Length:7"
	if (sys.argv[1] == "-B"):
		#byte method
		byteMethod = True
		#print "Byte Method"
	elif(sys.argv[1] == "-b"):
		#bit method
		bitMethod = True
		#print "Bit Method"
	else:
		print "No method specified"
		exit()

	if (sys.argv[2] == "-s"):
		#store data
		store = True
		#print "Store"
	elif(sys.argv[2] == "-r"):
		#retrieve data
		retrieve = True
		#print "Retrieve"
	else:
		print "Did you want to retrieve or store?"
		exit()

	if ("-o" in sys.argv[3]):
		offsetValue = sys.argv[3]
		offsetValue = offsetValue[2:]
		#print "Offset:{}".format(offsetValue)
	else:
		print "No offset value given"
		exit()
	
	if ("-i" in sys.argv[4]):
		intervalValue = sys.argv[4]
		intervalValue = intervalValue[2:]
		#print "Interval:{}".format(intervalValue)
	else:
		print "No interval value given"
		exit()
	
	if ("-w" in sys.argv[5]):
		wrapperFileValue = sys.argv[5]
		wrapperFileValue = wrapperFileValue[2:]
		#print "Wrapper File:{}".format(wrapperFileValue)
	else:
		print "No wrapper file value given"
		exit()

	if ("-h" in sys.argv[6]):
		hiddenFileValue = sys.argv[6]
		hiddenFileValue = hiddenFileValue[2:]
		#print "Hidden File:{}".format(hiddenFileValue)
	else:
		print "No hidden file value given"
		exit()

elif (len(sys.argv) == 6):
	#setup for values
	#print "Length:6"
	if (sys.argv[1] == "-B"):
		#byte method
		byteMethod = True
		#print "Byte Method"
	elif(sys.argv[1] == "-b"):
		#bit method
		bitMethod = True
		#print "Bit Method"
	else:
		print "No method specified"
		exit()

	if (sys.argv[2] == "-s"):
		#store data
		store = True
		#print "Store"
	elif(sys.argv[2] == "-r"):
		#retrieve data
		retrieve = True
		#print "Retrieve"
	else:
		print "Did you want to retrieve or store?"
		exit()

	if ("-o" in sys.argv[3]):
		offsetValue = sys.argv[3]
		offsetValue = offsetValue[2:]
		#print "Offset:{}".format(offsetValue)
	else:
		print "No offset value given"
		exit()
	
	if ("-i" in sys.argv[4]):
		intervalValue = sys.argv[4]
		intervalValue = intervalValue[2:]
		#print "Interval:{}".format(intervalValue)
		if ("-w" in sys.argv[5]):
			wrapperFileValue = sys.argv[5]
			wrapperFileValue = wrapperFileValue[2:]
			#print "Wrapper File:{}".format(wrapperFileValue)
		else:
			print "No wrapper file value given"
			exit()
	else:
		if("-w" in sys.argv[4]):
			wrapperFileValue = sys.argv[4]
			wrapperFileValue = wrapperFileValue[2:]
			#print "Wrapper File:{}".format(wrapperFileValue)
			if ("-h" in sys.argv[5]):
				hiddenFileValue = sys.argv[6]
				hiddenFileValue = hiddenFileValue[2:]
				#print "Hidden File:{}".format(hiddenFileValue)
			else:
				print "No hidden file value given"
				exit()
		
		if ("-w" in sys.argv[5]):
			wrapperFileValue = sys.argv[5]
			wrapperFileValue = wrapperFileValue[2:]
		else:
			#print "No wrapper file value given"
			exit()		
elif (len(sys.argv) == 5): 
	#setup for values
	#print "Length:5"
	if (sys.argv[1] == "-B"):
		#byte method
		byteMethod = True
		#print "Byte Method"
	elif(sys.argv[1] == "-b"):
		#bit method
		bitMethod = True
		#print "Bit Method"
	else:
		#print "No method specified"
		exit()

	if (sys.argv[2] == "-s"):
		#store data
		store = True
		#print "Store"
	elif(sys.argv[2] == "-r"):
		#retrieve data
		retrieve = True
		#print "Retrieve"
	else:
		print "Did you want to retrieve or store?"
		exit()

	if ("-o" in sys.argv[3]):
		offsetValue = sys.argv[3]
		offsetValue = offsetValue[2:]
		#print "Offset:{}".format(offsetValue)
	else:
		print "No offset value given"
		exit()
		
	if ("-w" in sys.argv[4]):
		wrapperFileValue = sys.argv[4]
		wrapperFileValue = wrapperFileValue[2:]
		#print "Wrapper File:{}".format(wrapperFileValue)
	else:
		print "No wrapper file value given"
		exit()
else:
	print "Improper Usage of arguments"
	exit()

	
intervalValue = int(intervalValue)
offsetValue = int(offsetValue)

	
def byteStore(intervalValue, offsetValue):
	hiddenFileInput= []
	wrapperFileInput = []
	
	#make a byte array for each of the two files
	if DEBUG:
		print "byteStore()"
	with open(hiddenFileValue, "rb") as hf:
		dataByte = hf.read(1)
		
		while (dataByte != ""):
			if DEBUG:
				print "HiddenFileReading"
			hiddenFileInput.append(dataByte)
			dataByte= hf.read(1)
	
	with open(wrapperFileValue, "rb") as wf:
		dataByte=wf.read(1)
		
		while (dataByte != ""):
			if DEBUG:
				#print "wrapperFileReading"
				pass
			wrapperFileInput.append(dataByte)
			dataByte=wf.read(1)
			
		
	#simply replace the bytes at the specified intervals with the bytes containing the hidden message
	i = 0
	if DEBUG:
		print "here"
	while (i < len(hiddenFileInput)):
		wrapperFileInput[offsetValue] = hiddenFileInput[i]
		offsetValue += intervalValue
		i+=1
		
	i = 0
	while (i < len(sentinelByteList)):
		wrapperFileInput[offsetValue] = sentinel[i]
		offsetValue+=intervalValue
		i+=1
	
	output =""
	for x in range(0,len(wrapperFileInput)):
		output+=str(wrapperFileInput[x])
	print output

def byteRetrieve():
	#print "intervalValue{}".format(intervalValue)
	#print "offsetValue{}".format(offsetValue)
	#open the wrapper file in read binary mode, call this f 
	with open(wrapperFileValue, "rb") as f:
		sentinelReached = False
		#skip the first offset bytes
		trashByte = f.read(offsetValue)
		#trashByte = f.read(intervalValue)
		#read the next byte
		dataByte = f.read(1)
		#generate an empty output list
		outputList = []
		#loop until we dont get any data
		while (dataByte != ""):
			#loop
			#add the data byte to the outputlist
			outputList.append(dataByte)
			#print "{} {} {}".format(dataByte, ord(dataByte), hex(ord(dataByte)))
			#hex rep of dataByte
			#dataByteHex = hex(ord(dataByte))
			#print "DataByteHex{}".format(dataByteHex)
			#if (dataByteHex == "0xff"):
			#	exit()
			if (len(outputList) >= 6):
				#check if sentinel
				#print "{} - {}".format(hex(ord(outputList[len(outputList)-6])), sentinel[0])
				if (hex(ord(outputList[len(outputList)-6])) == sentinel[0]):
					#print "First Match"
					if (hex(ord(outputList[len(outputList)-5])) == sentinel[1]):
						#print "Second Match"
						if (hex(ord(outputList[len(outputList)-4])) ==sentinel[2]):
							#print "Third Match"
							
							#exit()
							if (hex(ord(outputList[len(outputList)-3])) == sentinel[3]):
								#print "Fourth Match"
								#exit()
								if (hex(ord(outputList[len(outputList)-2])) == sentinel[4]):
									#print "Fifth Match"
									if (hex(ord(outputList[len(outputList)-1])) ==sentinel[5]):
										#print "Sixth Match"
										#exit()
										sentinelReached = True
				
			if (sentinelReached):
				break
			#if the output list has at least 6 things in it
			#skip the interval
			trashByte =f.read(intervalValue-1)
			#then read again
			dataByte=f.read(1)
		
		
		sys.stdout.flush()
		outputString=""
		for i in range(0, len(outputList)):
			outputString+=outputList[i]
		sys.stdout.write(outputString)
		
	
def bitStore(intervalValue, offsetValue):
	hiddenFileInput= []
	wrapperFileInput = []
	
	if DEBUG:
		print "bitStore()"
		
	#open the two files and store each byte as an int in a list	
	with open(hiddenFileValue, "rb") as hf:
		dataByte = hf.read(1)
		
		while (dataByte != ""):
			if DEBUG:
				print "HiddenFileReading"
			hiddenFileInput.append(ord(dataByte))
			dataByte= hf.read(1)
	
	with open(wrapperFileValue, "rb") as wf:
		dataByte=wf.read(1)
		
		while (dataByte != ""):
			if DEBUG:
				#print "wrapperFileReading"
				pass
			wrapperFileInput.append(ord(dataByte))
			dataByte=wf.read(1)
	#aadd the sentinel to the hidden message
	for s in range(0, len(sentinel)):
		hiddenFileInput.append(sentinelByteList[s])
	i = offsetValue
	j = 0
	if DEBUG:
		print "here"
	#continue until we encode all of the hidden message
	while(j<len(hiddenFileInput)):
		#if (isinstance(hiddenFileInput[j], (int, long))):
		#	hiddenFileInput[j]=hiddenFileInput[j]
		#else:
		#	hiddenFileInput[j] = int(hex(ord(hiddenFileInput[j])), 0)
		
		#change the value of the current byte in the wrapper file to a modified byte
		for k in range(8):
			if DEBUG:
				print "i={},j={},k={}".format(i, j, k)
				print " pre wrapper: {0:08b}".format(wrapperFileInput[i])
				print " pre hidden:  {0:08b}".format(hiddenFileInput[j])
			#wrapperFileInput[i]= int(hex(ord(wrapperFileInput[i])),0)
			#hiddenFileInput[j] = int(hex(ord(chr(hiddenFileInput[j])),0)
			wrapperFileInput[i] &= 254
			wrapperFileInput[i] |= ((hiddenFileInput[j] & 128) >> 7)
			hiddenFileInput[j] = long(hiddenFileInput[j] << 1) & 255
			if DEBUG:
				print "post wrapper: {0:08b}".format(wrapperFileInput[i])
				print "post hidden:  {0:08b}".format(hiddenFileInput[j])
			i+=intervalValue
		j+=1
	
	output =""
	#print the output to stdout
	for x in range(0,len(wrapperFileInput)):
		output+=chr(wrapperFileInput[x])
	sys.stdout.write(output)
	
	
	
	
def bitRetrieve():
	
	with open(wrapperFileValue, "rb") as f:
		#throw away the first offset bits
		trashByte= f.read(offsetValue)
		if DEBUG:
			print "Offset : {} ".format(offsetValue)
			#exit()
		dataByte = f.read(1)
		outputList = []
		byte=0
		counterK=0
		counterD=0
		#loop as long as there is more to read
		while (dataByte != ""):
			#we need to figure out the LSB of the current byte
			#then take that value (either a one or a zero)
			#and output it to a string. then convert that string to hex
			#byte needs to be an int
			
			sentinelReached=False	
			dataByteInt= ord(dataByte)
			if DEBUG:
				print "HEXORD:{}".format(hex(ord(dataByte)))
				print "DATABYTEINT: {}".format(dataByteInt)
			binValue = dataByteInt & 1
			byte |= binValue
			if (counterK<7):
				byte <<= 1
			if DEBUG:
				print "Byte Value{}".format(byte)
				#exit()
			#add the str to the binary string
			counterK+=1
			if (counterK == 8):
				if DEBUG:
					print "Appending byte: {}".format(byte)
					counterD +=1
					#exit()
					
				outputList.append(byte)
				byte = 0
				counterK=0
				if (len(outputList) >= len(sentinelByteList)):
					#start checking for the sentinel
					#if we hit it break	
					#print "{} - {}".format(hex(ord(outputList[len(outputList)-6])), sentinel[0])
					if (outputList[len(outputList)-6] == sentinelByteList[0]):
						if DEBUG:
							print "First Match"
							#exit()
						if (outputList[len(outputList)-5] == sentinelByteList[1]):
							#print "Second Match"
							#exit()
							if (outputList[len(outputList)-4] == sentinelByteList[2]):
								#print "Third Match"
								#exit()
								if(outputList[len(outputList)-3] == sentinelByteList[3]):
									#print "Fourth Match"
									#exit()
									if (outputList[len(outputList)-2] == sentinelByteList[4]):
										#print "Fifth Match"
										if (outputList[len(outputList)-1] == sentinelByteList[5]):
											if DEBUG:
												print "Sixth Match"
												#exit()
											sentinelReached = True
					
			if (sentinelReached):
				break
			trashByte = f.read(intervalValue-1)
			dataByte = f.read(1)
			
		
		sys.stdout.flush()
		outputString=""
		#print everything but the sentinel
		for i in range(0, len(outputList)-6):
			outputString+=chr(outputList[i])
		sys.stdout.write(outputString)
			
		
	
if (byteMethod and retrieve):
	#print "byte retrieve"
	byteRetrieve()
elif(bitMethod and retrieve):
	if (DEBUG):
		print "bit retrieve"
	bitRetrieve()
elif(byteMethod and store):
	byteStore(intervalValue, offsetValue)
elif(bitMethod and store):
	bitStore(intervalValue, offsetValue)
else:
	print "Not A valid option"
	exit()
