import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def bitlink_checker(bitlink_url: str):
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_url}/clicks/summary', headers=headers)
    try:
        response.raise_for_status()
        return True
    except Exception:
        pass


def shorten_link(bitlink_url: str):
    json_data = {
        "long_url":bitlink_url,
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


def count_clicks(bitlink_url: str):
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_url}/clicks/summary', headers=headers)
    print(f'Total clicks : {response.json()["total_clicks"]}')
    return f'Total clicks : {response.json()["total_clicks"]}'


if __name__=='__main__':
    load_dotenv()
    token = os.getenv("TOKEN")
    headers = {
        "Authorization":f"Bearer {token}",
    }
    bitlink_url = input()
    if bitlink_checker(bitlink_url):
        count_clicks(bitlink_url)
    else:
        shorten_link(bitlink_url)
