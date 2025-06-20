import pandas as pd

movies1000_full = pd.read_csv('movies1000_full.csv')
movies2_also1000 = pd.read_csv('movies2_also1000.csv')

movies_2000 = pd.concat([movies1000_full, movies2_also1000], ignore_index=True)

print(movies_2000)

movies_2000.to_csv('movies_2000.csv', index = False)