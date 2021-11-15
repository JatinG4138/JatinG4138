import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb   = client["JatinG"]  
coll   = mydb["Trainings"]

print(mydb.list_collection_names())

# prnt single data which comes in first occurence.
f = coll.find_one()

print(f)

f = coll.find()

print(f)

# print all db data
for i in coll.find():
    print(i)

# print only some fields
for i in coll.find({"_id" : 0 , "name" : 1 , "addr" : 1}):
    print(i) 

# id can be 0 and those fields which you want to show put their values to 1
# You get an error if you specify both 0 and 1 values in the same object 
# (except if one of the fields is the _id field)

