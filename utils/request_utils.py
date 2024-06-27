import asyncio
import aiohttp



async def fetch_page(url,headers):
    #establishing the session
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as response:
            return await response.text()


async def main(url_list,headers):
    #gathering all the results at once
    return await asyncio.gather(*(fetch_page(url,headers)for url in url_list))