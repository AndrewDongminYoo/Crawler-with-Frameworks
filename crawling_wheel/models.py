import uuid
import bson
import mongoengine as me


class CatFood(me.Document):
    url = me.URLField()
    brand = me.StringField()
    title = me.StringField()
    analysis = me.StringField()
    ingredients = me.StringField()
    calorie = me.StringField()
    additives = me.StringField()
