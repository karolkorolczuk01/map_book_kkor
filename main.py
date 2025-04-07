from utils.controller import get_user_info
from utils.model import users


def mein():
    while True:
        print('====================MENU======================')
        print('0 - Exit')
        print('1 - Get user info')
        print('==============================================')

        choice = input('Wybierz opcje menu: ')
        if choice == '0': break
        if choice == '1': get_user_info(users)

if __name__ == '__main__':
    mein()
