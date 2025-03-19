import numpy as np
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[6,5,4],[3,2,1]])

# mathematical operations
print(arr1+arr2)        
print("-----------------------------------------------")
print(arr1-arr2) 
print("-----------------------------------------------")
print(arr1*arr2) 
print("-----------------------------------------------")
print(arr1/arr2) 
print("-----------------------------------------------")
print(arr1%arr2) 
print("-----------------------------------------------")
print(np.sqrt(arr1))
print("-----------------------------------------------")
print(np.exp(arr1))
print("-----------------------------------------------")
print(np.log(arr1))

# Broadcasting
print("-----------------------------------------------")
scalar = 10
print(arr1 + scalar)    # add 10 to every elements

# aggregate function
print("-----------------------------------------------")
print(np.sum(arr2))
print(np.mean(arr2))
print(np.median(arr2))
print(np.std(arr2))
print(np.min(arr2))
print(np.max(arr2))
print(np.argmax(arr2))   # index of max
print(np.argmin(arr2))   # index of min
print("-----------------------------------------------")
print(arr1)
print(np.sum(arr1,axis=0))   # sum of each col
print(np.sum(arr1,axis=1))   # sum of each row

# random numbers
print("-----------------------------------------------")
print(np.random.rand(3))     # 3 random no
print(np.random.randint(1,10,size=(3,3)))     # 3 x 3 matrix of random no
print(np.random.randn(3,3))     # 3 x 3 matrix with normal distribution
print(np.random.seed(42))     # set seed

# reshaping and flattering
print("-----------------------------------------------")
arr = np.array([1,2,3,4,5,6])
reshaped = arr.reshape((2,3))       # convert to 2 x 3 matrix
print(reshaped)
print(reshaped.flatten())           # convert back to 1D array