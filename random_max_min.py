#8.	Write a NumPy program to create a 10×10 array with random values and find the minimum and maximum values.
n=np.random.random((3,3,3))
max_n=n.max()
min_n=n.min()
print("array:",n)
print("Maximum:",max_n)
print("Minimun:",max_n)
