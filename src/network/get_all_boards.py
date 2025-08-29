"""
    Functions that search and return all 4chan boards, ensuring the project
    does not use deprecated boards and none are left out.

    Author: JuaanReis
    Date: 28-08-2025
    Last modification: -
    E-mail: teixeiradosreisjuan@gmail.com   
    Version: 0.0.1

    Example:
        from get_all_boards import get_boards, get_request

        response = get_request(url)
        boards = get_boards(response)

        for board in boards:
            print(board)
"""

import httpx
from ..utils.load_config import load_config_json
import re
from bs4 import BeautifulSoup

def get_response(url):
    try:
        DATA = load_config_json()
        with httpx.Client(http2=True) as client:
            response = client.get(url, timeout=4)
        return response
    except httpx.RequestError:
        return None
        
def get_boards(response):
    if response is None:
        return []
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        pattern = re.compile(r"^//boards\.4chan\.org/([a-z0-9]+)/?$")
        boards = set()
        for a in soup.find_all("a", href=pattern):
            match = pattern.match(a['href'])
            if match:
                board_name = match.group(1)
                boards.add(board_name)
        return list(boards)
    except Exception as e:
        return []