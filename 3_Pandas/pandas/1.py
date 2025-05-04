import numpy as np
import pandas as pd


df1 = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], columns = ['a', 'b', 'c']) # Creating a dataframe from a list
print( "Dataframe 1 from list: ")
print(df1) # Printing the dataframe
df2 = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6], 'c': [7,8,9]}) # Creating a dataframe from a dictionary
print( "Dataframe 2 from dictionary: ")
print(df2)
# Creating a dataframe from an array
arr = np.random.randint(0, 10, ( 3, 3 )) # Creating a 3x3 array with random integers between 0 and 10
df3 = pd.DataFrame(arr, columns = ['a', 'b', 'c']) # Creating a dataframe from the array
print( "Dataframe 3 from array: ")
print(df3)

# Performing selection
print( "First row of dataframe 3: ")
print(df3.iloc[0]) # Accessing the first row
print( "First column of dataframe 3: ")
print(df3.iloc[:, 0]) # Accessing the first column
# Accessing columns by name
print( "Column b of dataframe 3: ")
print(df3['b']) # Accessing column 'b'
# Performing filtering
print( "Elements greater than 5 in dataframe 3: ")
print(df3[df3 > 5]) # Accessing elements greater than 5
