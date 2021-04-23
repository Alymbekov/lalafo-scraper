import time
from bs4 import BeautifulSoup
from configs.settings import driver


def get_products(html):
    soup = BeautifulSoup(html, "lxml")
    products = soup.find(
        "div", {
            "class": "main-feed__wrapper"
        }
    ).find_all("div", "AdTileHorizontal")

    for product in products:
        result = product.find(
            "div", {"class": "AdTileHorizontalMainInfo"}).div.a
        print(result)


driver.get("https://lalafo.kg/kyrgyzstan/elektronika")
# driver.execute_script("window.scrollTo(0, 20000)")
time.sleep(5)
html_source = driver.page_source
get_products(html_source)
