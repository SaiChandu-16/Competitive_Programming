"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    # Your code goes here
    result = input_array
    while(len(input_array) >= 1):
        size = len(input_array)
        if(size % 2 != 0):
            midpoint = input_array[size//2]
        else:
            midpoint = input_array[(size//2)-1]
        if(value == midpoint):
            return result.index(midpoint)
        elif(value < midpoint):
            input_array = input_array[:(input_array.index(midpoint))]
        elif(value > midpoint):
            input_array = input_array[(input_array.index(midpoint)+1):]
    return -1
