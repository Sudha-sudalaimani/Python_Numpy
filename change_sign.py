#25.	How to negate a boolean, or to change the sign of a float inplace?

bool_arr = np.array([True, False, True])
bool_arr = ~bool_arr   # Negates True → False, False → True
print(bool_arr)
float_arr = np.array([1.5, -2.0, 3.0])
float_arr *= -1   # multiply all elements by -1
print(float_arr)
