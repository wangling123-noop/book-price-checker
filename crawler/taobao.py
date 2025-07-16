import requests
from bs4 import BeautifulSoup
import urllib.parse

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

def search_price(book_name):
    query = urllib.parse.quote(book_name)
    url = f'https://s.taobao.com/search?q={query}'
    resp = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(resp.text, 'html.parser')
    price_tag = soup.select_one('div.price g_price g_price-highlight')  # 示例，需根据网页实际调整
    if price_tag:
        return price_tag.get_text(strip=True)
    return '未找到价格'
