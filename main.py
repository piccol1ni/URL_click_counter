import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def bitlink_checker(url: str):
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary', headers=headers)
    try:
        response.raise_for_status()
        return True
    except Exception:
        pass


def shorten_link(url: str):
    json_data = {
        "long_url":url,
    }
    response_get_bitlink = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, json=json_data)
    try:
        response_get_bitlink.raise_for_status()
    except Exception:
        print('THIS IS FAIL LINK BRO, try something like https://google.com')
        return 'THIS IS FAIL LINK BRO'
    bitlink = response_get_bitlink.json()["id"]
    print(bitlink)
    return bitlink


def count_clicks(url: str):
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary', headers=headers)
    print(f'Total clicks : {response.json()["total_clicks"]}')
    return f'Total clicks : {response.json()["total_clicks"]}'


if __name__=='__main__':
    load_dotenv()
    token = os.getenv("TOKEN")
    headers = {
        "Authorization":f"Bearer {token}",
    }
    url = input()
    if bitlink_checker(url):
        count_clicks(url)
    else:
        shorten_link(url)
