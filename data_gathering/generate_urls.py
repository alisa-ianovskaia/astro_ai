SOURCES_URLS_MAP = {
    '1': 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=',
    '2': ['https://cafeastrology.com/', 'dailyhoroscope.html'],
    '3': ['https://www.dailyhoroscope.com/horoscopes/daily/', '?full=true'],
    '4': 'https://www.washingtonpost.com/horoscopes/',
    '5': ['https://www.elle.com/horoscopes/daily/a','-daily-horoscope/']
}

SIGNS = ['aries', 'taurus', 'gemini', 'cancer', 'leo',
        'virgo', 'libra', 'scorpio', 'sagittarius',
        'capricorn', 'aquarius', 'pisces']

def generate_urls(source_id:str) -> list:
    '''Returns list of generated urls for each source'''
    urls = list()
    
    if  source_id == '1':
        for n in range(1, 13):
            urls.append(SOURCES_URLS_MAP[source_id] + str(n))
    
    elif (source_id == '2') | (source_id == '4'):
        url_first_part = SOURCES_URLS_MAP[source_id][0]
        url_second_part = SOURCES_URLS_MAP[source_id][1]
        for sign in SIGNS:
            urls.append(url_first_part + sign + url_second_part)
    
    elif source_id == '3':
        for sign in SIGNS:
            urls.append(SOURCES_URLS_MAP[source_id] + sign)
    
    elif source_id == '5':
        url_first_part = SOURCES_URLS_MAP[source_id][0]
        url_last_part = SOURCES_URLS_MAP[source_id][1]
        url_middle_parts = ['60/'] + [f'{str(n)}/' for n in range(98,109)]
        for sign, middle_part in zip(SIGNS, url_middle_parts):
            urls.append(url_first_part + middle_part + sign + url_last_part)
    
    else:
        raise ValueError('Parameter "source_id" should be string in range 1-5.')
    
    return urls