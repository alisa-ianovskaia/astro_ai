import requests
from bs4 import BeautifulSoup

def get_html_page(url, headers) -> str:
    """Returns html code of a page for given URL"""
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def get_horoscope(page_code) -> str:
    """Returns horoscope text from html page code"""
    try:
        soup = BeautifulSoup(page_code, features="html.parser")
        paragraph = soup.select('.main-horoscope p')
        text = paragraph[0].text.split('-')[1].strip()
        return text
    except Exception:
        return None 
