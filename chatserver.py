import socket 
import time
from binascii import hexlify


ZERO = 0.01
ONE = 0.1

covert = "oh hey look a secret message" + "EOF"
covert_bin = ""
for i in covert:
	#convert each character to a full byte
	#hexlify converts the ASCII to hex
	# int converts the hex to a decimal integer
	# bin provides its binary representation (with a 0b prefix that must be removed)
	# that's the [2:] (return the string from the third character on)
	# zfill left-pads the bit string with 0s to ensure a full byte
	covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8)


#create a socket
#probably best to do in a try:except
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1337
s.bind(("", port))
s.listen(0)


#accept a connecting client
c, addr = s.accept()
#c becomes a socket representing the connection of the client to the server
#addr is the address of the connecting client

#to send a message, one char at a time

msg = "There is a super duper secret message hidden in here somewhere if you know how to look. Or maybe there isn't, how would i know? You can't expect me to know everything in the entire universe. That's a heavy burden for a crappy python chat server."
print msg
n = 0

for i in msg:
	c.send(i)
	print i
	if(covert_bin[n] == "0"):
		time.sleep(ZERO)
	else:
		time.sleep(ONE)
	n = (n+1) % len(covert_bin)
	
c.send("EOF")
c.close()


	



