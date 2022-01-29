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
        self.site = obj.get("site") or None
        self.url = obj.get("url") or None
        self.brand = obj.get("brand") or None
        self.title = obj.get("title") or None
        self.image = obj.get("image") or None
        self.analysis = obj.get("analysis") or None
        self.ingredients = obj.get("ingredients") or None
        self.calorie = obj.get("calorie") or None
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
