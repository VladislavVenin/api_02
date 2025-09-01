import requests
import urllib.parse
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-hs', "--host",
                        type=str,
                        help="url",
                        default="https://wttr.in")
    parser.add_argument('-p', "--places",
                        type=str,
                        help="places",
                        nargs='*',
                        default=['svo'])
    parser.add_argument('-k', "--keys",
                        type=str,
                        help="key=value pairs",
                        nargs='*')
    args = parser.parse_args()
    host = args.host
    places = args.places
    keys = args.keys
    if keys:
        keys = dict(key.split('=') for key in keys)

    for place in places:
        try:
            response = requests.get(urllib.parse.urljoin(host, place), params=keys)
        except requests.exceptions.ConnectionError:
            print("The host name contains errors or is written in an invalid format")
            break
        if not response.ok:
            print(response.status_code)
        else:
            print(response.text)


if __name__ == '__main__':
    main()
