import shelve

t = shelve.open("photo_db.dat")
for t1 in t.keys():
    del t[t1]
 
t["pipeline"] = []
t.close()

t = shelve.open("tags_db.dat")
for t1 in t.keys():
    del t[t1]
 
t.close()

