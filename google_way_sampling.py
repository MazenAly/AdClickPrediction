# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import csv
import time
import pickle	

TITLE = ['SearchID', 'AdID', 'Position', 'HistCTR', 'IsClick',
         'SearchDate', 'IPID', 'UserID', 'IsUserLoggedOn', 'SearchQuery',
         'SearchLocationID', 'SearchCategoryID', 'SearchParams',  'SearchLocationLevel' , 'SearchRegionID' , 'SearchCityID' ,    'SearchCategoryLevel' , 'SearchParentCategoryID' ,  'SearchSubcategoryID' ,
         'UserAgentID', 'UserAgentOSID', 'UserDeviceID', 'UserAgentFamilyID' , 
     'AdCategoryID' ,'Params' , 'Price',  'Title' ,  'AdCategoryLevel', 'AdParentCategoryID' , 'AdSubcategoryID', 'weight']

SOURCE = 'data/train.csv'
DEST = 'data/train_sampled3.csv'

output_file = open(DEST, "w")
open_file_object = csv.writer(output_file)
open_file_object.writerow(TITLE)
output_file.close()

with open('data/search_ids_clicked_list.pickle', 'rb') as handle:
  search_ids_clicked_list = pickle.load(handle)

chunksize = 5000000
pd.options.mode.chained_assignment = None 
for chunk in pd.read_csv(SOURCE, sep=',', chunksize=chunksize , index_col=None ):
	col_name =chunk.columns[0]
	chunk=chunk.rename(columns = {col_name:'SearchID'})
	clicked_queries = chunk[chunk.SearchID.isin(search_ids_clicked_list)]
	clicked_queries['weight'] = 1 
	non_clicked_queries = chunk[~chunk.SearchID.isin(search_ids_clicked_list)]
	non_clicked_queries_sampled = non_clicked_queries.sample(non_clicked_queries.shape[0]/50)
	non_clicked_queries_sampled['weight'] = 50
	clicked_queries.append(non_clicked_queries_sampled).to_csv(DEST , mode = 'a' , header=False , index=False) 
	print(clicked_queries.shape[0] , " ", non_clicked_queries_sampled.shape[0] )

