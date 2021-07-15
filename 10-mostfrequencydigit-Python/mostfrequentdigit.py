# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.
from statistics import mode

def mostfrequentdigit(n):
	# your code goes here
	res = [int(x) for x in str(n)]
	return mode(res)
