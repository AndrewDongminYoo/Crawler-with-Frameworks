from crawling_wheel.selenium_soup import WebScrapper

if __name__ == '__main__':
    scraper = WebScrapper("Wellness")
    scraper.crawl(
        ingredients="#block-wellness-content > div > section.section-padding.product-detail-wysiwyg > div > div.product-detail-wysiwyg-block.ingredients > p:nth-child(2)",
        analysis="#tableWrapperWrapper > div.table-container > table > tbody",
        calorie="#tableWrapperWrapper > div.table-container > table > tbody > tr > td:-soup-contains(kcal)"
    )

    scraper = WebScrapper("Alpha Spirit")
    scraper.crawl(
        ingredients="#AddToCartForm--product-template > div.product-description.rte > div:nth-child(3) > div > p:nth-child(3) > span",
        analysis="#AddToCartForm--product-template > div.product-description.rte > div:nth-child(3) > div > table > tbody",
        additives="#AddToCartForm--product-template > div.product-description.rte > div:nth-child(3) > div > p:nth-child(4) > span"
    )
