import requests
import os
from dotenv import load_dotenv


def get_response(url, params=None, headers=None):
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response


def main():
    load_dotenv()
    dvmn_token = os.getenv('DEVMAN_TOKEN')

    dvmn_api_url = 'https://dvmn.org/api/user_reviews/'
    headers = {
        'Authorization': f'Token {dvmn_token}',
    }
    response = get_response(dvmn_api_url, headers=headers)
    print(response.text)


if __name__ == '__main__':
    main()
