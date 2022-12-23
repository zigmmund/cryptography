# Calculate Euler's Totient Function 
  
# Function to return 
# gcd of a and b 
def gcd(a, b): 
  
    if (a == 0): 
        return b 
    return gcd(b % a, a) 
  
# A simple method to evaluate Euler Totient Function a
def phi(n): 
  
    result = 1
    for i in range(2, n): 
        if (gcd(i, n) == 1): 
            result+=1
    return result 
  
# Random examples 
print(phi(10))
print(phi(15))
print(phi(33))
