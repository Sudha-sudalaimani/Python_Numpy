#11.	Write a NumPy program to create an 8×8 matrix and fill it with a checkerboard pattern (alternating 0's and 1's).
chessboard=np.zeros((8,8))

chessboard[1::2,::2]=1
chessboard[::2,1::2]=1
print(chessboard)
