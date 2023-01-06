import requests
import os

from dotenv import load_dotenv
from urllib.parse import urlparse


def is_bitlink(url_for_request: str, token: str):
    headers = {
        "Authorization": f"Bearer {token}",
    }
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url_for_request}', headers=headers)
    return response.ok

def shorten_link(url_for_request: str, token: str):
    headers = {
        "Authorization": f"Bearer {token}",
    }
    long_url = {
        "long_url": url_for_request,
    }
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, json=long_url)
    response.raise_for_status()
    bitlink = response.json()["id"]
    return bitlink


def count_clicks(url_for_request: str, token: str):
    headers = {
        "Authorization": f"Bearer {token}",
    }
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url_for_request}/clicks/summary', headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


if __name__=='__main__':
    load_dotenv()
    url_for_request = input()
    token = os.getenv("BITLY_TOKEN")
    try:
        if is_bitlink(url_for_request, token):
            print(f'Total clicks: {count_clicks(url_for_request, token)}')
        else:
            print(shorten_link(url_for_request, token))
    except requests.exceptions.HTTPError as ex:
        print(ex)
