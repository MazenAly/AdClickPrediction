# -*- coding: utf-8 -*-
import sqlite3
import csv
import time

#add 'IsClick' and remove 'ID' in case of merging train data
TITLE = ['ID', 'SearchID', 'AdID', 'Position', 'ObjectType', 'HistCTR',
         'SearchDate', 'IPID', 'UserID', 'IsUserLoggedOn', 'SearchQuery',
         'SearchLocationID', 'SearchCategoryID', 'SearchParams',  'SearchLocationLevel' , 'SearchRegionID' , 'SearchCityID' ,    'SearchCategoryLevel' , 'SearchParentCategoryID' ,  'SearchSubcategoryID' ,
         'UserAgentID', 'UserAgentOSID', 'UserDeviceID', 'UserAgentFamilyID' , 
    'AdLocationID' , 'AdCategoryID' ,'Params' , 'Price',  'Title',  'IsContext',  'AdLocationLevel',   'AdRegionID'  , 'AdCityID' ,  'AdCategoryLevel', 'AdParentCategoryID' , 'AdSubcategoryID']


conn = sqlite3.connect("/media/mazen/E4CCCF65CCCF311A/Avito/data/database.sqlite")
SearchStream = conn.cursor()
SearchInfo = conn.cursor()
UserInfo = conn.cursor()
AdsInfo = conn.cursor()


SearchStream.execute("select * from testSearchStream")

output_file = open("data/test.csv", "w", encoding="utf8")
open_file_object = csv.writer(output_file)
open_file_object.writerow(TITLE)

search = SearchStream.fetchmany(1000000)
cnt = len(search)
rows = []
while search:
    k =0 
    start_time = time.time()
    for i in search:
        k = k+1
	#skip non contextual ads (in test merging), in train merging the condition is i[5] == null
        if not i[4] == 3:  
            continue
        search_id = i[0]
        ad_id = i[1]
        SearchInfo.execute("select * from SearchInfo_ where SearchID="+str(search_id))
        AdsInfo.execute("select * from AdsInfo_ where AdID="+str(ad_id))
        search_info = SearchInfo.fetchone()
        ads_info = AdsInfo.fetchone()
        if search_info is None:
            if ads_info is None:
                ads_info = [0 for k in range(13)]
            search_info = [0 for k in range(15)]
            user_info = [0 for k in range(5)]
            row = list(i) + list(search_info[1:]) + list(user_info[1:]) + list(ads_info[1:])
            rows.append(row)
            continue
        user_id = search_info[3]
        UserInfo.execute("select * from UserInfo where UserID="+str(user_id))
        user_info = UserInfo.fetchone()
        if ads_info is None:
            ads_info = [0 for k in range(13)]
        if user_info is None:
            user_info = [0 for k in range(5)]
        row = list(i) + list(search_info[1:]) + list(user_info[1:]) +  list(ads_info[1:]) 
        rows.append(row)
        if (k % 10000 == 0 ):
        	print(time.time() - start_time , "sec")
        	start_time = time.time()
    print(cnt)
    open_file_object.writerows(rows)
    rows = []
    search = SearchStream.fetchmany(1000000)
    cnt += len(search)

output_file.close()
