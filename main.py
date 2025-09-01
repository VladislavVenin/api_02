import requests
import decouple
import argparse
import urllib.parse
import sys


def shorten_link(url, access_token):
    payload = {
        "url": url,
        "private": 0,
        "access_token": access_token,
        "v": 5.199
    }
    short_url = requests.get("https://api.vk.ru/method/utils.getShortLink", params=payload)
    return short_url


def count_clicks(key, token):
    payload = {
        "key": key,
        "access_token": token,
        "v": 5.199
    }
    clicks = requests.get("https://api.vk.ru/method/utils.getLinkStats", params=payload)
    return clicks


def is_shorten_link(url):
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc == 'vk.cc':
        return True


def main():
    token = decouple.config('TOKEN')
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', "--link", type=str)
    args = parser.parse_args()
    link = args.link

    if is_shorten_link(link):
        try:
            clicks_count = count_clicks(link[14:], token)
        except requests.exceptions.HTTPError:
            print(clicks_count.status_code)
            sys.exit()
        clicks_count = clicks_count.json()
        try:
            print("Число просмотров:", clicks_count['response']['stats'][0]['views'])
        except KeyError:
            print(clicks_count['error']['error_msg'])
        except IndexError:
            print("Никто пока не переходил по вашей ссылке")

    else:
        try:
            short_link = shorten_link(link, token)
        except requests.exceptions.HTTPError:
            print(short_link.status_code)
            sys.exit()
        short_link = short_link.json()
        try:
            print('Сокращенная ссылка:', short_link['response']['short_url'])
            key = urllib.parse.urlparse(short_link['response']['short_url'])
            key = key.path[1:]
        except KeyError:
            print(short_link['error']['error_msg'])
            sys.exit()

        try:
            clicks_count = count_clicks(key, token)
        except requests.exceptions.HTTPError:
            print(clicks_count.status_code)
            sys.exit()
        clicks_count = clicks_count.json()
        try:
            print("Число просмотров:", clicks_count['response']['stats'][0]['views'])
        except KeyError:
            print(clicks_count['error']['error_msg'])
        except IndexError:
            print("Никто пока не переходил по вашей ссылке")


if __name__ == '__main__':
    main()
