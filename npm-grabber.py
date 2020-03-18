from bs4 import BeautifulSoup
import time
import sys
import os
import re
import requests
import colorama
colorama.init()


def know_status(username):
    try:
        r = requests.get(url=f'https://www.npmjs.com/~{username}')
        if r.status_code == 404:
            return '404'
        else:
            return 'OK'
    except(requests.exceptions.ConnectionError):
        red = '\033[91m'
        endcolor = '\033[0m'
        print(f'{red}NO INTERNET CONNECTION{endcolor}')
        time.sleep(2)
        os.system('cls')
        main()


def npm_checker(username):
    try:
        r = requests.get(url=f'https://www.npmjs.com/~{username}')
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        element_scripts = soup.find_all('script')
        window_context = str(element_scripts[1].text)

        target_fullname = re.search(r'"fullname":"(.*?)"', window_context)
        try:
            fullname = target_fullname.group(1)
        except AttributeError:
            fullname = 'none'
        target_email = re.search(r'"email":"(.*?)"', window_context)
        try:
            email = target_email.group(1)
        except AttributeError:
            email = 'none'

        target_github = re.search(r'"github":"(.*?)"', window_context)
        try:
            github = target_github.group(1)
        except AttributeError:
            github = 'none'

        target_twitter = re.search(r'"twitter":"(.*?)"', window_context)
        try:
            twitter = target_twitter.group(1)
        except AttributeError:
            twitter = 'none'

        return fullname, email, github, twitter

    except(requests.exceptions.ConnectionError):
        red = '\033[91m'
        endcolor = '\033[0m'
        print(f'{red}NO INTERNET CONNECTION{endcolor}')
        time.sleep(2)
        os.system('cls')
        main()


def main():
    try:
        orange = '\033[33m'
        purple = '\033[105m'
        green = '\033[32m'
        endback = '\033[49m'
        endfore = '\033[39m	'
        print(f'{purple}NPM USER INFO{endback}\n')
        print(f'{orange}Enter username{endfore}')
        username = input('>>> ').lower().strip(' ')

        if username == ':q':
            sys.exit()
        os.system('cls')
        status = know_status(username)

        if status == 'OK':
            fullname, email, github, twitter = npm_checker(username)
            print(
                f'{green}User fullname:{endfore} {fullname}\n{green}User email:{endfore} {email}\n{green}User github:{endfore} {github}\n{green}User twitter:{endfore} {twitter}\n')
            print(f'{orange}press [ENTER] to restart{endfore}')
            restart = input('').lower().strip(' ')

            if restart:
                os.system('cls')
                main()
            else:
                os.system('cls')
                main()

        elif status == '404':
            print(f'{orange}No such user{endfore}')
            time.sleep(2)
            os.system('cls')
            main()
    except KeyboardInterrupt:
        os.system('cls')
        print(f'{orange}Process killed by user{endfore}')
        time.sleep(0.5)
        os.system('cls')
        sys.exit()


if __name__ == "__main__":
    main()
