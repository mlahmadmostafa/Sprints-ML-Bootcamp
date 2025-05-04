import numpy as np
# Create a 10 element array of random integers between 0 and 10
arr = np.random.randint(0, 10, 10)
print( "Array 1: ", arr)
# Reshape the array to a 2x5 matrix
arr = arr.reshape( 2, 5 )
print( "Reshaped array: ", arr)
# Stack 2 arrays
arr2 = np.array([1, 2, 3, 4, 5])
print( "Array 2: ", arr2)
arr_stacked = np.vstack((arr, arr2)) # vertical stack
print( "Stacked array: ", arr_stacked)
# Splitting an array
arr_split = np.split(arr_stacked, 3)
print( "Split array: ", arr_split)
# Apply boolen indexing
print("Elements greater than 5: ", arr_stacked[arr_stacked > 5])
