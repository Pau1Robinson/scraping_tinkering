import requests
from bs4 import BeautifulSoup

URL = 'https://www.jbhifi.com.au/products/asus-vg278qr-27-full-hd-165hz-ultra-fast-gaming-monitor'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup)