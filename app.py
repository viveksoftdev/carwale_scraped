import asyncio
import aiohttp

from bs4 import BeautifulSoup

page_count = 416
url_list = [f'https://www.carwale.com/used/all-used-cars/page-{page}/'for page in range(2,page_count)]

print(url_list)