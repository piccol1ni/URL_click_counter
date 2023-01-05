import requests
import os

from dotenv import load_dotenv
from urllib.parse import urlparse


def is_bitlink(url_for_request: str):
    token = os.environ["BITLY_TOKEN"]
    headers = {
        "Authorization":f"Bearer {token}",
    }
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url_for_request}', headers=headers)
    return response.ok

def shorten_link(url_for_request: str):
    token = os.getenv("BITLY_TOKEN")
    headers = {
        "Authorization":f"Bearer {token}",
    }
    long_url = {
        "long_url":url_for_request,
    }
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, json=long_url)
    response.raise_for_status()
    bitlink = response.json()["id"]
    return bitlink


def count_clicks(url_for_request: str):
    token = os.getenv("BITLY_TOKEN")
    headers = {
        "Authorization":f"Bearer {token}",
    }
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url_for_request}/clicks/summary', headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


if __name__=='__main__':
    load_dotenv()
    url_for_request = input()
    if is_bitlink(url_for_request) is True:
        print(f'Total clicks: {count_clicks(url_for_request)}')
    else:
        try:
            print(shorten_link(url_for_request))
        except requests.exceptions.HTTPError as ex:
            print(ex)           
