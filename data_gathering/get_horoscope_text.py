from bs4 import BeautifulSoup
from utils import *

# css selectors for each source
SOURCES_SELECTORS_MAP = {
    '1': '.main-horoscope p',
    '2': '.entry-content p',
    '3': 'p.body',
    '4': 'article[data-qa="main"] p.mt-sm',
    '5': '#main-content > div > .article-container > div[data-journey-body="standard-article"] > p'
}

def get_horoscope_text(page_code:str, source_id:str) -> str:
    """Returns horoscope text from html page code"""

    try:
        soup = BeautifulSoup(page_code, features="html.parser")
        paragraph = soup.select(SOURCES_SELECTORS_MAP[source_id])
        
        if source_id == '2':
            text = paragraph[3].text.strip()
        elif (source_id == '1') | (source_id == '3'):
            text = preprocess_soup(paragraph[0].text)
        elif (source_id == '4') | (source_id == '5'):
            text = paragraph[0].text.strip()
        return text
    
    except Exception as err:
        print(f'Unexpected {err}=, {type(err)}=')
        return None 
    