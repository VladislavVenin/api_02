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
    json_box = response.json()
    if 'response' in json_box:
        return json_box['response']['short_url']
    else:
        return json_box['error']['error_code']


def count_clicks(key, token):
    payload = {
        "key": key,
        "access_token": token,
        "v": 5.199
    }
    response = requests.get("https://api.vk.ru/method/utils.getLinkStats", params=payload)
    response.raise_for_status()
    json_box = response.json()
    if 'response' in json_box:
        return json_box['response']['stats'][0]['views']
    else:
        return json_box['error']['error_msg']


def is_shorten_link(url, token):
    error_code = 100
    check = shorten_link(url, token)
    if check == error_code:
        return True
    else:
        return False


def main():
    token = decouple.config('TOKEN')
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
