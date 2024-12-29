import requests
import os

api = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'
id = os.getenv('id_key')
api_key = os.getenv('api_key')

res = requests.get(url=api)
dict = res.json()['applist']['apps']
data_clean = {}
for game in dict:
    data_clean[game['appid']] = game['name']
    
def get_name(id):
    return data_clean[id]

def get_score(id):
    data = requests.get(f'https://store.steampowered.com/appreviews/{id}?json=1').json()['query_summary']
    score = data['total_positive']/data['total_reviews']
    return score

user_url = f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={api_key}&steamid={id}&include_appinfo=true&include_extended_appinfo=true&include_played_free_games=true'
user_game_data = requests.get(url=user_url).json()

games_owned = []
games_count = user_game_data['response']['game_count']
for result in user_game_data['response']['games']:
    games_owned.append({
        "appid": result['appid'],
        "name": result['name'],
        "playtime_forever": round(result['playtime_forever'] / 60)
    })