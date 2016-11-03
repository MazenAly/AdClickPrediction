import pandas as pd
import numpy as np
import pickle


search_di = {}
def count_search_ads(x):
    if not search_di.has_key(x['SearchID']):
        search_di[x['SearchID']] = {1: 0 , 2: 0 , 3: 0 }
    if x['ObjectType']==1:
        search_di[x['SearchID']][1] += 1 
    elif x['ObjectType']==2:
        search_di[x['SearchID']][2] += 1 
    else:
        search_di[x['SearchID']][3] += 1


#read the dataframe by chunk and apply the counting function
SOURCE2 = "data/trainSearchStream.tsv"
for chunk in pd.read_csv(SOURCE2, sep='\t' , chunksize=10000000):
    print(len(search_di))
    chunk.apply(count_search_ads , axis =1 )



with open('../data/search_di_train.pickle', 'wb') as handle:
  pickle.dump(search_di, handle)
