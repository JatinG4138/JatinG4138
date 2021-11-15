import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb   = client["JatinG"]  
coll   = mydb["Trainings"]

# sort function will sort all the name fields
sor    = coll.find().sort('name')

# iterate through sor object
for i in sor:
    print(i)

# to start sort in descending order we have to give one more parameter
#  -1 for descending order and 1 for ascending order 1
query  = coll.find().sort('name',-1)

for i in query:
    print(i)