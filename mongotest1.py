import pymongo
client = pymongo.MongoClient("mongodb+srv://<username>:Sampath3759@cluster0.pvqkix8.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name": "sampath",
    "surname": "nani",
    "email": "sampath@gmail.com"
}
db1=client['mongotest'];
coll=db1['test'];
coll.insert_one(d);