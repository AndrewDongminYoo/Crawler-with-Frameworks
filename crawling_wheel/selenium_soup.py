import time

import pymongo
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from crawling_wheel.data import result
from .models import CatFood
from .my_logging import get_my_logger


class WebScrapper:
    options = Options()
    options.add_argument("--window-size=1545,1047")
    options.add_argument("--window-position=0,0")

    def __init__(self, brand_name):
        self.brand_name = brand_name
        self.url_list = result[brand_name]
        # os.popen("mongod")
        client = pymongo.MongoClient()
        db = client.get_database("cat")
        self.col = db.get_collection("CatFood")
        self.logger = get_my_logger(brand_name)

    def crawl(self, analysis="", ingredients="", calorie="", additives=""):
        with Chrome(options=self.options) as driver:
            driver.implicitly_wait(10)
            for index, url in enumerate(self.url_list):
                item = CatFood()
                driver.get(url)
                item.url = url
                item.brand = self.brand_name
                item.title = driver.title
                next_value = ""
                try:
                    time.sleep(3)
                    WebDriverWait(driver, 8).until(EC.presence_of_all_elements_located((By.TAG_NAME, "p")))
                    soup = BeautifulSoup(driver.page_source, "html.parser")
                    if analysis:
                        next_value = "analysis"
                        item.analysis = soup.select_one(analysis).get_text().replace("\n", " ")
                    if ingredients:
                        next_value = "ingredients"
                        item.ingredients = soup.select_one(ingredients).get_text().replace("\n", " ")
                    if calorie:
                        next_value = "calorie"
                        item.calorie = soup.select_one(calorie).get_text()
                    if additives:
                        next_value = "additives"
                        item.additives = soup.select_one(additives).get_text()
                    self.col.update_one({"title": item.title}, {"$set": item.to_mongo()}, upsert=True)
                    self.logger.info(f"Saved ({index+1}/{len(self.url_list)}) :: {url}")
                except TimeoutException:
                    self.logger.warning(f"Timeout ({index+1}/{len(self.url_list)}) :: {url}")
                except AttributeError as e:
                    self.logger.warning(f"{e} :: {url}".replace("NoneType", next_value))


if __name__ == '__main__':
    scraper = WebScrapper("AlmoNature")
    scraper.crawl(
        analysis="#product > div > section.Ingredients > div > div.Ingredients__components.active > ul",
        ingredients="#product > div > section.Ingredients > div > div.Ingredients__info > div",
        calorie="#product > div > section.Ingredients > div > div.Ingredients__components.active > ul > li:nth-child(6)"
    )
