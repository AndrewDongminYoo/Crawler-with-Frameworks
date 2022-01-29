import json
import os

from pymongo import MongoClient

from models import CatFood

client = MongoClient()
db = client.get_database("cat")
col = db.get_collection("CatFood_test006")
data_path = os.path.join(os.curdir, "data")
files = [x for x in os.listdir(data_path) if x != "__pycache__"]


def upload():
    for fp in files:
        file_path = os.path.join(data_path, fp)
        with open(file=file_path, mode="r", encoding="utf8") as old:
            obj = json.load(old)
            for data in obj:
                cat_food = CatFood().from_dict(obj=data)
                col.update_one({"url": cat_food["url"]}, {"$set": cat_food.to_mongo()}, upsert=True)


def download():
    result = dict()
    for data in col.find({}, {"_id": False, "updated_at": False}):
        cat_food = CatFood().from_dict(obj=data)
        if cat_food.brand + ".json" in result.keys():
            result[cat_food.brand + ".json"].append(cat_food.to_dict())
        else:
            result[cat_food.brand + ".json"] = [cat_food.to_dict()]

    for key, value in result.items():
        file_path = os.path.join(data_path, key)
        with open(file=file_path, mode="w", encoding="utf8", newline="") as input_file:
            json.dump(value, input_file, allow_nan=False, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # upload()
    download()
