from crawling_wheel.selenium_soup import WebScrapper

if __name__ == '__main__':
    scraper = WebScrapper("Instinct Pet Food")
    scraper.crawl(
        ingredients="#our-ingredients > div > p",
        analysis="#nutritional-info > div > div:nth-child(4)",
        calorie="#nutritional-info > div > div:nth-child(3) > div > div > div:nth-child(2) > div"
    )
    scraper = WebScrapper("Nutrience")
    scraper.crawl(
        ingredients="body > div.main-container > div.container.product-info-ctn > div:nth-child(3) > div.col-md-7.offset-lg-1 > div.features-details-ctn > div.product-details-ctn > div:nth-child(1) > div",
        analysis="#tabs-3 > #analysis-table > tbody",
        calorie="#tabs-3 > p:-soup-contains(kcal)"
    )
    scraper = WebScrapper("Nutram Canada")
    scraper.crawl(
        ingredients="",
        analysis="",
        calorie=""
    )
    scraper = WebScrapper("Against The Grain")
    scraper.crawl(
        ingredients="div.entry.page.type-page.status-publish.entry div.entry_post > p:-soup-contains(Vitamins)",
        analysis="#content > div.sidebar_down > div:nth-child(1) > div.container_widgets_pieces > div.widget_center.widget_content > div > table > tbody",
        calorie="#content > div.sidebar_down > div:nth-child(1) > div.container_widgets_pieces > div.widget_center.widget_content > div > table > tbody > tr:last-child"
    )
    scraper = WebScrapper("Cardinal Fussie Cat")
    scraper.crawl(
        ingredients="div > div.elementor-element.elementor-widget.elementor-widget-heading > div > div.elementor-heading-title.elementor-size-default",
        analysis="div.elementor-element.elementor-widget.elementor-widget-heading > div > div:-soup-contains(Crude)",
        calorie="div.elementor-container.elementor-column-gap-default div.elementor-row div.elementor-column.elementor-col-50.elementor-inner-column.elementor-element:nth-child(1) div.elementor-column-wrap.elementor-element-populated div.elementor-widget-wrap div.elementor-element.elementor-widget.elementor-widget-heading > div.elementor-widget-container"
    )

