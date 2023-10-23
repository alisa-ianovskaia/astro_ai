import requests
from fake_headers import Headers

def get_page(url:str) -> str:
    """Returns html code of a page for given URL"""
    headers = Headers().generate()
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.text
    
    print(f'Something went wrong. The response status: {response.status_code}')
    return None
