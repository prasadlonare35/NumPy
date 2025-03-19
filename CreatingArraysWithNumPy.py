import numpy as np

arr1 = np.array([1,2,3,4,5])   # 1D
arr2 = np.array([[1,2,3],[4,5,6]])  # 2D
print(arr1)
print(arr2)

# Properties
print("----------------------")
print(arr2.shape)  # no of row, column
print(arr2.dtype)  # date type
print(arr2.ndim)   # no  of dimensions
print(arr2.size)   # total no of elements

# Special Arrays
print("----------------------")
print(np.zeros((3,3)))   # 3 x 3 matrix of zers
print("----------------------")
print(np.ones((2,4)))    # 2 x 4 matrix of ones
print("----------------------")
print(np.eye(3))         # 3 x 3 identity matrix
print("----------------------")
print(np.full((2,2),7))  # 2 x 2 matrix filled with 7
print("----------------------")
print(np.arange(1,10,2))   # 1 to 9 nos with step 2
print("----------------------")
print(np.linspace(0,10,5)) # 5 equally spaced nos 0 - 10
print("----------------------")

# Indexing & Slicing
print("----------------------")
print(arr1)
print(arr1[0])      # first elem
print(arr1[-1])     # last elem
print(arr1[1:4])    # 1 to 3 elem
print(arr1[:3])     # 1st 3 elem
print(arr1[::2])    # every second elem

matrix = np.array([[10,20,30],[40,50,60],[70,80,90]])
print("----------------------")
print(matrix)
print(matrix[0,1])    # 0th row 1st col  
print(matrix[0,:])    # 0th row
print(matrix[:,0])    # 0th col
print(matrix[0:2,1:3])   # submatrix

