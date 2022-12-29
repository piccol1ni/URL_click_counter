import requests


def main():
    headers = {
        "long_url": "http://dvmn.org/",
        "Authorization":"Bearer 09dee2d3b0b08731615e8d021cb6f35964c5caf5",
        "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "accept":"*/*",
        "accept-language":"en-US,en;q=0.9",
        "cookie":"_xsrf=92214c6b-fa1e-6b2d-e9c3-439888eff3a2; optimizelyEndUserId=oeu1672180585333r0.5587222189206329; _gcl_au=1.1.341046742.1672180589; _gid=GA1.2.1668883922.1672180589; _sp_ses.741f=*; _fbp=fb.1.1672180589833.1080966321; __q_state_s3IbMN4fxgnkq7YJ=eyJ1dWlkIjoiMTIzM2FmMjAtOGYxMy00ODI2LTk3ZTEtOWFkYmY1ZGRhMDU0IiwiY29va2llRG9tYWluIjoiYml0bHkuY29tIiwibWVzc2VuZ2VyRXhwYW5kZWQiOmZhbHNlLCJwcm9tcHREaXNtaXNzZWQiOmZhbHNlLCJjb252ZXJzYXRpb25JZCI6IjEwMzk3MDA3NDU2NDMyNjIyODcifQ==; sp=7a48768c-5728-4ff6-9129-1f0a37379946; cookie_banner=1; anon_u=cHN1XzY1ZDk5MTY5LTc2NjgtOWJjNi0xMDZjLTc4YzhkZWU5NTI2OQ==|1672180618|0332f2953510f2ee2ef4fdb6f0e1ca67d0ab2c60; user=ZGFuZGFuMTEx|1672180618|207e4305f042051698e8e18283374cd5c1a75123; _ga=GA1.3.1578376792.1672180589; _gid=GA1.3.1668883922.1672180589; ln_or=eyIzNDA5ODQ0IjoiZCJ9; _ga=GA1.1.1578376792.1672180589; _ga_567GCTL9BB=GS1.1.1672180589.1.1.1672182224.60.0.0; _sp_id.741f=6d401c59-68ac-4b76-b7be-ffbbdd0b2475.1672180589.1.1672182224.1672180589.87ae0382-045a-429d-a66c-de7efe3d070e..da77f0f4-bffc-49d3-8dc7-e8772cd94a62.1672180598721.7",
    }

    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers)
    return response.text

if __name__=='__main__':
    print(main())