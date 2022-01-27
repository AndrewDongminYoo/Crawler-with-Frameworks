import os
import json

import selenium.webdriver
from selenium.webdriver import Chrome
import requests
from bs4 import BeautifulSoup

PATH = "C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data"
FILE_LIST = []

for uri in os.listdir(PATH):
    if uri.endswith("json"):
        FILE_LIST.append(os.path.join(PATH, uri))

FILE_LIST = [
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\A La CARTE.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Aatas Cat.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\AATU.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Absolute Holistic.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\ACANA.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Addiction.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Adirondack.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\ADVANCE.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Against The Grain.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\AlmoNature.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Ancestry.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Animonda.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\AnnaMaet.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Artemis.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Aujou by RAWZ.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Avoderm.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\BEST BREED.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\BlackHawk.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Blackwood Pet Food.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Blue Buffalo.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Bonachibo.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\BOREAL.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Bravery Pet Food.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Canada Fresh.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Canagan.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Canidae Pet Foods.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Cardinal Fussie Cat.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Carna4.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Caru.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Catz finefood.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Celtic Connection Holistic Pet Food.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Chicken Soup for the Soul.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Companion Pets Classic.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Diamond Pet Foods Premium Edge.json',
             # "C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Dr. Clauder's Best Choice.json",
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Dr.Link.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Earthborn.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Economy ROYAL.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Entoma.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Essential The Jaguar.json',
             # "C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Evanger's GrainFree.json",
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Evolve.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Farmina Vet Life Feline.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Feline Natural.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\First Choice Canada.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\FirstMate.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Fish4Cats.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Forza10 USA.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\GATHER.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Go! Solutions.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Gosbi.json',
             # "C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Grandma mae's.json",
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Hagen Catit Dinner.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Halo pets.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Healthy Shores Canada.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Hi-tek Naturals.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Hills.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Husse.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Instinct.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\iti Pet Food.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Josera.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Kongo.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\KOOKUT.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Leonardo Catfood.json',
             # "C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Lily's Kitchen.json",
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Little BigPaw.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Lotus.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Maria Pet Food.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Marp.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Me-O.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\MEOW Cat Food.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\MeowMix.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Mera Finest.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Merrick.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Miamor (German).json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Micho.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Mito.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Monge.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Natural Balance.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Natural Greatness.json',
             # "C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Nature's Logic.json",
             # "C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Nature's Protection.json",
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Naturliebe FairCat.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Naturliebe HappyCat.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Naturo.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\North Paw.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Northwest Naturals.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\NOW FRESH.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Nulo Freestyle.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\NutraGold.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Nutram Canada.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Nutrience.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\NutriSource.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Nutro.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Openfarm Korea.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Organix.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Orijen Cat.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Oven-Baked Traditional.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\PRIMAL PET FOODS.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\PRO PAC Ultimates.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Pro-Nutrition PureLife.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Pronature Canada.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\PureLuxe.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Rawz.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Rex Catfood.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Royal_Canin.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Sanabelle.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Schesir.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Sheba.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Smack Raw Hydrate Cat Food.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\SmartHeartGold 9 care.json',
             # 'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\SolidGold Petfood.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Specific.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Stella and Chewys.json',
             "C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Steve's Real Food.json",
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Supreme Source.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Taste of the Wild.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Tender and True.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Terra Felis.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Thrive complete.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\TIKI CATS.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\TOMOJO Pet Food.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\TOTAL ALIMENTOS EQUILIBRIO.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Trovet.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\TRULINE.json',
             "C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Tuffy's Petfoods Dinnertime.json",
             "C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Tuffy's Purevita.json",
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\TUSCAN NATURAL.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Verus.json',
             "C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Vet's Complete Life.json",
             "C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Vet's Kitchen.json",
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Vigor and Sage.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Vintage Cat food.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Vitakraft Cat Food.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Vital Essentials.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Wellness.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Weruva Catfood.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Whiskas.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Wishbone.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\Wysong.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\ZEAL Canada.json',
             'C:\\Users\\ydm27\\PycharmProjects\\REPORT\\utils\\data\\ZiwiPeak.json']

import pymongo

client = pymongo.MongoClient()
db = client.get_database("cat")
col = db.get_collection("CatFood_test001")


def get_title_and_url_brand_name(webdriver: selenium.webdriver.chrome, url):
    webdriver.get(url)
    return webdriver.title
    # from crawling_wheel.models import CatFood
    # cat_food_item = CatFood()
    # cat_food_item.url = url
    # cat_food_item.title = webdriver.title
    # print(webdriver.title)
    # col.update_one({"title": cat_food_item.title}, {"$set": cat_food_item.to_mongo()}, upsert=True)


with Chrome() as driver:
    for file in FILE_LIST:
        with open(file=file, mode="r", encoding="utf8") as input_file:
            obj = json.load(input_file)
            if type(obj) is list:
                for item in obj:
                    if type(item) is dict:
                        title = get_title_and_url_brand_name(driver, item["url"])
                        if item["title"] != title:
                            print(title)
                            item["title"] = title
            # else:
            #     title = get_title_and_url_brand_name(driver, obj["url"])
            #     if title != obj["title"]:
            #         print(title)
            #         obj['title'] = title
        with open(file=file, mode="w", encoding="utf8") as output_file:
            json.dump(obj, output_file, allow_nan=False, ensure_ascii=False, indent=4)
