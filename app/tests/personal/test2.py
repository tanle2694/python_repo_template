import pandas as pd

result = pd.DataFrame()

sample = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# print(pd.concat([result, sample], axis=1))
# print(pd.concat([result, sample], axis=1, ignore_index=True))
sample2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
print(type(sample), sample.columns)
print(sample2)
print(pd.concat([sample, sample2], axis=1))
