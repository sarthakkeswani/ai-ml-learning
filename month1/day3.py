import numpy as np

#1D Array
arr1 = np.array ([10,20,30])
print('1D Array: ', arr1)

#2D Array
arr2= np.array ([[1,2], [3,4]])
print('2D Array: ',arr2)

print(np.zeros((2,3)))
print(np.ones((3,2)))
print(np.eye(3)) #3x3 Matrix
print(np.arange(0,10,2))
print(np.linspace(0,2,5))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b) 

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print("Dot product:", np.dot(v1, v2))  # 1*4 + 2*5 + 3*6 = 32