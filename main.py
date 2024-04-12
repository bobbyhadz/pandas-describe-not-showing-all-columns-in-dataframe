# Pandas: Describe not showing all columns in DataFrame

import pandas as pd


df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'experience': [1, 1, 5, 7],
    'salary': [175.1, 180.2, 190.3, 205.4],
})

print(df.describe())

print('-' * 50)

print(df.describe(include='all'))