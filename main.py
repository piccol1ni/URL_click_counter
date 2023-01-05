import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def bitlink_checker(url_for_request: str):
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url_for_request}/clicks/summary', headers=headers)
    try:
        response.raise_for_status()
        return True
    except Exception:
        pass


def shorten_link(url_for_request: str):
    long_url = {
        "long_url":url_for_request,
    }
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, json=long_url)
    try:
        response.raise_for_status()
    except Exception:
        print('THIS IS FAIL LINK BRO, try something like https://google.com')
        return 'THIS IS FAIL LINK BRO'
    bitlink = response.json()["id"]
    print(bitlink)
    return bitlink


def count_clicks(url_for_request: str):
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url_for_request}/clicks/summary', headers=headers)
    print(f'Total clicks : {response.json()["total_clicks"]}')
    return f'Total clicks : {response.json()["total_clicks"]}'


if __name__=='__main__':
    load_dotenv()
    token = os.getenv("TOKEN")
    headers = {
        "Authorization":f"Bearer {token}",
    }
    url_for_request = input()
    if bitlink_checker(url_for_request):
        count_clicks(url_for_request)
    else:
        shorten_link(url_for_request)
