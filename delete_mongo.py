import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb   = client["JatinG"]  
coll   = mydb["Trainings"]

query  = {"_id" : 11} 

coll.delete_one(query)

for i in coll.find():
    print(i)

# print(f)

query  = {'name' : {'$regex' : '^S'}}
newDB  = coll.delete_many(query)

print(newDB)
print(newDB.deleted_count,"DOCUMENT DELETED")
# for i in coll.find(newDB):



# DELETE ALL DOCUMENTS
query = coll.delete_many({})
print(query.deleted_count,"DOCUMENT DELETED")
