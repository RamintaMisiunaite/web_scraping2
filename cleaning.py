
import pandas as pd

file_name = '2024-02-01-12-51-08.csv'
df = pd.read_csv(f'headlines/{file_name}', names=['headline', 'posted_time', 'theme'])

# drop duplicate values keeping the first occurence
df = df.drop_duplicates(keep='first')

df.to_csv(f'headlines/cleaned_{file_name}', index=False)