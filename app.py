from utils.request_utils import main
import asyncio

page_count = 416
url_list = [f'https://www.carwale.com/used/all-used-cars/page-{page}/'for page in range(2,page_count)]


headers =  {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}


print(asyncio.run(main(url_list,headers=headers)))