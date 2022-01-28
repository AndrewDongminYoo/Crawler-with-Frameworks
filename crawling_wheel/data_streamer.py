import json
import os

from crawling_wheel.google_get_img import search_google_img_get_first, get_host_name

data_path = os.path.join(os.curdir, "data")
files = [x for x in os.listdir(data_path) if x != "__pycache__"]
# print(files.index("SmartHeartGold 9 care.json"))
for fp in files:
    file_path = os.path.join(data_path, fp)
    with open(file=file_path, mode="r", encoding="utf8") as old:
        obj = json.load(old)
        for cat_food in obj:
            cat_food['image'] = search_google_img_get_first(cat_food)
            cat_food['site'] = get_host_name(cat_food.get("url"))
    with open(file=file_path, mode="w", encoding="utf8") as new:
        json.dump(obj=obj, fp=new, ensure_ascii=False, allow_nan=False, indent=4)
