import sys
import random

def main():
	create_keys(sys.argv[1], sys.argv[2], sys.argv[3])

#Key generation function
def create_keys(seed, public_file, private_file):

	random.seed(seed)

	#Generate q and p
	is_prime = 0;
	while not is_prime:
		q = random.randint(1073741824, 2147483647)
		if q % 12 == 5:
			p = 2 * q + 1
			if isPrime(p, 40):
				is_prime = 1 

	#Public and private key
	d = random.randint(1, p - 2)	
	e1 = 2
	e2 = pow(e1, d, p)

	#Print public and private key to shell
	print("PUBLIC KEY: (", p, ", ", e1, ", ", e2, ")", sep = "")	
	print("PRIVATE KEY: (", p, ", ", e1, ", ", d, ")", sep = "")	

	#Print public key to external
	with open(public_file, 'w') as public:
		public.write(str(p))
		public.write(" ")
		public.write(str(e1))
		public.write(" ")
		public.write(str(e2))
	public.close()	
	
	#Print private key to external
	with open(private_file, 'w') as private:
		private.write(str(p))
		private.write(" ")
		private.write(str(e1))
		private.write(" ")
		private.write(str(d))
	private.close()	

#--------------CODE_DERIVED_FROM_GEEKS_FOR_GEEKS---------------#
def power(x, y, p):
     
    # Initialize result
    res = 1; 
     
    # Update x if it is more than or
    # equal to p
    x = x % p; 
    while (y > 0):
         
        # If y is odd, multiply
        # x with result
        if (y & 1):
            res = (res * x) % p;
 
        # y must be even now
        y = y>>1; # y = y/2
        x = (x * x) % p;
     
    return res;
 
# This function is called
# for all k trials. It returns
# false if n is composite and 
# returns false if n is
# probably prime. d is an odd 
# number such that d*2<sup>r</sup> = n-1
# for some r >= 1
def miillerTest(d, n):
     
    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    a = 2 + random.randint(1, n - 4);
 
    # Compute a^d % n
    x = power(a, d, n);
 
    if (x == 1 or x == n - 1):
        return True;
 
    # Keep squaring x while one 
    # of the following doesn't 
    # happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
 
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;
 
    # Return composite
    return False;
 
# It returns false if n is 
# composite and returns true if n
# is probably prime. k is an 
# input parameter that determines
# accuracy level. Higher value of 
# k indicates more accuracy.
def isPrime( n, k):
     
    # Corner cases
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;
 
    # Find r such that n = 
    # 2^d * r + 1 for some r >= 1
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
 
    # Iterate given nber of 'k' times
    for i in range(k):
        if (miillerTest(d, n) == False):
            return False;
 
    return True;
#------------------------------------------------------------#

if (__name__ == '__main__'):
	main()
