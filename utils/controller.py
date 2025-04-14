def get_user_info(users_data: list[dict]) -> None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował: {user["posts"]} postów')

def add_user(users_data:list[dict]) -> None:
    tmp_name:str = input('Podaj imię: ')
    tmp_location:str = input('Podaj miejscowość: ')
    tmp_post:int = int(input('Podaj liczbę postów: '))
    users_data.append({'name': tmp_name, 'location': tmp_location, 'posts': tmp_post})

def remove_user(users_data: list[dict]) -> None:
    user_name = input('Podaj imię użytkownika do usunięcia: ')
    for user in users_data:
        if user['name'] == user_name:
            users_data.remove(user)

def updata_user(users_data: list[dict]) -> None:
    user_name = input('Podaj imię użytkownika do zmodyfikowania: ')
    for user in users_data:
        if user['name'] == user_name:
            user['name'] = input('Podaj nowe imię: ')
            user['location'] = input('Podaj nową lokalizację: ')
            user['posts'] = input('Podaj nową liczbę postów: ')
