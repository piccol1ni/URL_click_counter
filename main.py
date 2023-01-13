import argparse
import requests
import os

from urllib.parse import urlparse
from dotenv import load_dotenv


def is_bitlink(url_for_user: str, token: str):
    headers = {
        "Authorization": f"Bearer {token}",
    }
    parsed_url = urlparse(url_for_user)

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.netloc}{parsed_url.path}',
                            headers=headers)
    return response.ok


def shorten_link(url_for_user: str, token: str):
    headers = {
        "Authorization": f"Bearer {token}",
    }
    long_url = {
        "long_url": url_for_user,
    }
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks',
                            headers=headers, json=long_url)
    response.raise_for_status()
    bitlink = response.json()["id"]
    return bitlink


def count_clicks(url_for_user: str, token: str):
    headers = {
        "Authorization": f"Bearer {token}",
    }
    parsed_url = urlparse(url_for_user)
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.netloc}{parsed_url.path}/clicks/summary',
                            headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


if __name__=='__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description='''Make shorten URLs using bit.ly
                                     or show count of clocks if it is bit.ly URL''')
    parser.add_argument('link', help='Your url or bit.ly url')


    args = parser.parse_args()
    token = os.getenv("BITLY_TOKEN")
    try:
        if is_bitlink(args.link, token):
            print(f'Total clicks: {count_clicks(args.link, token)}')
        else:
            print(shorten_link(args.link, token))
    except requests.exceptions.HTTPError as ex:
        print(ex)
