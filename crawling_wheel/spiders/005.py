from crawling_wheel.selenium_soup import WebScrapper

if __name__ == '__main__':
    scraper = WebScrapper("Natural Greatness")
    scraper.crawl(
        ingredients="div.elementor-text-editor.elementor-clearfix > :-soup-contains(Mineral)",
        analysis="div.elementor-text-editor.elementor-clearfix > :-soup-contains(Crude)",
        calorie="div.elementor-text-editor.elementor-clearfix > div > :-soup-contains(kcal)"
    )
    scraper = WebScrapper("Sanabelle")
    scraper.crawl(
        ingredients="#zusammensetzung > div > p:nth-child(3)",
        analysis="#analyt > div > div > div.modal-body",
        additives="#zusatzstoffe > div > div > div.modal-body > p"
    )
    scraper = WebScrapper("Whiskas")
    scraper.crawl(
        ingredients="body > main > div:nth-child(1) > section.pdSec2 > div > div.col-xs-12.col-sm-6.xs-m-b-15 > div > p",
        analysis="body > main > div:nth-child(1) > section.pdSec3 > div > div:nth-child(2) > div > table > tbody",
        calorie="body > main > div:nth-child(1) > section.pdSec3 > div > div:nth-child(2) > div.color-cont > div"
    )

