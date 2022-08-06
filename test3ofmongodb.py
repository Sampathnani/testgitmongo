import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://Sampath3759:Sampath3759@cluster0.pvqkix8.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name": "sampath",
    "surname": "nani",
    "email": "sampath@gmail.com"
}
data={
  "InsuranceCompanies":  {
    "Top Insurance Companies":[
      {
        "No": "1",
        "Name": "Berkshire Hathaway ( BRK.A)",
        "Market Capitalization": "$655 billion"
      }
    ],
  "source": "investopedia.com",
  "Time":"May 2021"
  }
}
db1=client['mongotest'];
coll=db1['test'];
##coll.insert_one(d);
coll.insert_one(data)