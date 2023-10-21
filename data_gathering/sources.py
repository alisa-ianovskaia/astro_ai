PATH = '/Users/alisayanovski/Documents/projects/astro_ai/data_gathering'

SIGNS = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']

SOURCES_URLS_MAP = {
    '1': {'url_parts': ['https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign='],
          'signs': list(range(1, 13))},
    '2': {'url_parts': ['https://cafeastrology.com/', 'dailyhoroscope.html'],
          'signs': SIGNS},
}