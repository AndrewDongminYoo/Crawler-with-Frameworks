from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from random import choice
from w3lib import html
driver = Chrome()
driver.implicitly_wait(10)

with open("catfood_addresses", mode="r", encoding="utf8", newline="") as input_file:
    for line in input_file.readlines():
        driver.get(line.strip())
        soup = BeautifulSoup(driver.page_source, "html.parser")
        print(driver.title)
        for tag in soup.get_text().split("\n"):
            if tag.strip():
                print(tag.strip().replace("  ", " "))

    # print(html.remove_tags(driver.page_source))
    driver.quit()
