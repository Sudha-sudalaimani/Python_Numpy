#18.Write a NumPy program to extract the integer part of a random array of positive numbers using four different methods.
import numpy as np
arr = np.random.random(5) * 10  
print("Original Array:", arr)
int_part1 = np.floor(arr)
int_part2 = np.trunc(arr)
int_part3 = arr.astype(int)
int_part4 = np.fix(arr)
print(int_part1)
print( int_part2)
print( int_part3)
print( int_part4)

