import pandas as pd
import numpy as np

data = {
'Name': ['Tom', 'Tom', 'Tom', 'Tom'],
'Age': [1, 3, 2, 4,],
'Height': [75.2, 78, 61.4, 68.1]
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)

df['Test'] = df['Age'].astype('str') + df['Name']

print(df)
-------------------------
import lxml
import requests
import pandas as pd

url = 'https://en.m.wikipedia.org/wiki/New_York_City'
html = requests.get(url).content
df_list = pd.read_html(html)
print(len(df_list))
print(df_list)

# get column names containing a specific string, s
#df.columns[df.columns.str.contains(s)]

import this
for i in df_list:
    if not i.filter(regex='Historical').columns.empty:
        print(i)
-------------------
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
print(df, end='\n\n\n')

# Renaming columns
df = df.rename(columns={df.columns[-1]: 'poop'})
print(df, end='\n\n\n')

df = df[['poop', 'A']]
print(df)
