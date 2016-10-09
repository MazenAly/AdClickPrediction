import pandas as pd
import numpy as np
import csv
import time


TITLE = ['SearchID', 'AdID', 'Position', 'HistCTR', 'IsClick',
         'SearchDate', 'IPID', 'UserID', 'IsUserLoggedOn', 'SearchQuery',
         'SearchLocationID', 'SearchCategoryID', 'SearchParams',  'SearchLocationLevel' , 'SearchRegionID' , 'SearchCityID' ,    'SearchCategoryLevel' , 'SearchParentCategoryID' ,  'SearchSubcategoryID' ,
         'UserAgentID', 'UserAgentOSID', 'UserDeviceID', 'UserAgentFamilyID' , 
     'AdCategoryID' ,'Params' , 'Price',  'Title' ,  'AdCategoryLevel', 'AdParentCategoryID' , 'AdSubcategoryID']

SOURCE = 'data/train.csv'
DEST = 'data/train_sampled.csv'

output_file = open(DEST, "w", encoding="utf8")
open_file_object = csv.writer(output_file)
open_file_object.writerow(TITLE)
output_file.close()

chunksize = 5000000
clicked_count = 0 
for chunk in pd.read_csv(SOURCE, sep=',', usecols=TITLE , chunksize=chunksize , index_col=0 ):
	chunck_clicked = chunk[chunk.IsClick == 1]
	chunck_clicked_rows_count = chunck_clicked.shape[0]
	clicked_count = clicked_count + chunck_clicked_rows_count
	chunck_not_clicked = chunk[chunk.IsClick == 0].sample(chunck_clicked_rows_count*2)
	chunck_clicked.append(chunck_not_clicked).to_csv(DEST , mode = 'a' , header=False) 
	print(clicked_count)

