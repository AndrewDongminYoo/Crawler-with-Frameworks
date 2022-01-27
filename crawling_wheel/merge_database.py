from pymongo import MongoClient

client = MongoClient()
db = client.get_database("cat")
Cat_Food = db.get_collection("CatFood")
TestDATA = db.get_collection("CatFood_test001")
NextDATA = db.get_collection("CatFood_test002")
NestDATA = db.get_collection("CatFood_test003")
#
for cat in Cat_Food.find({}, {"_id": False}):
    NextDATA.update_one({"title": cat.get("title")}, {"$set": cat}, upsert=True)

for cat in TestDATA.find({}, {"_id": False}):
    NextDATA.update_one({"url": cat.get("url")}, {"$set": cat}, upsert=True)

# for gato in NextDATA.find({}, {"_id": False}):
#     cat = CatFood()
#     for key, value in gato.items():
#         cat[key] = value
#     NextDATA.update_one({"title": cat.title}, {"$set": cat.to_mongo()}, upsert=True)
