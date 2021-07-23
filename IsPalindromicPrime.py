# Write a function isPalindromicPrime that takes a value n as a parameter and returns True if the given n is a palindrome and prime and False otherwise.

def isPalindromicPrime(a):
    if (isPalindrome(a) and isPrime(a)):
        return True
    else:
        return False

def isPalindrome(n):
    n=str(n)
    return n[::-1]==n

def isPrime(n):
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

assert (isPalindromicPrime(2) == True)
assert (isPalindromicPrime(10) == False)
assert (isPalindromicPrime(104) == False)
assert (isPalindromicPrime(235) == False)
assert (isPalindromicPrime(131) == True)
assert (isPalindromicPrime(900) == False)
assert (isPalindromicPrime(101) == True)
assert (isPalindromicPrime(383) == True)
assert (isPalindromicPrime(373) == True)
assert (isPalindromicPrime(121) == False)
print("All test cases passed... :-)")