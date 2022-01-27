import uuid
import bson
import mongoengine as me


class CatFood(me.Document):
    site = me.URLField()
    url = me.URLField()
    brand = me.StringField()
    title = me.StringField()
    image = me.URLField()
    analysis = me.StringField()
    ingredients = me.StringField()
    calorie = me.StringField()
    additives = me.StringField()
