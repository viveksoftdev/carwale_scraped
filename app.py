from utils.request_utils import (main,parse_return,
                                 extract,to_csv)
import asyncio
import json
import pandas as pd

page_count = 3
url_list = [f'https://www.carwale.com/used/all-used-cars/page-{page}/'for page in range(2,page_count)]


headers =  {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}


results = asyncio.run(main(url_list,headers=headers))

parsed_list = parse_return(results)

pattern = r'"url":\s{1,5}"([^,].+)?"'

url_dict = extract(parsed_list=parsed_list,pattern=pattern,tag='script',num=0)

#creating a dataframe out of the scraped urls
file_name = 'carwale_urls.csv'
to_csv(url_dict,file_name,)



