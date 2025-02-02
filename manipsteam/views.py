from django.shortcuts import render, get_object_or_404, redirect
# from .games import my_games_and_user_scores, games_count
from .games import games_owned, games_count
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
    find_game = Game.objects.get(appid=game_appid)
    screenshot_links = []
    
    try:
        game_info = f'https://store.steampowered.com/api/appdetails?appids={game_appid}'
        user_game_data = requests.get(url=game_info).json()
    except:
        pass

    if user_game_data.get(str(game_appid), {}).get('success') is False:
        screenshot_links = get_screenshot_links(game_appid)

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
    
    if request.method == 'POST':
        rating = request.POST.get('rating')
        status = request.POST.get('status')
        
        review = request.POST.get('review')
        review_clean = html.escape(review)
        
        if rating in dict(find_game.GAMERATING_CHOICE):
            find_game.local_rating = rating
            find_game.status = status
            find_game.local_review = review_clean
            find_game.save()
            return redirect('game_info', game_appid=game_appid)
        
    return render(request, 'manipsteam/game.html', {'game': find_game, 'scrns_game': screenshot_links, 'game_info': result_info})