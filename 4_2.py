# Python3 program to find multiplicative modulo
# inverse using Extended Euclid algorithm.

# Global Variables
x, y = 0, 1

# Function for extended Euclidean Algorithm

def gcdex(a, b):
	global x, y

	# Base Case
	if (a == 0):
		x = 0
		y = 1
		return b

	# To store results of recursive call
	gcd = gcdex(b % a, a)
	x1 = x
	y1 = y

	# Update x and y using results of recursive
	# call
	x = y1 - (b // a) * x1
	y = x1

	return gcd


def inverse_element(A, N):

	g = gcdex(A, N)
	if (g != 1):
		print("Inverse doesn't exist")

	else:

		# m is added to handle negative x
		res = (x % N + N) % N
		print("Modular multiplicative inverse is ", res)


# Driver Code
if __name__ == "__main__":
	A = 5
	N = 18

	# Function call
	inverse_element(A, N)
