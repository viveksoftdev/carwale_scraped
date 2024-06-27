import asyncio
import aiohttp
import re
import pandas as pd
from bs4 import BeautifulSoup
from collections import defaultdict

async def fetch_page(url, headers, timeout=10):
    """
    Fetches the HTML content of a given URL asynchronously using aiohttp.

    Args:
    - url (str): The URL to fetch.
    - headers (dict): Headers to be included in the HTTP request.
    - timeout (int, optional): Timeout duration in seconds. Default is 10 seconds.

    Returns:
    - str: The HTML content of the fetched page as a string, or an empty string if a timeout occurs.
    """
    async with aiohttp.ClientSession() as session:
        try:
            timeout_obj = aiohttp.ClientTimeout(total=timeout)
            async with session.get(url, headers=headers, timeout=timeout_obj) as response:
                return await response.text()
        except asyncio.TimeoutError:
            return ''

async def main(url_list, headers):
    """
    Asynchronously fetches pages from a list of URLs using fetch_page.

    Args:
    - url_list (list): List of URLs to fetch.
    - headers (dict): Headers to be included in the HTTP requests.

    Returns:
    - list: List of HTML content strings fetched from each URL.
    """
    return await asyncio.gather(*(fetch_page(url, headers) for url in url_list))

def create_soup(data):
    """
    Creates a BeautifulSoup object from HTML data.

    Args:
    - data (str): HTML content as a string.

    Returns:
    - BeautifulSoup object: Parsed BeautifulSoup object representing the HTML.
    """
    try:
        if isinstance(data, str):
            soup = BeautifulSoup(data, 'html.parser')
        return soup
    except Exception as error:
        print(error)

def parse_return(results):
    """
    Parses a list of HTML content strings into BeautifulSoup objects.

    Args:
    - results (list): List of HTML content strings.

    Returns:
    - list: List of BeautifulSoup objects parsed from each HTML string.
    """
    parsed_list = []
    for data in results:
        parsed_list.append(create_soup(data))
    return parsed_list

def extract(parsed_list, pattern, tag, num):
    """
    Extracts URLs from BeautifulSoup objects based on a given pattern.

    Args:
    - parsed_list (list): List of BeautifulSoup objects.
    - pattern (str): Regular expression pattern to match URLs.
    - tag (str): HTML tag to search within (e.g., 'a' for <a> tags).
    - num (int): Used for indexing here.

    Returns:
    - defaultdict: Dictionary with 'url' as key and a list of extracted URLs as values.
    """
    url_dict = defaultdict(list)
    for soup in parsed_list:
        for item in soup.find_all(tag):
            for url in re.findall(pattern, str(item)):
                url_dict['url'].append(url)
    return url_dict

def to_csv(url_dict, f_name, encoding='utf-8-sig'):
    """
    Converts a dictionary of URLs into a Pandas DataFrame and saves it as CSV.

    Args:
    - url_dict (defaultdict): Dictionary with 'url' as key and list of URLs as values.
    - f_name (str): File name for the CSV output.
    - encoding (str, optional): Encoding format for the CSV file. Default is 'utf-8-sig'.
    """
    df = pd.DataFrame(url_dict)
    df.to_csv(f_name, encoding=encoding)
