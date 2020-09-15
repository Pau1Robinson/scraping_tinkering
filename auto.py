from autoscraper import AutoScraper

url = 'https://www.jbhifi.com.au/products/asus-vg278qr-27-full-hd-165hz-ultra-fast-gaming-monitor'

wanted_list = ['Screen Size (Inches)', '27']

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)