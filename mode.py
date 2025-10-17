#26.	Given a NumPy array, write a program to find the most frequent (mode) value in the array.
arr = np.array([1,2,2,3])
mode = np.bincount(arr).max()
print(mode)
