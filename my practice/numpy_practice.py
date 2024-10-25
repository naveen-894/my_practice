import numpy as np

arr = np.array([1,2,3])
print(arr)
print(arr.shape)
print(arr.dtype)
# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
arr1 = arr.copy()
print(arr1)
# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
x = arr.view()
x[1] = 666
print(arr)
# The shape of an array is the number of elements in each dimension.
print(x)
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('shape of array :', arr.shape)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 55, 3], [4, 5, 6]]])

print(a.ndim, 'kjhgh')
print(b.ndim)
print(c.ndim)
print(d.ndim)

print(d[0])

arr = np.array([1, 2, 3, 4], dtype='i')

print(arr)
print(arr.dtype)


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 55, 3], [4, 5, 6]]])

np.random.shuffle(arr)

print(arr)


import time
import numpy as np

# Creating a large list and NumPy array
size = 1000000
my_list = list(range(size))
my_array = np.arange(size)

# Timing list multiplication
start = time.time()
my_list = [x * 2 for x in my_list]
end = time.time()
print(f"List time: {end - start} seconds")

# Timing NumPy array multiplication
start = time.time()
my_array = my_array * 2
end = time.time()
print(f"NumPy time: {end - start} seconds")




"""Array Creation and Basic Operations:

Create a NumPy array of integers from 1 to 100.
Reshape it into a 10x10 matrix.
Find the mean, median, and standard deviation of the matrix.
Find the sum of all elements in the matrix."""

arr = np.arange(1, 101)

new_matrix = arr.reshape(10, 10)
print(arr)
print(new_matrix)
print(np.mean(new_matrix))
print(np.median(new_matrix))
print(np.std(new_matrix))


"""
Element-wise Operations:

Create two random 5x5 matrices using np.random.rand().
Perform element-wise addition, subtraction, multiplication, and division on these matrices.
"""

# arr1 = np.random.rand(5, 5)
# arr2 = np.random.rand(5, 5)
arr1 = np.random.randint(1, 100, size=(5, 5))
arr2 = np.random.randint(1, 100, size=(5, 5))

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 / arr2)
print(arr1 * arr2)




"""Slicing and Indexing:

Create a 7x7 matrix filled with random integers between 10 and 100.
Extract:
The first three rows.
The last two columns.
The elements on the diagonal."""

arr1 = np.random.randint(1, 100, size=(7, 6))

print(arr1)
print(arr1[:3])
print(arr1[-3:])
print(np.diag(arr1))


"""
Broadcasting:

Create a 4x4 matrix with values from 1 to 16.
Add a 1D NumPy array of size 4 (values: [1, 2, 3, 4]) to each row of the matrix using broadcasting.
"""

matrix = np.random.randint(1,16, size=(4,4))
arr = np.array([1,2,3,4])

print(matrix)
print(matrix+arr)


"""
Generate a 1D NumPy array with 1000 random values following a normal distribution.
Calculate the mean, variance, and standard deviation of the array.
Find how many elements are greater than 1.
"""

arr = np.random.randn(1000)

print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))
print(np.sum(arr>1))

"""
Basic Array Creation and Manipulation
Array Creation: Create a 1D array of numbers from 10 to 50. Then, reverse the array.
Zeroes and Ones: Create a 3x3 array of all ones, and multiply every element by 5.
Replace Values: Generate a 1D array of 20 random integers between 1 and 10. Replace all values greater than 5 with the number -1.
"""
arr = np.arange(10, 50)
print(arr[:-1])
arr1 = np.random.randint(1, 50, size=(3, 3))
print(arr1)
# print(arr1*5)
arr1[arr1>5] = -1
print(arr1)

"""
Slicing and Indexing
Row and Column Extraction: Create a 4x4 matrix with values from 1 to 16. Extract the second row and third column from this matrix.
Selective Assignment: Create a 5x5 matrix of random integers from 1 to 100. Replace all values in the matrix that are less than 50 with zero.
"""
matrix = np.random.randint(1, 16, size=(4,4))
print(matrix)

print(matrix[1])
print(matrix[:, 2])

matrix = np.random.randint(1, 100, size=(5,5))
print(matrix)
matrix[matrix>50] = 0
print(matrix)


"""
Arithmetic Operations
Array Multiplication: Generate two 1D arrays of size 10 with random values. Perform element-wise multiplication and division.
Add Row to Matrix: Create a 3x4 matrix with values from 1 to 12. Then, add the row [10, 20, 30, 40] to each row in the matrix using broadcasting.
"""
arr = np.arange(1, 10, 8)
arr1 = np.arange(1, 10, 8)

print(arr * arr1)

arr1 = np.arange(1, 13).reshape(3,4)
arr2 = np.array([10, 20, 30, 40])
print(arr1)
arr1 + arr2

print(arr1 + arr2)