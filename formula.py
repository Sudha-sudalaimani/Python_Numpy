#17.	Given two NumPy arrays A and B, compute
#(A+B) ∗ (−A/2) (A + B) * (-A/2) (A+B)∗(−A/2) 
#in place without creating a new array.
import numpy as np
A = np.array([2, 4, 6])
B = np.array([1, 3, 5])

# In-place computation
A += B          # Step 1: A = A + B   (modify A itself)
A *= (-A / 2)   # Step 2: A = A * (-A / 2)   (still in place)

print(A)
