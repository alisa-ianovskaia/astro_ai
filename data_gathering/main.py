from typing import NoReturn
from get_data import *
from load_data_to_db import *

import sys

def main(source_id) -> NoReturn:
    data = get_data(source_id)
    load_data_to_db(data, source_id,)

main(sys.argv[1])