from crawling_wheel.selenium_soup import WebScrapper

if __name__ == '__main__':
    # scraper = WebScrapper("Blackwood Pet Food")
    # scraper.crawl(
    #     ingredients="#main > div.product-tabs > div > div.tabs > div.tab.tab-ingredients > div.wp-block-group > div",
    #     analysis="#main > div.product-tabs > div > div.tabs > div.tab.tab-guaranteed-analysis > table > tbody",
    #     calorie="#main > div.product-tabs > div > div.tabs > div.tab.tab-guaranteed-analysis > table > tbody > tr:last-child > td"
    # )
    # scraper = WebScrapper("Feline Natural")
    # scraper.crawl(
    #     ingredients="#accordion-container > div:nth-child(4) > div > p",
    #     analysis="#accordion-container > div.accordion-content > div > table > tbody > tr > td:nth-child(1) > p:nth-child(2)",
    #     calorie="#accordion-container > div.accordion-content > div > table > tbody > tr > td:nth-child(1) > p:nth-child(4)",
    #     additives="#accordion-container > div.accordion-content > div > table > tbody > tr > td:nth-child(2) > p:nth-child(2)"
    # )
    # scraper = WebScrapper("Leonardo Catfood")
    # scraper.crawl(
    #     ingredients="#analyse-tab-pane > div > div > div.product-detail-analyse-text > div:nth-child(1) > div:nth-child(1) > p",
    #     analysis="#analyse-tab-pane > div > div > div.product-detail-analyse-text > div:nth-child(1) > div:nth-child(2) > p",
    #     additives="#analyse-tab-pane > div > div > div.product-detail-analyse-text > div:nth-child(1) > div:nth-child(3) > p:nth-child(3)",
    # )
    # scraper = WebScrapper("Lotus")
    # scraper.crawl(
    #     ingredients="#app > div > div.animated.fadeIn > div > div:nth-child(2) > div > div > div.tab-content > div.tab-pane > div > div > div > div:nth-child(1) > p",
    #     analysis="#app > div > div.animated.fadeIn > div > div:nth-child(2) > div > div > div.tab-content > div.tab-pane > div > div > div > div > div.row.mb-4 > div > div:nth-child(3)",
    #     calorie="#app > div > div.animated.fadeIn > div > div:nth-child(2) > div > div > div.tab-content > div.tab-pane > div > div > div > div > div:nth-child(3) > div > div:nth-child(3) > div:nth-child(4) > ul > li"
    # )
    scraper = WebScrapper("Nature's Logic")
    scraper.crawl(
        ingredients="#av-layout-grid-1 > div.flex_cell.no_margin.av_one_half.avia-builder-el-13.el_after_av_cell_one_half.avia-builder-el-last.avia-full-stretch > div > div > section > div > p",
        analysis="#av-tab-section-1-2 > div > div > section > div > table",
        additives="#av-tab-section-1-4 > div > div > section > div > table",
        calorie="#av_section_2 > div > div > div > div > div.flex_column.av-1jsyzdm-cf33a913e34200fe85da617b61c289df.av_one_fifth.avia-builder-el-54.el_after_av_one_fifth.avia-builder-el-last.flex_column_div.av-zero-column-padding > div"
    )
    scraper = WebScrapper("Terra Fellis")
    scraper.crawl(
        ingredients="#description-tab-pane > div > div.product-info-composition.tab-section > div > div > div > div.compostion-text-container.order-1.order-lg-2",
        analysis="#analytical-components-tab-pane > div > div > div > div > p > span",
    )
    scraper = WebScrapper("BlackHawk")
    scraper.crawl(
        ingredients="#tabs-2 > div > p",
        analysis="#tabs-3 > div > table:nth-child(2) > tbody",
        additives="#tabs-3 > div > table:nth-child(3) > tbody"
    )
    scraper = WebScrapper("Catz finefood")
    scraper.crawl(
        ingredients="body > div.page-wrap > section > div > div.content--wrapper > div > div.tab-menu--product.js--tab-menu > div.tab--container-list > div > div.tab--content > div.content--description > div.product--description > p:nth-child(3)",
        analysis="body > div.page-wrap > section > div > div.content--wrapper > div > div.tab-menu--product.js--tab-menu > div.tab--container-list > div > div.tab--content > div.content--description > div.product--description > p:nth-child(5) > span",
        calorie="body > div.page-wrap > section > div > div.content--wrapper > div > div.tab-menu--product.js--tab-menu > div.tab--container-list > div > div.tab--content > div.content--description > div.product--description > p:nth-child(4)",
        additives="body > div.page-wrap > section > div > div.content--wrapper > div > div.tab-menu--product.js--tab-menu > div.tab--container-list > div > div.tab--content > div.content--description > div.product--description > p:nth-child(6) > span",
    )
    scraper = WebScrapper("First Choice Canada")
    scraper.crawl(
        ingredients="",
        analysis="",
        calorie=""
    )
    scraper = WebScrapper("Monge")
    scraper.crawl(
        ingredients="",
        analysis="",
        calorie=""
    )
    scraper = WebScrapper("Nature's Protection")
    scraper.crawl(
        ingredients="",
        analysis="",
        calorie=""
    )
    scraper = WebScrapper("Sheba")
    scraper.crawl(
        ingredients="",
        analysis="",
        calorie=""
    )
    scraper = WebScrapper("SolidGold Petfood")
    scraper.crawl(
        ingredients="",
        analysis="",
        calorie=""
    )
    scraper = WebScrapper("Vigor and Sage")
    scraper.crawl(
        ingredients="",
        analysis="",
        calorie=""
    )
    scraper = WebScrapper("Vital Essentials")
    scraper.crawl(
        ingredients="",
        analysis="",
        calorie=""
    )
    scraper = WebScrapper("BOREAL")
    scraper.crawl(
        ingredients="",
        analysis="",
        calorie=""
    )
