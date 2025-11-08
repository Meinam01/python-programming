import numpy as np

integer_array = np.array([1,2,3,4,])
print(integer_array)
print(integer_array.dtype)

float_array = np.array([1.1,2.2,3.3])
print(float_array)
print(float_array.dtype)

names_array = np.array(["tomba","choaba","thoiba"])
print(names_array)
print(names_array.dtype)

bool_array = np.array([True,False,True])
print(bool_array)
print(bool_array.dtype)

convert_float_array = np.array([10,20,30],dtype = np.float64)
print(convert_float_array)
print(convert_float_array.dtype)

print(integer_array.itemsize)
print(float_array.itemsize)