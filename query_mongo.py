# find method for limiting the search
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb   = client["JatinG"]  
coll   = mydb["Trainings"]

query  = {'addr' : 'hapur'}

new_lim  = coll.find(query)

for i in new_lim:
    print(i)

# advanced querry 
# use modifiers as value in query object

# find docs where the address field start with the letter "H" .

query = {'addr' : {'$gt' : 'H'}}

new_querry = coll.find(query)

for i in new_querry:
    print(i)

print('-------------------------------------------->>>>>>>')

# ADVANCED QUERY USING REGEX
query = {'addr' : {'$regex' : '^G'}}
new_querry = coll.find(query)

for i in new_querry:
    print(i)
