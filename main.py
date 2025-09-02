import requests
import decouple
import urllib.parse


def shorten_link(url, access_token):
    payload = {
        "url": url,
        "private": 0,
        "access_token": access_token,
        "v": 5.199
    }
    try:
        short_url = requests.get("https://api.vk.ru/method/utils.getShortLink", params=payload)
    except requests.exceptions.HTTPError:
        return short_url.status_code
    try:
        return short_url.json()['response']['short_url']
    except KeyError:
        return short_url.json()['error']['error_code']


def count_clicks(key, token):
    payload = {
        "key": key,
        "access_token": token,
        "v": 5.199
    }
    try:
        clicks = requests.get("https://api.vk.ru/method/utils.getLinkStats", params=payload)
    except requests.exceptions.HTTPError:
        return clicks.status_code
    try:
        return clicks.json()['response']['stats'][0]['views']
    except KeyError:
        return clicks.json()['error']['error_msg']
    except IndexError:
        print("Никто пока не переходил по вашей ссылке")


def is_shorten_link(url):
    check = shorten_link(url, decouple.config('TOKEN'))
    if check == 100:
        return False
    else:
        return True


def main():
    token = decouple.config('TOKEN')
    link = input("Введите вашу ссылку: ")
    parsed_url = urllib.parse.urlparse(link)
    key = parsed_url.path[1:]

    if not is_shorten_link(link):
        print(count_clicks(key, token))
    else:
        print(shorten_link(link, token))


if __name__ == '__main__':
    main()
