# RSA encryption of the contents of a file one byte at a time

# public and private keys
n = 437 	# product of primes
e = 5   	# encryption exponent
d = 317 	# decryption exponent


infile = raw_input("Input file name: ") 	# read in the input file name
infd = open(infile,"r")    	    	    	# open the file and create the file descriptor infd
outfile = raw_input("Output file name: ")   	# read in the output file name
outfd = open(outfile,"w")  	    	    	# open the file and create the file descriptor outfd  	    	

# now read 1 byte at a time from the input file, encrypt it and write the encrypted byte to the output file
# when the end of the input file is reached (zero bytes read) exit the while loop and close the files 
while 1:
    ptext = infd.read(1)
    if len(ptext) != 0:
        ctext = pow(ord(ptext),e,n)
        print >> outfd, '%i' % (ctext)
    else:
        break
infd.close()
outfd.close()

# now open and read the encrypted file
infile = raw_input("Input encyypted file name: ") 	# read in the input file name
infd = open(infile,"r")    	    	    	    	# open the file and create the file descriptor infd

# Now read 1 line at a time from the encrypted file, decrypt it and form a string
# containing the decrypted message, print the message and save it to a file
message = ''
while 1:
    ctext = infd.readline().rstrip()
    if len(ctext) != 0:
        ptext = pow(int(ctext),d,n)
        message = message + chr(ptext)
    else:
        break
infd.close()
outfd.close()
print message

# Now write decrypted message to the file decrypted
defd = open("decrypted","w")
defd.write(message)
defd.close()


