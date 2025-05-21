def get_user_info(users_data: list[dict]) -> None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował: {user["posts"]} postów')


def add_user(users_data: list[dict]) -> None:
    tmp_name: str = input('Podaj imię: ')
    tmp_location: str = input('Podaj miejscowość: ')
    tmp_post: int = int(input('Podaj liczbę postów: '))
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


def get_coordinates(location_name: str) -> list:
    import requests
    from bs4 import BeautifulSoup
    adres_url: str = f'https://pl.wikipedia.org/wiki/{location_name}'
    response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
    return [
        float(response_html.select('.latitude')[1].text.replace(',', '.')),
        float(response_html.select('.longitude')[1].text.replace(',', '.')),
    ]


def get_map(users_data: list[dict]) -> None:
    import folium
    map = folium.Map(location=[52.3, 21.0], zoom_start=6, tiles='OpenStreetMap')
    for user in users_data:
        # print(get_coordinates(user['location'])) debug
        folium.Marker(
            location=get_coordinates(user['location']),
            popup=f'<h5>{user['location']}</h5><br/>{user['name']}<br/>{user['posts']}'
        ).add_to(map)
    map.save('mapa.html')
