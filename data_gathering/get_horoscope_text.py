from bs4 import BeautifulSoup

def get_horoscope_text(page_code:str, source_id:str) -> str:
    """Returns horoscope text from html page code"""
    try:
        soup = BeautifulSoup(page_code, features="html.parser")
        if  source_id == '1':
            paragraph = soup.select('.main-horoscope p')
            text = paragraph[0].text.split('-')[1].strip()

        elif source_id == '2':
            paragraph = soup.select('.entry-content p')[3]
            text = paragraph.text.strip()

        elif source_id == '3':
            pass
        elif source_id == '4':
            pass
        elif source_id == '5':
            pass
        return text
    except Exception:
        return None 