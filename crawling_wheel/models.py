import uuid
import mongoengine as me


class Company(me.Document):
    id = me.LongField()
    logo_image = me.StringField()
    korean_name = me.StringField()
    english_name = me.StringField()
    country = me.StringField()
    social_score = me.FloatField()


class CatFood(me.Document):
    id = me.LongField()
    manufacturer = me.ReferenceField(Company)
    importer = me.ReferenceField(Company)
    texture = me.EnumField("Texture")
    packaging = me.FloatField()
    energy_100 = me.FloatField()
    ingredients = me.ListField(me.ReferenceField("Ingredient"))





