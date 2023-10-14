import re
import os

def preprocess_text(text) -> str:
    '''Replaces apostroth with the double one'''
    return text.replace("'", "''")

