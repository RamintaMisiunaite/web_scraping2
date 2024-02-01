import pandas as pd 

file_name = '2024-02-01-12-51-08.csv'
df = pd.read_csv(f'headlines/{file_name}', names=['headline', 'posted_time', 'theme'])

# convert data types 
df = df.convert_dtypes()
df['posted_time'] = df['posted_time'].apply(pd.Timestamp) 

print(df.dtypes)