from django.shortcuts import render
from .games import my_games_and_user_scores

def home(request):
    # Сортировка словаря по значению playtime_hours
    sorted_games = dict(sorted(my_games_and_user_scores.items(), key=lambda item: item[1]['playtime_hours'], reverse=True))

    # print(response)
    return render(request, 'manipsteam/home.html', {'response': sorted_games})