import numpy as np
import pandas as pd

arr = np.random.randint(0, 10, ( 6, 3 ))
df = pd.DataFrame(arr, columns = ['a', 'b', 'c'])
print( "Dataframe: ")
print( df)
# Pandas uses aggregation functions from numpy

# Performing aggregation with mean
print( "Mean: ")
print(df.mean())

# Performing Statistical analysis
print( "Standard Deviation: ")
print(df.std())
print( "Variance: ")
print(df.var())

# Performing transformation
print( "Z score standarization: ")
print( (df - df.mean())/ df.std() )

