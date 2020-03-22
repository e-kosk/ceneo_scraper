# Ceneo Scraper

## Etap 1 - analiza struktury opinii w serwisie [ceneo.pl](https://www.ceneo.pl/)
|Składowa                |Selektor                                        |Nazwa zmiennej|
|------------------------|------------------------------------------------|--------------|
|opinia                  |li.js_product-review                            |              |
|identyfikator opinii    |["data-entry-id"]                               |              |
|autor                   |div.reviewer-name-line                          |              |
|rekomendacja            |div.product-review-summary > em                 |              |
|ocena                   |span.review-score-count                         |              |
|treść opinii            |p.product-review-body                           |              |
|lista wad               |div.cons-cell > ul                              |              |
|lista zalet             |div.pros-cell > ul                              |              |
|przydatna               |button.vote-yes > span                          |              |
|nieprzydatna            |button.vote-no > span                           |              |
|data wystawienia opinii |span.review-time > time:first-child["datetime"] |              |
|data zakupu             |span.review-time > time:nth-child(2)["datetime"]|              |

## Etap 2 - pobranie składowych pojedynczej opinii
