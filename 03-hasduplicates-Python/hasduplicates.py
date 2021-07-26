# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	

def read2DArray():
    a = []
    l = int(input())
    for i in range(l):
        s = input().split(" ")
        t = []
        for j in range(len(s)):
            t.append(int(s[j]))
        a.append(t)
    return a