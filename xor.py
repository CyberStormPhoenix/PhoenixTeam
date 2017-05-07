###################
#
# Team Phoenix
# XOR Cipher
# May 4, 2017
#
###################

import sys
import binascii

#read input from stdin
textIn = sys.stdin.read()

#file name for the key is key
fileName= "key"

#open file key
f = open(fileName) 

#read key and store it as a string in keywords
keywords = f.read()

#convert the input and key to ascii values
a = binascii.hexlify(textIn)
b = binascii.hexlify(keywords)

#convert into an integer
#perform xor operation on the integer value
value = (int(a, 16) ^ int(b, 16))

#convert the integers back to ascii characters and print the result to stdout
sys.stdout.write(binascii.unhexlify('%x' % value))

#close the file object
f.close()


#convert the integers back to ascii characters and print the result to stdout
sys.stdout.write(binascii.unhexlify('%x' % value))

#close the file object
f.close()
