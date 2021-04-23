from bs4 import BeautifulSoup


def get_products(html):
    soup = BeautifulSoup(html)
    print(soup)
