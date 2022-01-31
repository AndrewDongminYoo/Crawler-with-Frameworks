import re

from pymongo import MongoClient

client = MongoClient()
db = client.get_database("cat")
col = db.get_collection("CatFood_test006")


# def main():
#     for item in col.find({}, {"_id": False}):
#         if item.get("additives"):
#             additives = item.get("additives")
#             if type(item["ingredients"]) is list:
#                 if type(item["additives"]) is list:
#                     item["ingredients"].extend(additives)
#                 else:
#                     item["ingredients"].append(additives)
#             else:
#                 if type(item["additives"]) is list:
#                     item["ingredients"] += ",".join(additives)
#                 else:
#                     item["ingredients"] += additives
#         col.update_one({"url": item["url"]}, {"$unset": {"additives": None}})


def string_fixer(string: str):
    string = re.sub("([\d.]+)%(\w)", " \\1%, \\2", string)
    string = string \
        .replace("(min.)", "") \
        .replace("(max.)", "") \
        .replace("(Max.)", "") \
        .replace("(Min.)", "") \
        .replace("Energy", "Energy:") \
        .replace("%.", "%") \
        .replace(" / ", "/") \
        .replace(" (2.47 oz) ", "/")
    string = re.sub("(\d+)[,’]{1}(\d{1,2})", " \\1.\\2", string)
    string = re.sub("(\d+)[.]{1}(\d{3})", "\\1,\\2", string)
    string = re.sub("([a-zA-Z])(\d)", "\\1: \\2", string)
    string = re.sub("\((\s*\d+\.\d+%)\)", "\\1,", string)
    string = re.sub("\((\s*\d+%)\)", "\\1,", string)
    string = re.sub("%(\w+)", "%, \\1", string)
    string = re.sub("kg(\w+)", "kg, \\1", string)
    string = re.sub("\s{2,}", " ", string)
    string = re.sub("^\s", "", string)
    string = string.replace(" imum", "") \
        .replace(" – ", ": ") \
        .replace("Analytical constituents:", "") \
        .replace("( min)", "") \
        .replace("Analytical Constituents", "") \
        .replace(",,", ",") \
        .replace(" – ", ": ")
    string = string. \
        replace("Proteína Bruta", "Crude Protein"). \
        replace("Grasa bruta", "Crude Fat"). \
        replace("Fibra bruta", "Crude Fiber"). \
        replace("Ceniza bruta", "Crude Ash"). \
        replace("Humedad", "Moisture")
    return string


def list_splitter(string: str):
    string = string.replace("Ingredients:", "")
    string = re.sub("^\s+", "", string)
    if ", " not in string:
        return string.split(". ")
    if "(" in string:
        bracket = 0
        for c in range(len(string)):
            if string[c] == "," and bracket == 0:
                string = string[:c] + ";" + string[c + 1:]
            elif string[c] == "(":
                bracket += 1
            elif string[c] == ")":
                bracket -= 1
        return string.split("; ")
    return string.split(", ")


def hello_peter(string: str):
    str_replace = {
        "\n": "",
        "\t": "",
        "Calorie Content (calculated) ": "",
        " (metabolizable energy) on an as fed basis.": "",
        "This food contains ": "",
        "The calculated metabolizable energy is ": "",
        "Calorie Control: ": "",
        "PLEASE STORE FOOD IN A DRY, COOL PLACE": "",
        "(CALCULATED): This food contains ": "",
        "Kcals per 100g": "kcal/100g",
        "cals": "cal",
        " 1 cup=4.4 oz. (125 g)": "",
        "Calorie Content (ME, calculated) ": "",
        "Calorie Content (ME Calculated as Fed): ": "",
        "*Not recognized as an essential nutrient by the AAFCO Cat Food Nutrient Profiles. ": "",
        "CALCULATED (ME): ": "",
        "(metabolizable energy, calculated): ": "",
        "Metabolisable Energy kJ	": "",
        "Calorie Content (Calculated): ": "",
        "Calories (ME) ": "",
        "Calorie Content ME (calculated) – ": "",
        "(calculated): ME = ": "",
        "PureLUXE Healthy Weight Cat Food is formulated to meet the nutrient levels established by the AAFCO Cat Food Nutrient Profiles for all life stages.": "",
        " 1 cup = approximately 4oz of food.": "",
        "Using the calculations provided by the AAFCO, ": "",
        " has approximately": "",
        "which is an average amount of calories compared to the average of the other dry cat foods in the CatFoodDB.": "",
        "1 measured cup of Pronto = approx. ": "",
        "Calories ": "",
        "is ": "",
        " of 250 ml": "",
        "with calories distributed to support peak conditioning;": "",
        "METABOLIZABLE ENERGY: ": "",
        "Threonine	1.49 %": "",
        "Kittens and pregnant or nursing females may consume two to three times the recommended amount.": "",
        "Calculated ME: ": "",
        "(CALCULATED): ": "",
        "Metabolisable Energy ": "",
        "Energy": "",
        "ME: ": "",
        "Kcal": "kcal",
        " - ": " ",
        "100g in MJ": "kcal/100g",
        "Calorie Content ": "",
        " • 464 kcal/cup • 4 kcal/g (ME – calculated)": "",
        "Energy ": "",
        "387 kcal/369g  164kcal/156g  84kcal/80g  ": "",
        " ME [metabolizable energy] on an as fed bas[calculated]": "",
        " Per Can": "",
        "Umsetzbare Energie: ": "",
        "EM ": "",
        " ME": "",
        "Metabolic energy ": "",
        "Calorie Content........ ": "",
        "Calorie Content ME (calculated): ": "",
        "Energy content: metabolisable energy (according to FEDIAF, 2016) ": "",
        "Metabolisable energy (according to FEDIAF, 2016) ": "",
        " kcal per cup ME (metabolizable energy) on an as-fed bas(calculated).": "kcal/cup",
        "(metabolizable energy)(calculated).  Contains a source of live naturally occurring microorganisms": "",
        "kca1": "kcal",
        "KCAL/KG": "kcal/kg",
        ". can": "",
        "kcal /kg": "kcal/kg",
        " 1 cup=4.8 oz. (130 g)": "",
        "*Not recognized as an essential nutrient by the AAFCO Cat Food Nutrient Profiles": "",
        "Threonine1.49 %": "",
        " Note: The calories can vary slightly over time due to naturally occurring variation in ingredients, processing and analyses": "",
        "Metabolizable energy: ": "",
    }
    for _from, _to in str_replace.items():
        string = string.replace(_from, _to)
    regex_list = {
        "^ ": "",
        "\, \d\d.\d kcal\/2\.47oz": "",
        "\, \d\d\d kcal\/2\.47oz": "",
        "\, \d\d kcal\/2\.47oz": "",
        "(kcal\/2\.47 oz) (\d\d\.\d\d)": "\\2 \\1",
        "kcal\/kg \d\d\.\d kcal/2\.47 oz": "kcal/kg",
        "(kcal\/100g): (0),(\d\d)": "\\2.\\3 \\1",
        "\.$": "",
        "(kcal\/kg) (\d\,\d{3})": "\\2 \\1",
        "kcal\/kg\, \d\d kcal": "kcal/kg",
        "(\d{2})\,(\d{2})kcal\/100g": "\\1.\\2 kcal/100g",
        "(\d{2})\,(\d{2}) kcal\/100g": "\\1.\\2 kcal/100g",
        " \(ME\)$": "",
        "kcal\/lb \d{4} Mj\/lb \d\.\d{2} (\d{3} kcal\/cup)": "\\1",
        "\d{3} kcal\/ CUP (\d{4} kcal\/ kg)": "\\1",
        "ME per kg (\d{4} kcal\/kg)": "\\1",
        "Calories": "kcal",
        "\(kcal\/100g\): (\d{2})": "\\1 kcal/100g",
        "(\d{3})kcal per 100g": "\\1 kcal/100g",
        "kcal(\d{4}.\d{2} kcal\/kg)": "\\1",
        "ME \(calculated\)\: (\d{4} kcal\/kg) \| \d{3} kcal\/cup": "\\1",
        "^Meow Mix® [éa-zA-Z \.&®]+": "",
        "(\d{3,4} kcal\/kg)\; \d{2} kcal\/2\.75 oz cup": "\\1",
        "(\d+)kcal": "\\1 kcal",
        "kcal\/kg \d+ kcal\/cup": "kcal/kg",
        "ME kcal\/Tub ([\d\.]+)": "\\1 kcal/Tub",
        "(\d+\.\d kcal\/kg) [\d\.]+ kcal\/2\.47oz": "\\1",
        "^kcal\/2\.47 oz ([\d\.]+)$": "\\1 kcal/2.47oz",
        "^(\d{3,4} kcal\/)70 g \(2\.47 oz\) [\d\.0]+$": "\\1kg",
        " \| \d{3} kcal\/level scoop$": "",
        " \| \d{3} kcal \/level scoop$": "",
        "kcal \/ Kg kcal \/ Level Scoop\*\: \d+$": "kcal/kg",
        "^(\d+ kcal\/kg) \d+ kcal\/kg$": "\\1",
        "^3\.0 oz \d+ kcal KG (\d+ kcal)$": "\\1/kg",
        "^(\d*)\,(\d{3} kcal\/kg) or \d{3} kcal\/cup$": "\\1\\2",
        "^(\d*)\,(\d{3}) kcal\/cup or \d{3} kcal\/cup$": "\\1\\2 kcal/kg",
        "^(\d*)\,(\d{3} kcal\/kg) \– 531 kcal\/cup 1 cup\=4\.8 oz\. \(130 g\)$": "\\1\\2",
        "^(\d*)\,(\d{3} kcal\/kg) \– \d{3} kcal\/cup$": "\\1\\2",
        "^(\d{2} kcal\/2\.8 oz) \d{3} kcal\/5\.5 oz$": "\\1",
        "^(\d)\,(\d{3}) kcal\/kg$": "\\1\\2 kcal/kg",
        "\.\, \d{3} kcal\/cup$": "",
        "\, \d{3} kcal\/cup$": "",
        "^kJ (\d{4}) kcal \d{3}$": "\\1 kJ",
        "^kJ(\d{4})$": "\\1 KJ",
        "^kJ (\d{4})$": "\\1 KJ",
        "^(\d)\,(\d{3} kcal\/kg)\; \d{3} kcal\/5\.5 oz or \d{3} kcal\/3 oz$": "\\1\\2",
        "^(\d)\,(\d{3} kcal\/kg) or \d{3} kcal\/can$": "",
        "^(\d{4} kcal\/kg) \(\d{3} kcal\/cup\)$": "\\1",
        "^\d{3} kcal\/\"CUP (\d{4} kcal\/kg)$": "\\1",
        "^\d{3} kcal\/CUP (\d{4} kcal\/kg)$": "\\1",
        "^[a-zA-Z ]+ Formula (\d{3}) calories per 100g \(\d{3} calories\/ounce\)\, $": "\\1 kcal/100g",
        "^(\d{2,})\/oz 4 oz$": "\\1 kcal/oz",
        "(\d{2,})\/oz 1 ounce \= approx\. 3 \-4 nuggets$": "\\1 kcal/oz",
        "^(\d{3,4} kcal\/kg)\, [0-9\,]{3,5} kcal \/ cup$": "\\1",
        "^(\d{4} kcal\/kg) \(\d{3} kcal per 250ml\/130g cup\)  \d+\% from protein\, \d+\% from vegetables and fruit\, and \d+\% from fat$": "\\1",
        "^(\d)\,(\d{3})": "\\1\\2",
        "kcal\/ kg$": "kcal/kg",
        "^5\.5 oz\: ([\d\,]{3,5} kcal\/kg) or \d{3,} kcal\/can$": "\\1",
        "(\d+) oz": "\\1oz",
        "^kcal\/70 g \(2\.47oz\) ([\d\.]+)$": "\\1 /kcal/70g",
        "^kcal\/100g\: (\d)\,(\d)$": "\\1.\\2 MJ/100g",
        "^ME (\d{3} kcal\/kg)\, \d{3} kcal per pack$": "\\1",
        "^(\d+)\,(\d+) kcal\/ 100g$": "\\1.\\2 kcal/100g",
        "^(\d{4})\/kg$": "\\1 kcal/kg",
        "^kcal\/Kg (\d\,\d{3})$": "\\1 kcal/kg",
        "kcal\/Kg$": "kcal/kg",
        "^content\: metabolisable energy \(according to FEDIAF\, 2016\) ": "",
        "MJ/kg\. $": "MJ/kg",
        "^(\d{4} kcal) per kilogram or \d{3} kcal per cup \(metabolizable energy\) on an as\-fed bas\(calculated\)$": "\\1/kg",
        "^\(Calculated\) (\d{4} kcal\/kg) or 397 kcal\/cup$": "\\1",
        "^\/ 100g\: (\d+ kcal)$": "\\1/100g",
        "^ME \= (\d)\,(\d{3} kcal\/kg)": "\\1\\2",
        "^ME \= (\d\d{3} kcal\/kg)": "\\1",
        "^\(calculated\)\: (\d{3} kcal\/kg) \d+ kcal\/tub$": "\\1",
        "^ME \= (\d{3} kcal\/kg)\; \d{3} kcal\/5\.5oz$": "\\1",
        "^Metabolizable energy:$": "",
        "^(\d+)\,(\d{,2})": "\\1.\\2",
        "kcal \/ 100 g$": "kcal/100g",
        "^etabolizable energy: ": "",
        "kcal Per Cup$": "kcal/cup",
        "^(kcal\/100g) ([\d\.]+)$": "\\2 \\1",
        "^(kcal\/100g): ([\d\.]+)$": "\\2 \\1",
        "^Metabolize  \(ME\*\) \= (\d{4} kcal\/kg) \= \d{3} kcal\/cup$": "\\1",
        "^ME\(kcal\/kg\) (\d{4})$": "\\1 kcal/kg",
        "^\(ME calculated\) (3\,454 kcal\/kg)$": "\\1",
        "^[a-zA-Z0-9\/\,&\- ]+ (\d{3}) calories per 100g [\(\)a-zA-Z0-9\/\, ]+$": "\\1 kcal/100g",
        "^\(ME calculated\) (\d)\,(\d{3} kcal\/kg)$": "\\1\\2",
        "(\d)\,(\d{3} kcal\/kg)$": "\\1\\2",
        "^\(calculated\)\: (\d)\,(\d{3} kcal\/kg) or \d{3} kcal\/cup$": "\\1\\2",
        "^\(ME Calculated\) (\d{3,4} kcal\/kg)$": "\\1",
        "^[\w\s\d\/\.\%\-\+\(\)]+ ([\d\,\.]+ kcal\/kg) [\w\s\d\/\.\%\-\+]+$": "\\1",
        "^Metabolizable energy (3)\,(914 kcal\/kg)\; \d{3} kcal\/cup \(calculated\)$": "\\1\\2",
        "^[\w\s\d\/\.\,\%\-\+\(\) ]+Content([\d\,\.]+ kcal\/kg)[É™&\w\s\d\/\.\%\-\+\(\) ]+$": "\\1",
        "^\(me calculated\)\: (\d{4} kcal\/kg)$": "\\1",
        "^Kittens and pregnant or nursing females may consume two to three timesthe recommended amount$": "",
        "^(\d)\,(\d{3}) (kcal\/kg)$": "\\1\\2 \\3",
        "^5\.5ozs (\d+ kcal\/kg)\, \d+ kcal per 5\.5oz$": "\\1",
        "^Metabolizable energy (3)\,(663 kcal\/kg)\; 378 kcal\/cup \(calculated\)$": "\\1\\2",
        "kg \– 48\.5 kcal\/2\.47oz$": "kg",
        "kg\; 80 kcal\/2\.75oz cup$": "kg",
        "kg\; 73 kcal\/cup$": "kg",
        "kg or \d{3} kcal\/cup ": "kg",
        "kg or \d{3} kcal\/cup \(metabolizable energy\) on an as\-fed bas\(calculated\)\.  Contains a source of live natrually occuring microorganisms": "kg",
        "kg or \d{3} kcal\/cup \(metabolizable energy\)\(calculated\)": "kg",
        "kg or \d{3} kcal\/cup \(metabolizable energy\) on an as\-fed bas\(calculated\)": "kg",
        "kg\; \d{3} kcal\/8 cup": "kg",
        "kg\; \d{3} kcal\/3oz can \= \d{4} kcal\/kg\; \d{3} kcal\/6oz can": "kg",
        "kg\; \d{3} kcal\/6oz can": "kg",
        "kg\; \d{2,3} kcal\/3oz can \= \d{4} kcal\/kg\; \d{3} kcal\/5\.5oz can": "kg",
        "kg\; \d{2,} kcal\/tub": "kg",
        "kg\; \d{3} kcal\/8oz cup"
        "kg\; \d{2,3} kcal\/5\.5oz or \d{2,3} kcal\/3oz": "kg",
        "kg\; \d{2,3} kcal\/5\.5oz": "kg",
        "kg\; \d{2,3} kcal\/5\.5oz can": "kg",
        "kg\; \d{2,3} kcal\/can": "kg",
        "kg\; \d{2,3} kcal": "kg",
        "kg\; \d{2,3}kcal \/ 5\.5oz or \d\d kcal \/ \doz": "kg",
        "kg\; \d{2,3} kcal\/5\.5oz or \d+ kcal\/\doz": "kg",
        "kg\; \d{2,3} kcal \/ 5\.5oz or 91 kcal \/ 3oz": "kg",
        "kg\(metabolizable energy\) on an as\-fed bas\(calculated\)\.  Contains a source of live natrually occuring microorganisms": "kg",
        "kg\(metabolizable energy\)\(calculated\)": "kg",
        "kg\(metabolizable energy\) on an as\-fed bas\(calculated\)": "kg",
        "kg\/8oz cup": "kg",
        "kg can": "kg",
        "kcal\/100gr": "kcal/100g",
        "kg or \d{2,3} kcal\/3oz": "kg",
        "kg \/ 5\.5oz or \d{2,3} kcal \/ 3oz": "kg",
    }
    for _from, _to in regex_list.items():
        string = re.sub(_from, _to, string)
    return string


def main():
    for item in col.find({}):
        energy: str = item.get("calorie")
        # regex = re.compile("[\d\.]{3,} kcal/kg|[\d\.]{2,} kcal/100g")
        if type(energy) is list:
            energy = " ".join(energy)
        if energy:
            # print("\033[93m"+item.get('brand')+" \033[0m"+hello_peter(energy))
            calorie = hello_peter(energy)
            col.update_one({"_id": item["_id"]}, {"$set": {"calorie": calorie}}, upsert=True)
        # for name, attr in item.items():
        #     if not attr:
        #         print(item["title"]+" \t\t "+name)
        # analysis = item.get("analysis")
        # if type(analysis) is not list:
        #     print(type(analysis))
        #     col.update_one({"_id": item["_id"]}, {"$set": {"analysis": string_fixer(analysis)}})
        # ingredients = item.get("ingredients")
        # if type(ingredients) is not list:
        #     print(type(ingredients))
        #     col.update_one({"_id": item["_id"]}, {"$set": {"ingredients": list_splitter(ingredients)}})


if __name__ == '__main__':
    # col.insert_many(db.get_collection("CatFood_test004").find({}, {"_id": False}))
    main()
