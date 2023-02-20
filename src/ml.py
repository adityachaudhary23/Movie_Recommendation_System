import numpy as np
import pandas as pd
import difflib

movies_data=pd.read_csv('/movies_metadata.csv.zip',usecols=['original_title','id','imdb_id','vote_average'])
movies=pd.DataFrame(movies_data)
movies.drop(movies.index[1000:45466],inplace=True)

movies.drop_duplicates(subset='imdb_id',keep=False,inplace=True)
mov=movies.pivot(index='imdb_id',columns='id',values='vote_average').fillna(0)

from scipy.sparse import csr_matrix
m=csr_matrix(mov.values)

from sklearn.neighbors import NearestNeighbors
model=NearestNeighbors(metric='cosine',algorithm='brute',n_neighbors=20)
print(model.fit(m))
!pip install fuzzywuzzy
from fuzzywuzzy import process
def recommender(name,data,n):
  i=process.extractOne(name,movies['original_title'])[2]
  d,ind=model.kneighbors(data[i],n_neighbors=n)
  print(movies['original_title'][i])
  print('Searching for recommendation.....')
  print(d,ind)
  for j in ind:
    print(movies['original_title'][j].where(j!=i))
recommender('Toy Story',m,10)