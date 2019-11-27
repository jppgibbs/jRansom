# RSA demo

import primes
import sys
p = 3			# one prime number
q = 19			# another prime 
n = p*q                 # the product of the primes
phi = (p-1)*(q-1)	# the totient

# Try a sensible value for the encryption exponent
e = 5
# Check to see that this is OK
if primes.gcd(phi,e) != 1:
    print 'e = %i was not a good choice' % e
    exit(0)

# Find the value of the decryption exponent
d=primes.invmod(phi,e)	
# Check that this is OK - should not have to do this
if d*e%phi != 1:
    print '(d*e) mod (phi) != 1 - something really wrong here!!!'
    sys.exit(0)

# Print out the prime numbers, n, the totient and the encryption and decryption exponents
print 'p = %i, q = %i, n = %i, phi = %i, e = %i, d = %i\n' % (p,q,n,phi,e,d)

# Encryption and decryption using the pow function to carry out modulo exponentiation
ptext = 53              # NOTE: 53 decimal is the decimal ASCII value for the CHARACTER 5		
ctext = pow(ptext,e,n)	# encrypt the integer 53
print 'The ciphertext of %i is %i' % (ptext, ctext)
ptext = pow(ctext,d,n)	# decrypt the encryption of the integer 53
print 'The plaintext of the ciphertext %i is %i\n' % (ctext,ptext)

# Encryption and decryption using the ** and % operators to carry out
# modulo exponentiationsys - this is not as efficient as using pow()
ctext = ptext**e%n
print 'The ciphertext of %i is %i' % (ptext, ctext)
ptext = ctext**d%n
print 'The plaintext of the ciphertext %i is %i\n' % (ctext,ptext)

#sys.exit(0) # COMMENT OUT THIS LINE AFTER YOU HAVE COMPLETED PARTS 1 TO 3
            # OF EXERCISE 9

# Since n = 57 integers up to 56 can be encrypted
# Generation of a look-up table for the encryption/decryption of integers
# from 0 to 56
print 'ciphertext\tplaintext'
for ptext in range(0,n):
    ctext = pow(ptext,e,n)
    print '%i\t\t%i' % (ctext,ptext)

# The generation of the table as a dictionary
table = {}
for ptext in range(0,n):
    ctext = pow(ptext,e,n)
    table[ctext] = ptext
print '\nDictionary for ciphertext to plaintext conversion\n%s\n' % (table)

# Example of use of dictionary
# If you have a ciphertext message that has a value of 16 the plaintext
# can be found simply by using 16 as the key in the table
print 'The plaintext of the ciphertext %i is %i\n' % (16,table[16])
