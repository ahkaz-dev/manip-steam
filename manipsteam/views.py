from django.shortcuts import render
# from .games import my_games_and_user_scores, games_count
from .games import games_owned, games_count

def home(request):
    # Sort by playtime_hours
    games_owned.sort(key=lambda item: item['playtime_forever'], reverse=True)
    return render(request, 'manipsteam/home.html', {'games': games_owned, 'games_count': games_count})