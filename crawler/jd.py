import requests
from bs4 import BeautifulSoup
import urllib.parse

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

def search_price(book_name):
    query = urllib.parse.quote(book_name)
    url = f'https://search.jd.com/Search?keyword={query}&enc=utf-8'
    resp = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(resp.text, 'html.parser')
    price_tag = soup.select_one('div.p-price strong i')
    if price_tag:
        return price_tag.get_text(strip=True)
    return '未找到价格'
