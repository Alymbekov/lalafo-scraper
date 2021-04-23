from parser_app import (
    parse_category_links, get_products
)
from configs.utils import get_html
from configs.settings import BASE_URL

print("Welcome to parser: ")
welcome_name = input("Введите имя: ")
category_choice = input("Введите категорию: ")
# https://lalafo.kg/kyrgyzstan/elektronika
import time
for category_url in parse_category_links(get_html(BASE_URL)):
    print(get_products(get_html(category_url)))
    time.sleep(5)
    print()
    print()
