import uuid
import bson
import json
import mongoengine as me


class CatFood(me.Document):
    def __str__(self):
        return json.dumps({
            "site": self.site,
            "url": self.url,
            "brand": self.brand,
            "title": self.title,
            "image": self.image,
            "analysis": self.analysis,
            "ingredients": self.ingredients,
            "calorie": self.calorie,
            "additives": self.additives,
        }, ensure_ascii=False)

    site = me.URLField(default="")
    url = me.URLField(default="")
    brand = me.StringField(default="")
    title = me.StringField(default="")
    image = me.URLField(default="")
    analysis = me.StringField(default="")
    ingredients = me.StringField(default="")
    calorie = me.StringField(default="")
    additives = me.StringField(default="")
