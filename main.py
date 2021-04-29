import os
from time import sleep

import requests
from dotenv import load_dotenv
import telegram


def get_response(url, params=None, headers=None):
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response


def check_verified_work(dvmn_token, tg_token, tg_chat_id):
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
            print(response_detail) #убрать<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            status = response_detail['status']
            if status == 'found':
                params['timestamp'] = response_detail['last_attempt_timestamp']
                verified_works = response_detail['new_attempts']

                for work in verified_works:
                    is_negative = work['is_negative']
                    lesson_title = work["lesson_title"]
                    send_tg_message(tg_token,
                                    tg_chat_id,
                                    is_negative,
                                    lesson_title)
            elif status == 'timeout':
                params['timestamp'] = response_detail['timestamp_to_request']
        except requests.exceptions.ReadTimeout:
            print('timeout')
            continue
        except requests.ConnectionError:
            print('ConnectionError')
            sleep(60)


def send_tg_message(tg_token, tg_chat_id, is_negative, lesson_title):
    bot = telegram.Bot(token=tg_token)
    if is_negative:
        bot.send_message(chat_id=tg_chat_id,
                         text=f'У вас проверили работу "{lesson_title}"\n'
                              'К сожалению, в работе нашлись ошибки.')
    else:
        bot.send_message(chat_id=tg_chat_id,
                         text=f'У вас проверили работу "{lesson_title}"\n'
                              'Преподавателю всё понравилось, можно '
                              'приступать к следующему уроку!')


def main():
    load_dotenv()
    dvmn_token = os.getenv('DEVMAN_TOKEN')
    tg_token = os.getenv('TG_NOTIFY_BOT_TOKEN')

    tg_chat_id = os.getenv('MY_ID')

    check_verified_work(dvmn_token, tg_token, tg_chat_id)

if __name__ == '__main__':
    main()
