from django.shortcuts import render, get_object_or_404
# from .games import my_games_and_user_scores, games_count
from .games import games_owned, games_count
from .models import *
import requests

def home(request):
    # Sort by playtime_hours
    games_owned.sort(key=lambda item: item['playtime_forever'], reverse=True)
    return render(request, 'manipsteam/home.html', {'games': games_owned, 'games_count': games_count})

def game_info(request, game_appid):
    find_game = Game.objects.get(appid=game_appid)
    try:
        game_info = f'https://store.steampowered.com/api/appdetails?appids={game_appid}'
        user_game_data = requests.get(url=game_info).json()
    except Exception:
        pass
    result_info = []
    for game_id, game_info in user_game_data.items():
        if game_info['success']:
            data = game_info['data']
            result_info.append({
                "short_description": data.get('short_description'),
                "detailed_description": data.get('detailed_description'),
                "about_the_game": data.get('about_the_game'),
                "categorie1": data['categories'][0]['description'],
                "categorie2": data['categories'][1]['description'],
                "categorie3": data['categories'][2]['description'],
                "genres": [genre['description'] for genre in data['genres']],
                "screenshots": [screenshot['path_full'] for screenshot in data['screenshots']],
                "release_date": data['release_date'].get('date'),
            })
    print(user_game_data)
    return render(request, 'manipsteam/game.html', {'game': find_game, 'game_info': result_info})