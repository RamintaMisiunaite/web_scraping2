import pandas as pd 

file_name = '2024-02-01-12-51-08.csv'
df = pd.read_csv(f'headlines/{file_name}', names=['headline', 'posted_time', 'theme'])

# convert data types 
df = df.convert_dtypes()
df['posted_time'] = df['posted_time'].apply(pd.Timestamp) 


# avg headline lenght

# df['headline_length'] = len(df['headline'])
# print(df[['headline', 'headline_length']])

df['words'] = df['headline'].str.lower().str.split()

for w in df['words']:
    print(len(w))
# ar yra kada daugiausiai postina laiko intervalas 
# kokiose temose daugiausiai 
# zodziu analyze headline
