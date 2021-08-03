# isPalindromicPrime() Write a function isPalindromicPrime that takes a value n as a parameter and returns True if the given n is a palindrome and prime and False otherwise.
# assert (isPalindromicPrime(2) == True)
# assert (isPalindromicPrime(10) == False)
# assert (isPalindromicPrime(104) == False)
# assert (isPalindromicPrime(235) == False)
# assert (isPalindromicPrime(131) == True)
# assert (isPalindromicPrime(900) == False)
# assert (isPalindromicPrime(101) == True)
# assert (isPalindromicPrime(383) == True)
# assert (isPalindromicPrime(373) == True)
# assert (isPalindromicPrime(121) == False)
# print("All test cases passed... :-)")

def isPalindrome(n):
    a = str(n)
    if(len(a) == 1):
        return True
    elif(a == a[::-1]):
        return True
    return False

def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

def isPalindromicPrime(n):
    if(isPalindrome(n) and isPrime(n)):
        return True
    return False

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