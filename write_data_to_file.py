# imports
import time
import random

from typing import NoReturn
from fake_headers import Headers
from utils import preprocess_text
from urls import *
from get_data import *

def write_to_file(horoscope, file) -> NoReturn:
    with open(file, 'w') as f:
        f.write(horoscope)

def write_all_horoscopes(url) -> NoReturn:
    for sign_num in range(1, 13):
        full_url = url + str(sign_num)
        headers = Headers().generate()

        page_code = get_html_page(full_url, headers)
        horoscope_text = preprocess_text(get_horoscope(page_code))
        
        file_name = f'daily_texts/1/{sign_num}.txt'
        write_to_file(horoscope_text, file_name)

        print(f'Horoscope {sign_num} is done')

        time.sleep(random.randint(3, 16))

        
write_all_horoscopes(URL)