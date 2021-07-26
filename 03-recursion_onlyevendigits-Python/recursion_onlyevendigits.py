# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(l, result=[]): 
	if len(l)==0:
		return []
	else:
		even=evenDigit(l[0])
		invert=revnum(even)
		result.append(invert)
		fun_recursion_onlyevendigits(l[1:])
	return result

def evenDigit(n, result=0):
	if n<10:
		if n%2==0:
			result=(result*10+(n%10))
		return result
	elif n%2==0:
		result=result*10+(n%10)
	result=evenDigit(n//10,result)
	return result

def revnum(n, result=0):
	if n<10:
		return (result*10+(n%10))
	else:
		result=(result*10+(n%10))
		return revnum(n//10,result)