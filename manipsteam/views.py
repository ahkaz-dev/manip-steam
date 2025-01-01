from django.shortcuts import render, get_object_or_404
# from .games import my_games_and_user_scores, games_count
from .games import games_owned, games_count
from .models import *

def home(request):
    # Sort by playtime_hours
    games_owned.sort(key=lambda item: item['playtime_forever'], reverse=True)
    return render(request, 'manipsteam/home.html', {'games': games_owned, 'games_count': games_count})

def game_info(request, game_appid):
    find_game = Game.objects.get(appid=game_appid)
    print(find_game)
    return render(request, 'manipsteam/game.html', {'game': find_game})