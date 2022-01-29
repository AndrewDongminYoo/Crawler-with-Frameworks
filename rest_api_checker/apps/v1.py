from flask import Blueprint, request, jsonify
from pymongo import MongoClient

from crawling_wheel.google_get_img import search_google_image_with_title
from crawling_wheel.models import CatFood

app = Blueprint('v1', __name__, url_prefix="/v1")
client = MongoClient()
db = client.get_database("cat")
col = db.get_collection("CatFood_test006")


@app.route('/cat-foods', methods=['GET', 'PATCH'])
def call_cat_foods():
    args = request.args
    if request.method == "GET":
        page = int(args.get("page") or 1)
        per_page = 60
        cat_foods = col.find({}, {"_id": False}).skip((page - 1) * per_page).limit(per_page)
        return jsonify(list(cat_foods))
    elif request.method == "PATCH":
        title = args.get("title")
        target = col.find_one({"title": title})
        cat_food = CatFood().from_dict(target)
        cat_food.image = search_google_image_with_title(title)
        col.update_one({"title": cat_food.title}, {"$set": cat_food.to_mongo()})
        return cat_food.to_json()
