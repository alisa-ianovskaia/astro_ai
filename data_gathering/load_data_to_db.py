# imports
from datetime import date
import psycopg2
import os

from cred import *

# functions
def generate_insert_query(date, sign_id, source_id, text) -> str:
    return f'''INSERT INTO horoscopes(hor_date, sign, source, hor_text) 
                VALUES ('{date}', {sign_id}, {source_id}, '{text}');'''

# constants 
FILES_PATH = 'daily_texts/1/'

# set today's date
TODAY = str(date.today())

# establish connection
conn = psycopg2.connect(database=DB,
                        user=USER,
                        host=HOST,
                        port=PORT)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# read files and write queries
for sign_id in range(1, 13):
    full_path = f'{FILES_PATH}{sign_id}.txt'

    # check if file is not empty
    if os.stat(full_path).st_size != 0:
        
        with open(full_path, 'r') as f:
            text = f.read()
            query = generate_insert_query(TODAY, sign_id, 1, text)

            cursor.execute(query)
    else:
        print('File is empty')

# Commit changes and close connection
conn.commit()
conn.close()
