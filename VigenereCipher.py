##########################################
##Matthew Louque
##Implementation of a Vigenere Cypher in python 2.7
##3/30/17
##########################################

#needed to grab command line arguments
import sys

def logic(mode):
	#this is gonna be the basis for the output
	outputString = ""
	#grab the input
	rawMessage = raw_input()
	#need these to build lists.
	rawMessageValues = []
	capLetterList = []
	for x in rawMessage:
		#if we have a letter
		if x in alphabetList:
			#grabs the index of the current letter in the alphabet list
			value = alphabetList.index(x)
			#append that value to the list of letter values
			rawMessageValues.append(value)
		#if we have a capital letter
		elif x in alphabetCapList:
			#make it a lowercase letter
			value = alphabetList.index(x.lower())
			#append the value of the lowercase letter to the list of values 
			rawMessageValues.append(value)
			#append the current location to the list of letters that need to be capitalized
			capLetterList.append(rawMessage.index(x))
		#it isnt a letter
		else:
			#just append it
			rawMessageValues.append(x)
	#list for the outputvalues
	outputValues = []
	#length of the key
	keyLength = len(keyValues)
	#where we should be in the key
	counter = 0
	#go through the values that need to be encrypted or decrypted
	for y in rawMessageValues:
		try:
			#if the mode is encrypt add the value of the current letter in the key
			#if the mode is decrypt subtract the value of the current letter in the key
			# %keyLength makes it loop through the key over and over
			if (mode == "encrypt"):
				value = y + (keyValues[counter%(keyLength)])
			elif (mode == "decrypt"):
				value = y - (keyValues[counter%(keyLength)])
			#gives us the value of the new letter
			value = value % 26
			#put this in output value list
			outputValues.append(value)
			counter+=1
		#this means it wasnt a letter so dont encrypt or decrypt
		except TypeError:
			outputValues.append(y)
			
	#print "Output values: "+str(outputValues)
	
	#convert the output values to the correct letter
	for z in outputValues:
		#its a letter
		try: 
			#so grab the letter in the alphabetList at that index
			value = alphabetList[z]
			#add it to the output string
			outputString+=value
		#it isnt a letter so just append it
		except: 
			#print "exception"
			outputString+=z
	
	#loops through the list of indices of letters that need to be capitalized
	for q in capLetterList:
		#outputString[q] = outputString[q].upper()
		#takes the output string up to this point, swaps the character, then keeps going
		outputString = outputString[:q] + outputString[q].swapcase() + outputString[(q+1):]
	# print the final output	
	print outputString
	#print rawMessage

#define the alphabet lists	
alphabetCapString ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetCapList = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alphabetString = "abcdefghijklmnopqrstuvwxyz"
alphabetList = list('abcdefghijklmnopqrstuvwxyz')

if (len(sys.argv) >2):
	#this grabs the first command line argument, either a -d or a -e
	mode = sys.argv[1]
	#this grabs the key string
	keyString = sys.argv[2]
else:
	print "You didnt enter a valid mode or key, use -e to encrypt and -d to decrypt followed by a key"
	exit()
 
#convert it to lowercase
keyString = keyString.lower()
#convert it to a list
keyList = list(keyString)
keyValues = []
#set the value from 0 -25 for the corresponding letter of the alphabet
#this is calculated using the index of the item in the alphabetList
for x in keyList:
	if x in alphabetList:
		value = alphabetList.index(x)
		keyValues.append(value)
	#else:
	#	keyValues.append(x)
#print keyValues
#if the mode was -d decrypt
if (mode == '-d'):
	logic("decrypt")
#if the mode was -e encrypt
elif(mode == '-e' ):
	logic("encrypt")
#they didnt enter a valid mode
else:
	print "You didnt enter a valid mode, use -e to encrypt and -d to decrypt"
	exit()
 
 
