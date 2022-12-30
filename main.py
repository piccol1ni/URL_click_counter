import requests
from urllib.parse import urlparse


def bitlink_checker(input_url):
    if input_url[:7] == 'bit.ly/':
        return True

def url_converter(token, url):
    headers = {
        "Authorization":f"Bearer {token}",
    }
    if not bitlink_checker(url):
        json_data = {
            "long_url":url,
        }
        response_get_bitlink = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, json=json_data)
        response_get_bitlink.raise_for_status
        bitlink = response_get_bitlink.json()["id"]
        return bitlink
    else:
        bitlink = url
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary', headers=headers)
    response.raise_for_status

    return f'Total clicks : {response.json()["total_clicks"]}'


def main():
    token = input()
    url = input()
    try:
        return url_converter(token, url)
    except KeyError:
        print('Not vailid url, excample: https://google.com, or invailid autherization token!')


if __name__=='__main__':
    print(main())
