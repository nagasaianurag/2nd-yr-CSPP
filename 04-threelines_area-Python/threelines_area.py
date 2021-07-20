# Write the function fun_threelines_area(d1, d2, d3) 
# that takes length of 3 sides
# find the area of a triangle(return an int) given its side lengths.

import math

def fun_threelines_area(a, b, c):
	sum = (a+b+c)/2
	distance = sum*(sum-a)*(sum-b)*(sum-c)
	area = int(math.sqrt(distance))
	return area
	