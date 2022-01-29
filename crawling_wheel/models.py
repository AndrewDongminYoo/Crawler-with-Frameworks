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
        }, ensure_ascii=False)

    def from_dict(self, obj):
        self.site = obj.get("site")
        self.url = obj.get("url")
        self.brand = obj.get("brand")
        self.title = obj.get("title")
        self.image = obj.get("image")
        self.analysis = obj.get("analysis")
        self.ingredients = obj.get("ingredients")
        self.calorie = obj.get("calorie")
        return self

    def to_dict(self, *args, **kwargs):
        return super().to_mongo(*args, **kwargs)

    site = me.URLField(default="")
    url = me.URLField(default="")
    brand = me.StringField(default="")
    title = me.StringField(default="")
    image = me.URLField(default="")
    analysis = me.StringField(default="")
    ingredients = me.StringField(default="")
    calorie = me.StringField(default="")
