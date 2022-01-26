from crawling_wheel.selenium_soup import WebScrapper

if __name__ == '__main__':
    scraper = WebScrapper("Nutro Natural Choice")
    scraper.crawl(
        analysis="#tab-nutrition > div > div.left > div > div",
        ingredients="#tab-nutrition > div > div.right > div > div:nth-child(1) > div",
        calorie="#tab-nutrition > div > div.right > div > div:nth-child(2) > div"
    )
