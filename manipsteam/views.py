from django.shortcuts import render
from .games import my_games_and_user_scores

def home(request):
    # Sort by playtime_hours
    sorted_games = dict(sorted(my_games_and_user_scores.items(), key=lambda item: item[1]['playtime_hours'], reverse=True))

    return render(request, 'manipsteam/home.html', {'response': sorted_games})