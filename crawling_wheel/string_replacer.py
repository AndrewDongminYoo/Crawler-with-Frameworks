import re

from pymongo import MongoClient

client = MongoClient()
db = client.get_database("cat")
col = db.get_collection("CatFood_test005")


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


def main():
    for item in col.find({}):
        # analysis = item.get("analysis")
        # if type(analysis) is str and analysis:
        # col.update_one({"_id": item["_id"]}, {"$set": {"analysis": string_fixer(analysis)}})
        # col.update_one({"_id": item["_id"]}, {"$set": {"analysis": analysis.split(", ")}})
        # print(analysis)
        ingredients = item.get("ingredients")
        if type(ingredients) is str and ingredients:
            print(list_splitter(ingredients))
            col.update_one({"_id": item["_id"]}, {"$set": {"ingredients": list_splitter(ingredients)}})


if __name__ == '__main__':
    # col.insert_many(db.get_collection("CatFood_test004").find({}, {"_id": False}))
    main()
