from urllib.parse import urlparse, quote

from pymongo import MongoClient
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# from crawling_wheel.my_logging import logger

driver = Chrome()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, timeout=5)


def finda(XPATH) -> WebElement:
    return wait.until(EC.element_to_be_clickable((By.XPATH, XPATH)))


def search_google_image_with_title(title):
    try:
        driver.get(f"https://www.google.com/search?q={quote(title)}&tbm=isch")
        finda('//*[@id="islrg"]/div[1]/div[1]/a[1]').click()
        return finda('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute(
            "src")
    except TimeoutException:
        print(f"save image failed, {title}")
        return


def search_google_img_get_first(product):
    try:
        url = product['url']
        driver.get(f"https://www.google.com/search?q={quote(url)}&tbm=isch")
        finda('//*[@id="islrg"]/div[1]/div[1]/a[1]').click()
        return finda('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute(
            "src")
        # finda('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[1]/a[1]').click()
        # finda('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[1]/div[2]/div/a').click()
        # return finda('//*[@id="yDmH0d"]/div[6]/div/div[2]/span/div/div/div[4]/a').text
    except TimeoutException:
        print(product)


def get_host_name(url):
    parsed = urlparse(url)
    scheme = parsed.scheme
    host = parsed.hostname
    return f"{scheme}://{host}"


def main():
    client = MongoClient()
    db = client.get_database("cat")
    col = db.get_collection("CatFood_test002")
    for cat_food in col.find({}, {"_id": False}):
        if not cat_food['image']:
            cat_food['image'] = search_google_img_get_first(cat_food)
        if not cat_food['site']:
            cat_food['site'] = get_host_name(cat_food.get("url"))
        col.update_one({"url": cat_food.get("url")}, {"$set": cat_food}, upsert=True)
        # break


if __name__ == '__main__':
    main()
