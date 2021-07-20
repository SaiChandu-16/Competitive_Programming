# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import math
def nthpowerfulnumber(n):
	# Your code goes here
	x = 0
	y = 0
	while(x<=n):
		y = y+1
		if(powerfulNo(y)):
			x = x+1
	return y


def powerfulNo(a):
	while(a%2 == 0):
		c = 0
		while(a%2==0):
			a = a//2
			c = c+1
		if(c == 1):
			return False
	for power in range(3,int(math.sqrt(a))+1,2):
		c = 0
		while(a%power == 0):
			a = a//power
			c = c+1
		if(c == 1):
			return False
	return (a==1)