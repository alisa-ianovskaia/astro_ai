# imports
from datetime import date
from typing import NoReturn
import psycopg2

from cred import *
from generate_insert_query import *
from utils import *

def load_data_to_db(data:dict, source_id:str) -> NoReturn:
    todays_date = str(date.today())

    # establish connection
    conn = psycopg2.connect(database=DB,
                            user=USER,
                            host=HOST,
                            port=PORT)

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # read files and write queries
    for sign_id, text in data.items():
        
        if text:
            prep_text = preprocess_text(text)
            query = generate_insert_query(todays_date, sign_id, source_id, prep_text)
            cursor.execute(query)
            print(f'Writing text {sign_id} to DB...')
        else:
            print('There is no text to write to DB.')

    # Commit changes and close connection
    conn.commit()
    conn.close()
