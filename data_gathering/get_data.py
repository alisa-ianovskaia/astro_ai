from generate_urls import *
from get_page import *

def get_data(source_id:str) -> dict:
    urls_list = generate_urls(source_id)

    for url in urls_list:
        page = get_page(url)
