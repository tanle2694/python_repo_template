import pandas as pd
import numpy as np

# Define the number of rows and columns
num_rows = 1
num_cols = 4
data1 = np.random.rand(1, num_cols)
df1 = pd.DataFrame(data1, columns=[f'col{i}' for i in range(1, num_cols+1)])

num_rows = 5
num_cols = 4
data2 = np.random.rand(num_rows, num_cols)
df2 = pd.DataFrame(data2, columns=[f'col{i}' for i in range(1, num_cols+1)])



df_ignore_index = pd.concat([df1, df2], ignore_index=True)
print("With ignore_index=True")
print(df_ignore_index)
print("---------")

df_no_ignore_index = pd.concat([df1, df2])

print("With ignore_index default")
print(df_no_ignore_index)

# Generate random numbers for the third DataFrame
data3 = np.random.rand(6, num_cols)

# Create the third pandas DataFrame
df3 = pd.DataFrame(data3, columns=[f'col_x_{i}' for i in range(1, num_cols+1)])
print(df3)
# # Concatenate df_no_ignore_index and df3
df_final = pd.concat([df_ignore_index, df3], axis=1, ignore_index=True)
#
# print("After concat")
print(df_final)
# df_final = pd.concat([pd.DataFrame(), df3], axis=1)
# print(df_final)
