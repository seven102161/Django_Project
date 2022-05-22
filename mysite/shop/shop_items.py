import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["magic_shop"]
mycol = mydb["foods"]

myquery = { "name": "美味饺子" }
product = mycol.find(myquery,{"_id": 0})
print(product[0])