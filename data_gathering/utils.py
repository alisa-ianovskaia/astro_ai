from datetime import date

def preprocess_soup(text:str) -> str:
    '''Preprocesses text from source 3 and 1 and returns only horoscope.'''
    # get rid of everything after the horoscope
    text = text.split('\n')[0]
    
    # find where the current date at the beginning of the text ends
    year_now = date.today().year
    str_to_find = f'{year_now } - '
    index_to_cut = text.find(str_to_find) + len(str_to_find)

    return text[index_to_cut:].strip() 

def preprocess_text(text:str) -> str:
    '''Replaces apostroth with the double one'''
    return text.replace("'", "''")

