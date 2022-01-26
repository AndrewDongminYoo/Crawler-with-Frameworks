from crawling_wheel.selenium_soup import WebScrapper

if __name__ == '__main__':
    scraper = WebScrapper("Hill's Science Diet")
    scraper.crawl(
        analysis="#content > div > div > div > div > div.accordion.component.section.accordion-product-detail.odd.col-xs-12.initialized > div > ul > li.accordion-slide.last > div > div > div > div.box.component.section.box-product-detail.first.odd.col-xs-12 > div > div > div.productAwareRichText.richText.component.section.default-style.odd.col-xs-12.initialized > div > div > div > table > tbody",
        ingredients="div.component-content > div > div.productAwareRichText.richText.component.section.default-style.even.col-xs-12.col-sm-8.initialized > div > div > p",
        calorie="div.productAwareRichText.richText.component.section.default-style.even.col-xs-12 h6"
    )
