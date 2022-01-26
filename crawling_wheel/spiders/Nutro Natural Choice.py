from crawling_wheel.selenium_soup import WebScrapper

if __name__ == '__main__':
    scraper = WebScrapper("Nutro Natural Choice")
    scraper.crawl(
        analysis="#product > section:nth-child(5) > div > div > div.two-third.break-half > section:nth-child(1) > div > div:nth-child(1) > div > div > dl:nth-child(2) > dd > div > table > tbody",
        ingredients="#product > section:nth-child(5) > div > div > div.two-third.break-half > section:nth-child(1) > div > div:nth-child(2) > div > ul",
        calorie="#product > section:nth-child(5) > div > div > div.two-third.break-half > section:nth-child(1) > div > div:nth-child(1) > div > div > dl:nth-child(2) > dd > div > table > tbody > tr:last-child > td:nth-child(2)"
    )

    scraper = WebScrapper("Nutro")
    scraper.crawl(
        analysis="body > main > section.proDetSec2 > div > div > div:nth-child(2) > div > table > tbody",
        ingredients="body > main > section.proDetSec2 > div > div > div:nth-child(1) > div > p",
        calorie="body > main > section.proDetSec3 > div > div > div:nth-child(2) > div > p:-soup-contains(calculated)"
    )
