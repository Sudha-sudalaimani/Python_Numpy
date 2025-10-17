import numpy as np
#27.	Given a NumPy array, write a program to get the n largest values.
arr = np.array([1, 3, 2, 5]) #1,2,3,5
n = 2
largest = np.sort(arr)[-n:]
print(largest)
