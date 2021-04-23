from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


BASE_URL = "https://lalafo.kg"


header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
    'AppleWebKit/537.11 (KHTML, like Gecko) '
    'Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

chrome_options = Options()
chrome_options.add_argument("--disable-javascript")
driver = webdriver.Chrome(ChromeDriverManager(
    chrome_type=ChromeType.GOOGLE).install())



