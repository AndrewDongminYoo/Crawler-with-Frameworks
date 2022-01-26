from selenium.common.exceptions import JavascriptException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from crawling_wheel.models import CatFood
from crawling_wheel.data.data import result
import time


class WebScrapper:
    options = Options()
    options.add_argument("--window-size=1545,1047")
    options.add_argument("--window-position=0,0")

    def __init__(self, brand_name, type_of_selector="XPATH"):
        self.driver = Chrome(options=self.options)
        self.driver.implicitly_wait(10)
        # self.driver.minimize_window()
        self.brand_name = brand_name
        self.url_list = result[brand_name]
        self.type_of_selector = type_of_selector
        self.result_list = []

    def execute(self, script: str):
        try:
            return self.driver.execute_script(script)
        except JavascriptException:
            time.sleep(3)
            return self.driver.execute(script)

    def set_attr(self, element_id: str, attr_to_on: str):
        self.execute(f"document.getElementById('{element_id}').setAttribute('{attr_to_on}','true');")

    def scroll_infinite(self):
        scroll_to_bottom = "window.scrollTo(0, document.body.scrollHeight);"
        get_window_height = "return document.body.scrollHeight"
        last_height = self.execute(get_window_height)
        while True:
            self.execute(scroll_to_bottom)
            time.sleep(3)
            new_height = self.execute(get_window_height)
            if new_height == last_height:
                break
            last_height = new_height

    def activate_class(self, element_id: str, show_class: str):
        return self.execute(f"document.getElementById('{element_id}').classList.add('{show_class}');")

    def activate_class_by_selector(self, selector: str, show_class: str):
        return self.execute(f"document.querySelector('{selector}').classList.add('{show_class}');")

    def scroll_to(self, element: WebElement):
        return self.driver.execute_script("arguments[0].scrollIntoView(false);", element)

    def click_element(self, selector):
        return self.execute(f"document.querySelector('{selector}').click().scrollIntoViewIfNeeded();")

    def get_text(self, selector):
        result_list = []
        if self.type_of_selector == "XPATH":
            targets = self.driver.find_elements(By.XPATH, selector)
        else:
            targets = self.driver.find_elements(By.CSS_SELECTOR, selector)
        if len(targets) == 0:
            return None
        elif len(targets) == 1:
            self.scroll_to(targets[0])
            return targets[0].text.replace("\n", "|")
        elif len(targets) > 1:
            self.scroll_to(targets[-1])
            for t in targets:
                if t.text:
                    result_list.append(t.text.replace("\n", "|"))
            if len(result_list) == 1:
                return result_list[0]
            return result_list

    def crawl(self,
              INGREDIENTS='',
              ANALYSIS='',
              ADDITIVES='',
              CALORIE_CONTENT='',
              JAVASCRIPT='',
              ):
        for url in self.url_list:
            product = CatFood()
            product.brand = self.brand_name
            product.url = url
            self.driver.get(url)
            self.execute(JAVASCRIPT)
            time.sleep(2)
            product['title'] = self.driver.title
            if INGREDIENTS:
                product['ingredients'] = self.get_text(INGREDIENTS)
            if ANALYSIS:
                product['analysis'] = self.get_text(ANALYSIS)
            if ADDITIVES:
                product['additive'] = self.get_text(ADDITIVES)
            if CALORIE_CONTENT:
                product['calorie'] = self.get_text(CALORIE_CONTENT)
            print(product)
            self.result_list.append(product)
        self.driver.quit()
