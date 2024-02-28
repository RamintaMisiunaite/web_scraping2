import pandas as pd 

file_name = '2024-02-01-12-51-08.csv'
df = pd.read_csv(f'headlines/{file_name}', names=['headline', 'posted_time', 'theme'])

# convert data types 
df = df.convert_dtypes()
df['posted_time'] = df['posted_time'].apply(pd.Timestamp) 


df['words'] = df['headline'].str.lower().str.split()


# avg headline lenght
df['headline_word_count'] = df['headline'].str.count(' ') + 1

print('Average headline length: ' + str(df.loc[:, 'headline_word_count'].mean()))


# kokiose temose daugiausiai 
print(df['theme'].value_counts())

# ar yra kada daugiausiai postina laiko intervalas 

# zodziu analyze headline
    

