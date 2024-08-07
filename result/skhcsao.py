import numpy
import numpy as np
import pandas as pd

my_index = ['A', 'B', 'C']
my_columns = ['이름', '나이', '성별']
my_data = numpy.array([['Alice', 'Bob', 'Hong'],
                       [25,30,26],
                       ['남','여','남']]).transpose()
print(my_data)
df = pd.DataFrame(my_data, index=my_index, columns=my_columns)
# print(df[['이름','이름']])

print(df,"\n",df.loc["A"])