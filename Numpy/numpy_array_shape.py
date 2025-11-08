import numpy as np

one_d_array = np.array([5,10,15,20])
print(one_d_array)
print(one_d_array.shape)

two_d_array = np.array([
    [1,2],
    [3,4],
    [5,6]
])
print(two_d_array)
print(two_d_array.shape)

three_d_array = np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])
print(three_d_array)
print(three_d_array.shape)