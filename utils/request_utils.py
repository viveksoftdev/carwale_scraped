import asyncio
import aiohttp
import re
import pandas as pd
from bs4 import BeautifulSoup

async def fetch_page(url,headers):
    #establishing the session
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as response:
            return await response.text()


async def main(url_list,headers):
    #gathering all the results at once
    return await asyncio.gather(*(fetch_page(url,headers)for url in url_list))


def create_soup(data):
    soup = BeautifulSoup(data,'html.parser')
    return soup

def parse_return(results):
    parsed_list = []
    for data in results:
        parsed_list.append(create_soup(data))
    return parsed_list

def extract(parsed_list,pattern,tag,num):
    import re
    from collections import defaultdict
    url_dict = defaultdict(list)
    for soup in parsed_list:
        print(soup.find_all(tag[num]))
        for item in soup:
            for _ in re.findall(pattern,str(item)):
                url_dict['url'].append(_)
    return url_dict

def to_csv(url_dict,f_name,encoding='utf-8-sig'):
    df = pd.DataFrame(url_dict)

    df.to_csv('urls.csv',encoding='utf-8-sig')