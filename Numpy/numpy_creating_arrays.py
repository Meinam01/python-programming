import numpy as np

numbers_list_array = np.array([10,20,30,40,50,])
print(numbers_list_array)
print(type(numbers_list_array))

#tuple
numbers_tuple_array = np.array([10,20,30,40,50,])
print(numbers_tuple_array)

#0 - d
simple_value_array = np.array(99)
print(simple_value_array)

#1 - d
student_scores_array = np.array([80,85,90,95,100,])
print(student_scores_array)
#2 - d
matrix_table_array = np.array([[1,2,3],[4,5,6]])
print(matrix_table_array)
print(matrix_table_array.shape)
#3 - d
cube_data_array = np.array([[[1,2,3],[4,5,6]],
                            [[1,2,3],[4,5,6]]])
print(cube_data_array)