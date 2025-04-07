users:list[dict] = [
    {'name': 'Karol', 'location': 'Miedzyrzec Podlaski', 'posts': 500, },
    {'name': 'Monika', 'location': 'Siedlce', 'posts': 1000, },
    {'name': 'Kinga', 'location': 'Lipa', 'posts': 400,}
]


def get_user_info(users_data:list[dict])->None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował: {user["posts"]} postów')

get_user_info(users)