# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def fun_nth_additive_prime(x):
	x=abs(x)
	count=0
	start=2
	while(count<=x):
		if (isprime(start) and digitsum(start)):
			count+=1
		start+=1    
	return start-1  
            
def isprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n):
            if n % i == 0:
                return False
        return True
 
def digitsum(x):        
    sum=0
    while (x>0):
        sum+=(x%10)
        x=int(x/10)         
    return isprime(sum)
