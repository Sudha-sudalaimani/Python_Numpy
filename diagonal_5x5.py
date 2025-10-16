#10.	Write a NumPy program to create a 5×5 matrix with values 1, 2, 3, 4 just below the diagonal.
n=[1,2,3,4]
dig=np.diag(n,k=-1)
print(dig)
