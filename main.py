import os

import requests
from dotenv import load_dotenv


def get_response(url, params=None, headers=None):
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response


def main():
    load_dotenv()
    dvmn_token = os.getenv('DEVMAN_TOKEN')

    dvmn_api_url = 'https://dvmn.org/api/long_polling/'
    headers = {
        'Authorization': f'Token {dvmn_token}',
    }
    params = {
        'timestamp': None
    }

    while True:
        response = get_response(dvmn_api_url, headers=headers, params=params)
        response_detail = response.json()
        print(response_detail)
        status = response_detail['status']
        if status == 'found':
            params['timestamp'] = response_detail['last_attempt_timestamp']
        if status == 'timeout':
            params['timestamp'] = response_detail['timestamp_to_request']



if __name__ == '__main__':
    main()
