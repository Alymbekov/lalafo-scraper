import urllib.request
from urllib.request import urlopen
from configs.settings import header


def get_html(url):
    request = urllib.request.Request(url=url, headers=header)
    html = urlopen(request)
    return html
