import numpy as np

# Create an array 'x'
x = [4, 2, 6, 8, 10]
arr = np.array(x)
print("Array 'arr':", arr)

# Correct the 'y' list
y = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]
arr = np.array(y)
print("Array 'arr' from 'y':\n", arr)

# Create arrays filled with zeros and ones
arr_zeros = np.zeros((4, 4))
arr_ones = np.ones((4, 4))
print("Array of zeros:\n", arr_zeros)
print("Array of ones:\n", arr_ones)

# Generate a random array
arr_random = np.random.random([3, 2])
print("Random array:\n", arr_random)

# Create an array using arange
arr_arange = np.arange(1, 30, 3)
print("Array using arange:\n", arr_arange)

# Create an array using linspace
arr_linspace = np.linspace(0, 20, 5)
print("Array using linspace:\n", arr_linspace)

# Perform arithmetic operations on arrays 'a' and 'b'
a = np.array([100, 200, 300])
b = np.array([[20, 25, 30], [40, 50, 60]])
print("Sum of arrays 'a' and 'b':\n", np.add(a, b))
print("Subtraction of arrays 'a' and 'b':\n", np.subtract(a, b))
print("Element-wise multiplication of arrays 'a' and 'b':\n", np.multiply(a, b))

# Calculate mean, standard deviation, and variance of array 'a'
print("Mean of array 'a' elements:", np.mean(a))
print("Standard deviation of array 'a' elements:", np.std(a))
print("Variance of array 'a' elements:", np.var(a))

# Fix the errors below
# 1. Correct the function name: np.arange instead of np.aran
# 2. Correct the reshape function: np.arange(1, 40, 4).reshape(5, 2)
arr_reshaped = np.arange(1, 40, 4).reshape(5, 2)
print("Reshaped array:\n", arr_reshaped)

# Transpose array 'arr1'
arr1 = np.array([[1, 2, 3, 4], [2, 3, 7, 11]])
arr1_transposed = arr1.transpose()
print("Transposed array 'arr1':\n", arr1_transposed)

# Correct the 'arr2' definition
arr2 = np.array([[1, 3, 5, 7], [2, 4, 6, 8]])
print("Array 'arr2':\n", arr2)

# Concatenate arrays 'arr1' and 'arr2'
concatenated_array = np.concatenate((arr1, arr2))
print("Concatenated array:\n", concatenated_array)
