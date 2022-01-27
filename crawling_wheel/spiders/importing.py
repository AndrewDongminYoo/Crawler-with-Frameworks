import json
import os

from selenium.webdriver import Chrome

from crawling_wheel.models import CatFood

PATH = "C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data"
CUR_PATH = os.path.realpath(os.path.pardir)
DATA_PATH = os.path.join(CUR_PATH, "data")
if not DATA_PATH:
    os.mkdir(DATA_PATH)

import pymongo

client = pymongo.MongoClient()
db = client.get_database("cat")
col = db.get_collection("CatFood_test001")


def make_item(element):
    result = CatFood()
    result.url = element.get("url")
    result.site = element.get("site")
    result.brand = element.get("brand")
    result.title = element.get("title")
    result.image = element.get("image")
    result.ingredients = element.get("ingredients")
    result.analysis = element.get("analysis")
    result.calorie = element.get("calorie")
    result.additives = element.get("additives")
    col.update_one({"title": result.title}, {"$set": result.to_mongo()}, upsert=True)
    return result.to_mongo()


with Chrome() as driver:
    for uri in os.listdir(PATH):
        _file_input = os.path.join(PATH, uri)
        with open(file=_file_input, mode="r", encoding="utf8") as input_file:
            obj = json.load(input_file)
            _file_output = os.path.join(DATA_PATH, uri)
            if type(obj) is list:
                items = [make_item(elem) for elem in obj]
                with open(file=_file_output, mode="w+", encoding="utf8") as output_file:
                    json.dump(items, output_file, allow_nan=False, ensure_ascii=False, indent=4)
            elif type(obj) is dict:
                item = make_item(obj)
                with open(file=_file_output, mode="w+", encoding="utf8") as output_file:
                    json.dump(item, output_file, allow_nan=False, ensure_ascii=False, indent=4)
