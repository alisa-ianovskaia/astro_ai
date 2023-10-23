def generate_insert_query(date, sign_id, source_id, text:str) -> str:
    '''Generates insert query for horoscope text'''
    return f'''INSERT INTO horoscopes(hor_date, sign, source, hor_text) 
                VALUES ('{date}', {sign_id}, {source_id}, '{text}');'''
