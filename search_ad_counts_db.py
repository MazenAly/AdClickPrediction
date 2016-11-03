import sqlite3
import time

conn = sqlite3.connect("/media/mazen/E4CCCF65CCCF311A/Avito/data/database.sqlite")

conn.execute('drop table if exists search_di')
conn.execute('CREATE TABLE "search_di" ("SearchID" INTEGER NOT NULL PRIMARY KEY , "reg" INTEGER , "highlighted" INTEGER , "context" INTEGER )')

db = conn.cursor()
search_di = {}

def flush_dict():
	for key, value in search_di.items():
		db.execute('insert or replace into search_di values (?  , ? , ? , ?)', (key  , value[1]  , value[2]   , value[3]  ) )
	search_di.clear()
	conn.commit()

SearchStream = conn.cursor()
SearchStream.execute("select * from trainSearchStream")
search = SearchStream.fetchmany(1000000)
cnt = len(search)
while search:
	k =0 
	start_time = time.time()
	for x in search:
		k += 1
		if not search_di.has_key(x[0]):
			search_di[x[0]] = {1: 0 , 2: 0 , 3: 0 }
		if x[3]==1:
			search_di[x[0]][1] += 1 
		elif x[3]==2:
			search_di[x[0]][2] += 1 
		else:
			search_di[x[0]][3] += 1
	if (k % 10000 == 0 ):
		print(time.time() - start_time , "sec")
		start_time = time.time()
	print(cnt, "rows processed")
	search = SearchStream.fetchmany(1000000)
	cnt += len(search)
	flush_dict()

