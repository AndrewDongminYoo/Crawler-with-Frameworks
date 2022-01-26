from crawling_wheel.selenium_soup import WebScrapper

if __name__ == '__main__':
    # scraper = WebScrapper("Forza10 USA")
    # scraper.crawl(
    #     ingredients="#tab__Nutritional-Info > div > p:nth-child(2)",
    #     analysis="#tab__Nutritional-Info > div > p:nth-child(4)",
    #     calorie="#tab__Nutritional-Info > div > p:nth-child(3)"
    # )
    # scraper = WebScrapper("KOOKUT")
    # scraper.crawl(
    #     ingredients="section > div > div.product__info-wrapper.grid__item > div > div:nth-child(12) > details > div > p > span",
    #     analysis="section > div > div.product__info-wrapper.grid__item > div > div:nth-child(13) > details > div > p > span"
    # )
    # scraper = WebScrapper("MeowMix")
    # scraper.crawl(
    #     ingredients="#tab-nutrition-collapse-0 > div > div.left > p",
    #     analysis="#tab-nutrition-collapse-0 > div > div.right > div.guaranteed-analysis > div"
    # )
    # scraper = WebScrapper("ZiwiPeak")
    # scraper.crawl(
    #     ingredients="#quickset-tabs_air_dried_and_canned_no_ta > div > div.view.view-pdp-2019-page-elements.resp-tab-content > div > div > div > div > div > div.pdp-ingredients-list",
    #     analysis="#quickset-tabs_air_dried_and_canned_no_ta > div > div.view.view-pdp-2019-page-elements.resp-tab-content > div.view-content > div",
    # )
    # scraper = WebScrapper("Chicken Soup for the Soul")
    # scraper.crawl(
    #     ingredients="div.view-mode-full > div.field-wrapper.field.field-node--field-ingredients.field-name-field-ingredients.field-type-text-long.field-label-above > div > div > p:nth-child(2)",
    #     analysis="div.view-mode-full > div.field-wrapper.field.field-node--field-guaranteed-analysis.field-name-field-guaranteed-analysis.field-type-text-long.field-label-above > div > div > table > tbody",
    #     calorie="div.view-mode-full > div.field-wrapper.field.field-node--field-calorie-content.field-name-field-calorie-content.field-type-text-long.field-label-above > div > div > p:nth-child(2)"
    # )
    # scraper = WebScrapper("Merrick")
    # scraper.crawl(
    #     ingredients="#ingredients > p",
    #     analysis="#guaranteed-analysis > div > div.analysis__table.col-12.col-md-6",
    #     calorie="#feeding-guide > div.feeding-guide__wrapper > div.feeding-guide__additional > p:nth-child(4)"
    # )
    # scraper = WebScrapper("NutriSource")
    # scraper.crawl(
    #     ingredients="#ingredients-nutrition > div.et_pb_row.et_pb_row_4 > div.et_pb_column.et_pb_column_2_3.et_pb_column_6.et_pb_css_mix_blend_mode_passthrough > div.et_pb_module.et_pb_text.et_pb_text_10.et_pb_text_align_left.et_pb_bg_layout_light > div > p:nth-child(2)",
    #     calorie="#ingredients-nutrition > div.et_pb_row.et_pb_row_4 > div.et_pb_column.et_pb_column_1_3.et_pb_column_7.et_pb_css_mix_blend_mode_passthrough.et-last-child > div > div > table > tbody",
    #     analysis="#ingredients-nutrition > div.et_pb_row.et_pb_row_4 > div.et_pb_column.et_pb_column_2_3.et_pb_column_6.et_pb_css_mix_blend_mode_passthrough > div.et_pb_module.et_pb_text.et_pb_text_11.et_pb_text_align_left.et_pb_bg_layout_light > div > table > tbody"
    # )
    # scraper = WebScrapper("Thrive complete")
    # scraper.crawl(
    #     ingredients="#po2",
    #     analysis="#po3"
    # )
    # scraper = WebScrapper("Weruva Catfood")
    # scraper.crawl(
    #     ingredients="#nutritionDetailInfo > div > div.col-md-8.col-xl-7.order-first > div.product-extra-detail.product-ingredients-detail > p:nth-child(3)",
    #     analysis="#nutritionDetailInfo > div > div.col-md-4 > div:nth-child(2) > table",
    #     calorie="#nutritionDetailInfo > div > div.col-md-4 > div:nth-child(1) > table > tbody"
    # )
    # scraper = WebScrapper("Optimanova")
    # scraper.crawl(
    #     ingredients="#contenido-2 > div > div > div:nth-child(2) > div.col-xs-8.column > div.composicion.infosec > div.info",
    #     analysis="#contenido-2 > div > div > div:nth-child(2) > div.col-xs-8.column > div:nth-child(3) > div.info",
    #     additives="#contenido-2 > div > div > div:nth-child(2) > div.col-xs-8.column > div:nth-child(4) > div.info"
    # )
    # scraper = WebScrapper("Organix")
    # scraper.crawl(
    #     ingredients="#ingredientsContentContainer > div > p:nth-child(1)",
    #     analysis="#analysisContentContainer > div > div > table",
    #     calorie="#feedingGuideContentContainer > div > div > label > p:last-child"
    # )
    scraper = WebScrapper("Rawz")
    scraper.crawl(
        ingredients="#our-recipe > div:nth-child(2) > div.ingredients-column > div",
        analysis="#guaranteed-analysis > div > div > div > table > tbody",
        calorie="#feeding-guidelines-table > div > div > div > table > tbody > tr:last-child > td:nth-child(2)"
    )
