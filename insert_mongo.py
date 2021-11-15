import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

# creating a database
mydb = client['JatinG']

# list all databases
print(client.list_database_names())

# created all db list object
dblist = client.list_database_names()

# check that db is created or not
# if "JatinG" in dblist:
#   print("The database exists.")

# else:
#     print('Not YEt..') 

coll = mydb["Trainings"]

# dictionary for inserting sing
data_dict = {
    'name' : 'JatinG',
    'addr' : 'Gzb',
    'phone': 999999
}
data_dict1 = [
    {   
        '_id'  :  1,
        'name' : 'Srishti',
        'addr' : 'hapur',
        'phone': 85469
    },
    {   '_id'  :  11,
        'name' : 'Srishti',
        'addr' : 'hapur',
        'phone': 85469
    },
    {
        'name' : 'arunesh',
        'addr' : 'gonda',
        'phone': 85469
    }
]

coll_list = mydb.list_collection_names()

if "Trainings" in coll_list:

    print("Exists")

# insert_data = coll.insert_one(data_dict,data_dict1)
# insert_one will only store 1 dictionary which comes first 
insert_data = coll.insert_one(data_dict)

# get single
print(insert_data.inserted_id)

# insert_data = coll.insert_many(data_dict1)

# print(insert_data.inserted_ids)

# to insert multiple documents with specified ids we use """_id"""
# to get id of single document we use (x.inserted_id)
# to get id of multiple document we use (x.inserted_ids)

