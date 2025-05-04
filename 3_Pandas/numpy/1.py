import numpy as np

# Creating arrays
arr_int = np.random.randint(0, 10, 5) # Generate an array of 5 random integers between 0 and 10
arr_flo = np.random.rand(5) # Generate an array of 5 random floats
arr_boo = np.random.rand(5) > 0.5 # Generate an array of 5 random booleans

# Accessing elements
print(arr_int[0]) # Access the first element of the array
print(arr_flo[1:4]) # Access the second to fourth elements of the array

# Showing arrays
print( "Array of integers: ", arr_int)
print( "Array of floats: ", arr_flo)
print( "Array of booleans: ", arr_boo)
# basic arthimitic between arrays
print(arr_int+5) # addition between int array and int scaler
print(arr_int + arr_flo) # addition between int and float
print(arr_int * arr_flo) # multiplication between int and float
print( arr_flo - arr_boo) # subtraction between int and bool
