import numpy as np
import pandas as pd


df1 = pd.DataFrame([[1,np.nan,3], [4,5,6], [7,8,np.nan]], columns = ['a', 'b', 'c']) # Creating a dataframe from a list
print( "Dataframe 1: ")
print(df1) # Printing the dataframe

# Creating a dataframe from an array
arr = np.array([[1,7,4]]).T # Creating a 1x3 array with random integers between 0 and 10
df2 = pd.DataFrame(arr, columns = ['d']) # Creating a dataframe from the array
print( "Dataframe 2: ")
print(df2)



# Dropping rows with missing values
print( "Dataframe 1 with missing values dropped by row: ")
print(df1.dropna())

# Dropping columns with missing values
print( "Dataframe 1 with missing values dropped by column: ")
print(df1.dropna(axis = 1))

# Filling missing values
print( "Dataframe 1 with missing values filled: ")
df1 = df1.fillna( df1.mean())
print(df1) # Filling missing values with 0

# Joining dataframes
df_join = df1.join(df2, how = 'left', lsuffix = '_left', rsuffix = '_right') # Joining df1 and df2 on the index
print( "Joined dataframe: ")
print(df_join)

# Merging dataframes
df_merge = pd.merge(df1, df2, how = 'left', left_on = 'a', right_on = 'd') # Merging df1 and df2 on column 'a' and 'd'
# As you can see, df2 is rearranged to match df1 on column d
print( "Merged dataframe: ")
print(df_merge)

