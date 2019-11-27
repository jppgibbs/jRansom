# Finds the primitive roots between 10 and 50 for primes between 1000 and 9999
import primes
import sys
p = input('Input your prime number: ')
if (p < 1000 or p >9999):
    print 'Only finds primitive roots for primes on interval [1000,9999]'
    sys.exit(0)
if (primes.isprime(p) == 0):
    print '%i is NOT prime' % (p)
    sys.exit(0)
primroots =[]
ordp = range(1,p)
for a in range(10,51):
    orda = []
    for i in range(1,p):
        orda.append(pow(a,i,p))
    orda.sort()
    if orda == ordp:
        primroots.append(a)
print 'The primitive roots of %i on the interval [10,50] are %s' % (p,primroots)        
