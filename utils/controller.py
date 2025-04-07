def get_user_info(users_data: list[dict]) -> None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował: {user["posts"]} postów')

def add_user(user_data:list[dict]) -> None:
    tmp_name:str = input('Podaj imię: ')
    tmp_location:str = input('Podaj miejscowość: ')
    tmp_post:int = int(input('Podaj liczbę postów: '))
    user_data.append({'name': tmp_name, 'location': tmp_location, 'posts': tmp_post})