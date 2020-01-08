'''
The column names mentioned in the dataset does not have any implecation about 
the data contained in that column. Like, '01' named column stores information
about number of gold medals received by a country, '02' for 'Silver' and '03'
for 'Bronze'. This program cleans the dataset and replaces the column names
with more suitable names. 
'''
import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (taking first 3 characters from that)

df = df.drop('Totals')
df.head()
