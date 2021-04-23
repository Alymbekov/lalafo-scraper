from bs4 import BeautifulSoup
from configs.settings import BASE_URL


def parse_category_links(html):
    soup = BeautifulSoup(html, "lxml")
    div_nav_container = soup.find(
        "div", {
            "class": "main-nav__container"
        })
    li_tags = div_nav_container.find(
        "ul", {
            "class": "main-nav__first-level-list"
        }).children
    category_links = set()
    for li in li_tags:
        if not li.a:
            continue
        full_url_to_category = BASE_URL + li.a["href"]
        category_links.add(full_url_to_category)
    return category_links
