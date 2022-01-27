import json
import os

from pymongo import MongoClient

from models import CatFood

client = MongoClient()
db = client.get_database("cat")
col = db.get_collection("CatFood_test005")
result = dict()

for data in col.find({}, {"_id": False, "updated_at": False}):
    item = CatFood()
    item.site = data.get("site")
    item.url = data.get("url")
    item.brand = data.get("brand")
    item.title = data.get("title")
    item.image = data.get("image")
    item.analysis = data.get("analysis")
    item.ingredients = data.get("ingredients")
    item.calorie = data.get("calorie")
    if item.brand + ".json" in result.keys():
        result[item.brand + ".json"].append(item.to_mongo())
    else:
        result[item.brand + ".json"] = [item.to_mongo()]

for key, value in result.items():
    file_path = os.path.join(os.curdir, "data", key)
    with open(file=file_path, mode="w", encoding="utf8", newline="") as input_file:
        json.dump(value, input_file, allow_nan=False, ensure_ascii=False, indent=4)
