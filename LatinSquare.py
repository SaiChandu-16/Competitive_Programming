# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    # Your code goes here...
    n = len(lst)
    rows = []
    for i in range(n):
        rows.append(set([]))
 
    cols = []
    for i in range(n):
        cols.append(set([]))
 
    invalid = 0
    for i in range(n):
        for j in range(n):
            rows[i].add(lst[i][j])
            cols[j].add(lst[i][j])
 
            if (lst[i][j] > n or lst[i][j] <= 0):
                invalid += 1
 
    numofrows = 0
    numofcols = 0
    for i in range(n):
        if (len(rows[i]) != n):
            numofrows += 1
 
        if (len(cols[i]) != n):
            numofcols += 1
 
    if (numofcols == 0 and numofrows == 0 and invalid == 0):
        return True
    else:
        return False

lst = [[1, 2],
       [2, 1]]
assert(isLatinSquare(lst) == True)

lst1 = [[1, 2, 3],
       [3, 1, 2],
       [2, 3, 1]]
assert(isLatinSquare(lst1) == True)

lst2 = [[1, 5, 6],
       [8, 1, 21],
       [9, 10, 12]]
assert(isLatinSquare(lst2) == False)

lst3 = [[1, 2, 3,4],
       [32, 1, 32,45],
       [2, 3, 1,47],
       [3,8,75,5]]
assert(isLatinSquare(lst3) == False)

print("All test cases passed...!")