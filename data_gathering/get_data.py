import time
import random

from generate_urls import *
from get_page import *
from get_horoscope_text import *

def get_data(source_id:str) -> dict:
    # generate urls for the source
    urls_list = generate_urls(source_id)

    # initialize dict for horoscopes
    horoscopes_dict = dict()

    # get text from page and write to dict
    for i, url in enumerate(urls_list):
        page_code = get_page(url)
        text = get_horoscope_text(page_code, source_id)

        horoscopes_dict[str(i)] = text

        # wait
        time.sleep(random.randint(3, 16))

    return horoscopes_dict
