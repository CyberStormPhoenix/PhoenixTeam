import socket
import sys
from time import time 
from binascii import hexlify
from binascii import unhexlify

ZERO = 0.01
ONE = 0.1
print "Connecting to Server"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1337))

covert_bin = ""
covert = ""


data = s.recv(4096)

while (data.rstrip("\n") != "EOF"):
	sys.stdout.write(data)
	t0 = time()
	data = s.recv(4096)
	#print data
	t1 = time()
	#round to the second decimal
	delta = round(t1-t0, 2)
	if(delta >= ONE):
		covert_bin +="1"
	else:
		covert_bin+="0"
	
	
	sys.stdout.flush()
	
s.close()
print "\nDisconnecting from Server"

i = 0
#print covert_bin
while(i < len(covert_bin)):
	#process one byte at a time
	b = covert_bin[i:i + 8]
	#convert it to ASCII
	n = int("0b{}".format(b), 2)
	try: 
		covert += unhexlify("{0:x}".format(n))
	except TypeError:
		covert +="?"
	# stop at the string "EOF"
	i +=8
	if (len(covert) >2 and covert[len(covert)-3] == "E" and covert[len(covert)-2] == "O" and covert[len(covert)-1] == "F"):
		break
covert = covert[:len(covert)-3]
print covert
