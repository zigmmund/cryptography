# RSA asymmetric cryptographic algorithm
import math

def gcd(a, h):
	temp = 0
	while(1):
		temp = a % h
		if (temp == 0):
			return h
		a = h
		h = temp

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

p = 3
q = 11
n = p*q
e = 7
phi = (p-1)*(q-1)

while (e < phi):

	# e must be co-prime to phi and
	# smaller than phi.
	if(gcd(e, phi) == 1):
		break
	else:
		e = e+1

# Private key (d stands for decrypt)
d = mod_inverse(e, phi)


# Message to be encrypted
msg = 2.0

print("Message data = ", msg)

# Encryption c = (msg ^ e) % n
c = pow(msg, e)
c = math.fmod(c, n)
print("The encryption of m = 2 is", c)

# Decryption m = (c ^ d) % n
m = pow(c, d)
m = math.fmod(m, n)
print("The decryption of c = 29 is", m)
