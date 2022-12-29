import requests
import json
from urllib.parse import urlparse


def count_clicks(token, url):
    headers = {
        "Authorization":f"Bearer {token}",
    }

    json_data = {
        "long_url":url,
    }
    response_get_bitlink = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, json=json_data)
    bitlink = response_get_bitlink.json()["id"]
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary')
    print(urlparse(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'))
    print(response.raise_for_status)
    return response.text

def main():
    token = input()
    url = input()
    try:
        return count_clicks(token, url)
    except KeyError:
        print('Not vailid url, excample: https://google.com, or invailid autherization token!')


if __name__=='__main__':
    print(main())
