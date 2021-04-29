import os
from time import sleep

import requests
from dotenv import load_dotenv
import telegram


def get_response(url, params=None, headers=None):
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response


def check_verified_work(dvmn_token):
    dvmn_api_url = 'https://dvmn.org/api/long_polling/'
    headers = {
        'Authorization': f'Token {dvmn_token}',
    }
    params = {
        'timestamp': None,
    }

    while True:
        try:
            response = get_response(dvmn_api_url, headers=headers, params=params)
            response_detail = response.json()
            print(response_detail)
            status = response_detail['status']
            if status == 'found':
                params['timestamp'] = response_detail['last_attempt_timestamp']
            elif status == 'timeout':
                params['timestamp'] = response_detail['timestamp_to_request']
        except requests.exceptions.ReadTimeout:
            print('timeout')
            continue
        except requests.ConnectionError:
            print('ConnectionError')
            sleep(60)


def main():
    load_dotenv()
    dvmn_token = os.getenv('DEVMAN_TOKEN')
    tg_token = os.getenv('TG_NOTIFY_BOT_TOKEN')

    chat_id = os.getenv('MY_ID')

    # check_verified_work(dvmn_token)

    bot = telegram.Bot(token=tg_token)
    bot.send_message(chat_id=chat_id, text="Привет")

if __name__ == '__main__':
    main()
