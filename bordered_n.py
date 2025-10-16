#9.	Write a NumPy program to add a border (filled with 0's) around an existing array.
n=np.ones((3,3))
bordered_n=np.pad(n,pad_width=1,mode="constant",constant_values=1)
print(bordered_n)
