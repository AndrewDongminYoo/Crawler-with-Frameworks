from crawling_wheel.selenium_soup import WebScrapper

if __name__ == '__main__':
    scraper = WebScrapper("Blackwood Pet Food")
    scraper.crawl(
        ingredients="#main > div.product-tabs > div > div.tabs > div.tab.tab-ingredients > div.wp-block-group > div",
        analysis="#main > div.product-tabs > div > div.tabs > div.tab.tab-guaranteed-analysis > table > tbody",
        calorie="#main > div.product-tabs > div > div.tabs > div.tab.tab-guaranteed-analysis > table > tbody > tr:last-child > td"
    )
    scraper = WebScrapper("Feline Natural")
    scraper.crawl(
        ingredients="#accordion-container > div:nth-child(4) > div > p",
        analysis="#accordion-container > div.accordion-content > div > table > tbody > tr > td:nth-child(1) > p:nth-child(2)",
        calorie="#accordion-container > div.accordion-content > div > table > tbody > tr > td:nth-child(1) > p:nth-child(4)",
        additives="#accordion-container > div.accordion-content > div > table > tbody > tr > td:nth-child(2) > p:nth-child(2)"
    )
    scraper = WebScrapper("Leonardo Catfood")
    scraper.crawl(
        ingredients="#analyse-tab-pane > div > div > div.product-detail-analyse-text > div:nth-child(1) > div:nth-child(1) > p",
        analysis="#analyse-tab-pane > div > div > div.product-detail-analyse-text > div:nth-child(1) > div:nth-child(2) > p",
        additives="#analyse-tab-pane > div > div > div.product-detail-analyse-text > div:nth-child(1) > div:nth-child(3) > p:nth-child(3)",
    )
    scraper = WebScrapper("Lotus")
    scraper.crawl(
        ingredients="#app > div > div.animated.fadeIn > div > div:nth-child(2) > div > div > div.tab-content > div.tab-pane > div > div > div > div:nth-child(1) > p",
        analysis="#app > div > div.animated.fadeIn > div > div:nth-child(2) > div > div > div.tab-content > div.tab-pane > div > div > div > div > div.row.mb-4 > div > div:nth-child(3)",
        calorie="#app > div > div.animated.fadeIn > div > div:nth-child(2) > div > div > div.tab-content > div.tab-pane > div > div > div > div > div:nth-child(3) > div > div:nth-child(3) > div:nth-child(4) > ul > li"
    )
    scraper = WebScrapper("Nature's Logic")
    scraper.crawl(
        ingredients="#av-layout-grid-1 > div.flex_cell.no_margin.av_one_half.el_after_av_cell_one_half.avia-builder-el-last.avia-full-stretch",
        analysis="#av-tab-section-1-2 > div > div > section > div > table",
        additives="#av-tab-section-1-4 > div > div > section > div > table",
        calorie="#av_section_2 > div > div > div > div > div.flex_column.av_one_fifth.el_after_av_one_fifth.avia-builder-el-last.flex_column_div.av-zero-column-padding > div > strong"
    )
    scraper = WebScrapper("Terra Felis")
    scraper.crawl(
        ingredients="#description-tab-pane > div > div.product-info-composition.tab-section > div > div > div > div.compostion-text-container.order-1.order-lg-2",
        analysis="#analytical-components-tab-pane > div > div > div > div > p > span",
    )
    scraper = WebScrapper("BlackHawk")
    scraper.crawl(
        ingredients="#tabs-2 > div > p",
        analysis="#tabs-3 > div > table > tbody"
    )
    scraper = WebScrapper("Catz finefood")
    scraper.crawl(
        ingredients="body > div.page-wrap > section > div > div.content--wrapper > div > div.tab-menu--product.js--tab-menu > div.tab--container-list > div > div.tab--content > div.content--description > div.product--description > p:nth-child(3)",
        analysis="body > div.page-wrap > section > div > div.content--wrapper > div > div.tab-menu--product.js--tab-menu > div.tab--container-list > div > div.tab--content > div.content--description > div.product--description > p:nth-child(5)",
        calorie="body > div.page-wrap > section > div > div.content--wrapper > div > div.tab-menu--product.js--tab-menu > div.tab--container-list > div > div.tab--content > div.content--description > div.product--description > p:nth-child(4)",
        additives="body > div.page-wrap > section > div > div.content--wrapper > div > div.tab-menu--product.js--tab-menu > div.tab--container-list > div > div.tab--content > div.content--description > div.product--description > p:nth-child(6)",
    )
    scraper = WebScrapper("First Choice Canada")
    scraper.crawl(
        ingredients="body > section.section.section--has-medium-padding.section--has-small-padding-bottom.section--has-smaller-padding-top-mobile > div > div > ul > li:nth-child(2) > div.accordion__item-content.js-accordion-item-content > p",
        analysis="body > section.section.section--has-medium-padding.section--has-small-padding-bottom.section--has-smaller-padding-top-mobile > div > div > ul > li:nth-child(3) > div.accordion__item-content.js-accordion-item-content > p",
        calorie="#tab-adult > table > tbody > tr:nth-child(10) > td > div.complex-table__footer-row.complex-table__footer-infos.grid.grid--justify-center.grid--align-center"
    )
    scraper = WebScrapper("Monge")
    scraper.crawl(
        ingredients="div.post-content > div.row.info_product > div > div.tab-content > div:nth-child(1) > p",
        analysis="div.post-content > div.row.info_product > div > div.tab-content > div:nth-child(2) > p",
        additives="div.post-content > div.row.info_product > div > div.tab-content > div:nth-child(3) > p"
    )
    scraper = WebScrapper("Nature's Protection")
    scraper.crawl(
        ingredients="#txt_cont > div.product_cont > div.data.aright > div.descr > div > table > tbody > tr > td.content.dazymas > div:nth-child(1) > div:nth-child(1) > div > span:nth-child(2)",
        analysis="#txt_cont > div.product_cont > div.data.aright > div.descr > div > table > tbody > tr > td.content.formos",
        additives="#txt_cont > div.product_cont > div.data.aright > div.descr > div > table > tbody > tr > td.content.dazymas > div:nth-child(1) > div:nth-child(4) > span:nth-child(3)",
    )
    scraper = WebScrapper("Sheba")
    scraper.crawl(
        ingredients="#content > article > div.product-details > div.tab.ingredients > div",
        analysis="#content > article > div.product-details > div.tab.nutrition > div",
        calorie="#content > article > div.product-details > div.tab.nutrition > div:nth-child(2)"
    )
    scraper = WebScrapper("SolidGold Petfood")
    scraper.crawl(
        ingredients="#eael-advance-tabs-ca9134b > div.eael-tabs-content > div:nth-child(1) > span",
        analysis="#eael-advance-tabs-ca9134b > div.eael-tabs-content > div:nth-child(2) > table > tbody",
        calorie="#eael-advance-tabs-ca9134b > div.eael-tabs-content > div.clearfix > table > tbody > tr:last-child > td:last-child"
    )
    scraper = WebScrapper("Vigor and Sage")
    scraper.crawl(
        ingredients="#tab-additional_information > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_composition > td > p:nth-child(1)",
        additives="#tab-additional_information > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_composition > td > p:nth-child(2)",
        analysis="#tab-additional_information > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_analytical-constituents > td > p",
    )
    scraper = WebScrapper("Vital Essentials")
    scraper.crawl(
        ingredients="#chicken-freeze-dried-mini-patties-entree-2 > main > section.product-wrapper > div.tab-wrapper > div.tab.nutrition.clearfix > div:nth-child(1) > p",
        analysis="#chicken-freeze-dried-mini-patties-entree-2 > main > section.product-wrapper > div.tab-wrapper > div.tab.nutrition.clearfix > div:nth-child(2)",
    )
    scraper = WebScrapper("BOREAL")
    scraper.crawl(
        ingredients="#content > div:nth-child(15) > h6:nth-child(2)",
        analysis="#content > div:nth-child(18) > p:nth-child(1)",
        calorie="#content > div:nth-child(18) > p:nth-child(3)"
    )
