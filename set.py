# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]
import itertools
def limitedPowerSet(n, k):
    # Your code goes here...
    a = set(())
    lst = [{}]
    for i in range(1, n+1):
        a.add(i)
    for i in range(1, len(a)+1):
        x = list(map(set, itertools.combinations(a,i)))
        for j in range(len(x)):
            if len(lst) != k:
                lst.append(x[j])
            else:
                return lst

assert(limitedPowerSet(6, 12) == [ {}, {1}, {2}, {3}, {4}, {5}, {6}, {1, 2}, {1, 3}, {1, 4}, {1, 5}, {1, 6}])
assert(limitedPowerSet(7, 8) == [ {}, {1}, {2}, {3}, {4}, {5}, {6}, {7} ])
assert(limitedPowerSet(5, 7) == [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ])

print("All test cases passed...!")