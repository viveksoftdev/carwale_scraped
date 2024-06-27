from utils.request_utils import main

page_count = 416
url_list = [f'https://www.carwale.com/used/all-used-cars/page-{page}/'for page in range(2,page_count)]


print(asyncio.run(main(url_list)))