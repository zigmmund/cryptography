# Extended Euclidean Algorithm
def gcdex(a, b):
	# Base Case
	if a == 0 :
		return b,0,1
			
	gcd,x1,y1 = gcdex(b%a, a)
	
	# Update x and y using results of recursive
	# call
	x = y1 - (b//a) * x1
	y = x1
	
	return gcd,x,y
	

# Driver code
a, b = 612,342
g, x, y = gcdex(a, b)
print("gcd(", a , "," , b, ") = ", g)
