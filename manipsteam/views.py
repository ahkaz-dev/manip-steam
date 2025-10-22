from django.shortcuts import render, get_object_or_404, redirect
# from .games import my_games_and_user_scores, games_count
from .games import games_owned, games_count, data_clean
from .models import *
import requests
import html
from bs4 import BeautifulSoup

def home(request):
    # Sort by playtime_hours
    games_owned.sort(key=lambda item: item['playtime_forever'], reverse=True)
    return render(request, 'manipsteam/home.html', {'games': games_owned, 'games_count': games_count})

def get_screenshot_links(appid):
    url = f"https://steamcommunity.com/app/{appid}/screenshots/?p=1&browsefilter=toprated"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    screenshots = soup.find_all("img", class_="apphub_CardContentPreviewImage")
    image_links = [img['src'] for img in screenshots][:10]

    return image_links

def game_info(request, game_appid):
    game_appid = str(game_appid)  # приведение к строке для надёжности

    find_game, created = Game.objects.get_or_create(
        appid=game_appid,
        defaults={
            'name': data_clean.get(int(game_appid), 'Unknown Game'),
            'playtime_forever': 0,
        }
    )

    try:
        response = requests.get(f'https://store.steampowered.com/api/appdetails?appids={game_appid}')
        user_game_data = response.json()
    except Exception:
        user_game_data = {}

    screenshot_links = []
    if user_game_data.get(str(game_appid), {}).get('success') is False:
        screenshot_links = get_screenshot_links(game_appid)

    result_info = []
    for game_id, info in user_game_data.items():
        if info['success']:
            data = info['data']
            result_info.append({
                "short_description": data.get('short_description'),
                "about_the_game": data.get('about_the_game'),
                "genres": [g['description'] for g in data.get('genres', [])],
                "screenshots": [s['path_full'] for s in data.get('screenshots', [])],
                "release_date": data.get('release_date', {}).get('date'),
            })

    if request.method == 'POST':
        rating = request.POST.get('rating')
        status = request.POST.get('status')
        review = html.escape(request.POST.get('review', ''))

        if rating in dict(find_game.GAMERATING_CHOICE):
            find_game.local_rating = rating
            find_game.status = status
            find_game.local_review = review
            find_game.save()
            return redirect('game_info', game_appid=game_appid)

    return render(request, 'manipsteam/game.html', {
        'game': find_game,
        'scrns_game': screenshot_links,
        'game_info': result_info
    })
