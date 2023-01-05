import requests
import os

from dotenv import load_dotenv
from urllib.parse import urlparse


def bitlink_checker(url_for_request: str):
    token = os.getenv("TOKEN")
    headers = {
        "Authorization":f"Bearer {token}",
    }
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url_for_request}/clicks/summary', headers=headers)
    response.raise_for_status()
    return True



def shorten_link(url_for_request: str):
    token = os.getenv("TOKEN")
    long_url = {
        "long_url":url_for_request,
    }
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, json=long_url)
    response.raise_for_status()
    bitlink = response.json()["id"]
    return bitlink


def count_clicks(url_for_request: str):
    headers = {
        "Authorization":f"Bearer {token}",
    }
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{url_for_request}/clicks/summary', headers=headers)
    return f'Total clicks : {response.json()["total_clicks"]}'


def main():


if __name__=='__main__':
    load_dotenv()
    url_for_request = input()
    try:
        if bitlink_checker(url_for_request):
            print(count_clicks(url_for_request))
    except requests.exceptions.HTTPError:
        try:
            print(shorten_link(url_for_request))
        except requests.exceptions.HTTPError as ex:
            print(ex)           
