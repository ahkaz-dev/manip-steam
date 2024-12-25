import requests
import os
import json

api = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'
id = os.getenv('id_key')
res = requests.get(url=api)
dict = res.json()['applist']['apps']
data_clean = {}
for game in dict:
    data_clean[game['appid']] = game['name']
    
# with open('data1.json', 'w') as f:
#     json.dump(data_clean, f)

def get_name(id):
    return data_clean[id]

def get_score(id):
    data = requests.get(f'https://store.steampowered.com/appreviews/{id}?json=1').json()['query_summary']
    score = data['total_positive']/data['total_reviews']
    return score

user_url = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={os.getenv('api_key')}&steamid={id}&format=json'
user_game_data = requests.get(url=user_url).json()

games_owned = []
for result in user_game_data['response']['games']:
    games_owned.append({
        "appid": result['appid'],
        "playtime_forever": result['playtime_forever']
    })
    
# with open('data2.json', 'w') as f:
#     json.dump(games_owned, f)

my_games_and_user_scores = {}
for game in games_owned:
    try:
        game_name = get_name(game['appid'])
        playtime_hours = game['playtime_forever'] / 60  # Преобразование в часы
        my_games_and_user_scores[game_name] = {
            "appid": game['appid'],
            "playtime_hours": round(playtime_hours, 2),  # Округление до двух знаков
        }
    except Exception as e:
        # print(f"Error fetching game info for {game['appid']}: {e}")
        game_name = 'Название игры не найдено'
        playtime_hours = game['playtime_forever'] / 60  # Преобразование в часы
        my_games_and_user_scores[game_name] = {
            "appid": game['appid'],
            "playtime_hours": round(playtime_hours, 2),  # Округление до двух знаков
        }
        # pass
    
# with open('data3.json', 'w') as f:
#     json.dump(my_games_and_user_scores, f)
