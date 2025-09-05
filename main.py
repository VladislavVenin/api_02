import requests
import decouple
import urllib.parse
import sys


def shorten_link(url, access_token):
    payload = {
        "url": url,
        "private": 0,
        "access_token": access_token,
        "v": 5.199
    }
    response = requests.get("https://api.vk.ru/method/utils.getShortLink", params=payload)
    response.raise_for_status()
    dict_response = response.json()
    if 'response' in dict_response:
        return dict_response['response']['short_url']
    return dict_response['error']['error_code']


def count_clicks(key, token):
    payload = {
        "key": key,
        "access_token": token,
        "v": 5.199
    }
    response = requests.get("https://api.vk.ru/method/utils.getLinkStats", params=payload)
    response.raise_for_status()
    stats_response = response.json()
    return stats_response['response']['stats'][0]['views']


def is_shorten_link(url, token):
    error_code = 100
    check = shorten_link(url, token)
    return check == error_code


def main():
    token = decouple.config('TOKEN')
    link = input("Введите вашу ссылку: ")
    while not link:
        print("Вы не указали ссылку")
        link = input("Введите вашу ссылку: ")

    parsed_url = urllib.parse.urlparse(link)
    key = parsed_url.path[1:]

    if is_shorten_link(link, token):
        try:
            count = count_clicks(key, token)
        except IndexError:
            print("Никто пока не переходил по вашей ссылке")
            sys.exit()
        print(count)
    else:
        short_link = shorten_link(link, token)
        print(short_link)


if __name__ == '__main__':
    main()
