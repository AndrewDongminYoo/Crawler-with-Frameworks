window.onload = (() => {
    loadCatFoods(1)
})

function loadCatFoods(num) {
    let articleContainer = document
        .querySelector("#page-content > div > div > div.row > div > div > section.results-products.js-tracked-product-list")
    fetch(`/v1/cat-foods?page=${num}`)
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            data.forEach((a) => {
                let article = showArticle(a)
                articleContainer.innerHTML += article
            })
        })
        .catch((reason) => {
            console.log(reason)
        })
}

function showArticle(article) {
    let {analysis, brand, calorie, image, ingredients, site, title, url} = article
    return `<article class="product-holder js-tracked-product  cw-card cw-card-hover">
        <a class="product is-10-px-padded"
           href="${url}" style="padding-bottom: 104px;">
            <div class="image-holder">
                <img alt="${title}"
                     loading="lazy"
                     src="${image}">
                <span class="product-choices "
                      href=""> More Choices Available</span>
                <div class="badge">
                </div>
            </div>
            <div class="content">
                <h2>
                    <strong>${brand}</strong> ${title}
                </h2>
                <h2>${analysis}</h2>
                <h2>${ingredients}</h2>
                <div class="product-info">
                    <p class="price">
                        <strong>
                            ${calorie}
                        </strong>
                        <span class="price-old">$31.98</span>
                    </p>
                    <p class="rating item-rating">
                        <picture>
                            <source srcset="/assets/img/ratings/rating-4_5.svg"
                                    type="image/svg+xml">
                            <img alt="rating-star" src="/assets/img/ratings/rating-4_5.png">
                        </picture>
                        <span>410</span>
                    </p>
                    <p class="shipping">${site}
                    </p>
                </div>
            </div>
            <section class="ga-eec__container hidden">
                <div class="ga-eec__currencyCode">USD</div>
                <div class="ga-eec__name">Purina ONE True Instinct Natural Real Chicken Plus
                    Vitamins &amp; Minerals High Protein Grain-Free Dry Cat Food, 14.4-lb bag
                </div>
                <div class="ga-eec__id">135642</div>
                <div class="ga-eec__brand">Purina ONE</div>
                <div class="ga-eec__category">388</div>
                <div class="ga-eec__category-hierarchy">
                </div>
                <div class="ga-eec__price">29.98</div>
                <div class="ga-eec__position">1</div>
                <div class="ga-eec__variant">14.4-lb bag</div>
                <div class="ga-eec__dimension25">false</div>
                <div class="ga-eec__dimension18">
                    { "deal": false, "strike": false, "greenbar": false }
                </div>
                <div class="ga-eec__dimension19">
                </div>
            </section>
        </a>
    </article>`
}