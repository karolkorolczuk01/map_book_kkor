from utils.controller import get_user_info, add_user
from utils.model import users


def mein():
    while True:
        print('====================MENU======================')
        print('0 - Exit')
        print('1 - Get user info')
        print('2 - Add user')
        print('==============================================')

        choice = input('Wybierz opcje menu: ')
        if choice == '0': break
        if choice == '1': get_user_info(users)
        if choice == '2': add_user(users)

if __name__ == '__main__':
    mein()
