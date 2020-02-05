# Import libraries
import requests, os
import urllib.request
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
import statistics
import json
# Set the URL you want to webscrape from
def get_game_ids(outfile='game_ids.csv'):
    all_games = []
    ### Get the top 5000 games from BBG
    for i in tqdm(range(1,51)):
        print(i)
        # Connect to the URL

        response = requests.get(f'https://boardgamegeek.com/browse/boardgame/page/{i}')

        # Parse HTML and save to BeautifulSoup object¶
        soup = BeautifulSoup(response.text, "html.parser")

        for row in soup.find_all(id='row_'):
            all_games.append(row.find_all('a')[1].get('href'))
    game_ids = list(map(lambda x: x.split('/')[2], all_games))

    ### Get the top 1500 kid games from BBG
    kid_games = []
    for i in tqdm(range(1,16)):

        # Connect to the URL
        response = requests.get(f'https://boardgamegeek.com/childrensgames/browse/boardgame/page/{i}')

        # Parse HTML and save to BeautifulSoup object¶
        soup = BeautifulSoup(response.text, "html.parser")
        for row in soup.find_all(id='row_'):
            if row.find_all('td')[3].contents[0].strip()!='N/A':
                kid_games.append(row.find_all('a')[1].get('href'))
    for elm in map(lambda x: x.split('/')[2], kid_games):
        game_ids.append(elm)
    ### Get the top 1500 family games from BBG
    family_games = []
    for i in tqdm(range(1,16)):

        # Connect to the URL
        response = requests.get(f'https://boardgamegeek.com/familygames/browse/boardgame/page/{i}')

        # Parse HTML and save to BeautifulSoup object¶
        soup = BeautifulSoup(response.text, "html.parser")
        for row in soup.find_all(id='row_'):
            if row.find_all('td')[3].contents[0].strip()!='N/A':
                family_games.append(row.find_all('a')[1].get('href'))

    for elm in map(lambda x: x.split('/')[2], family_games):
        game_ids.append(elm)
    game_ids = set(game_ids)
    with open(outfile, 'w') as f:
        for id in game_ids:
            f.write(f'{id}\n')

def get_game_info(game_id):
    stats_kws = ['usersrated','average', 'bayesaverage', 'stddev', 'median', 'owned', 'trading','wanting','wishing','numcomments', 'numweights','averageweight']
    info_kws = ['yearpublished', 'minplayers', 'maxplayers', 'playingtime','minplaytime','maxplaytime','age']
    # See what's been saved
    done = set()
    #for id in tqdm(set(game_id)):
    game_json = {}
    #First get the stats
    response = requests.get(f'https://www.boardgamegeek.com/xmlapi/boardgame/{game_id}?stats=1')

    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")
    game_json['name'] = soup.find("name", primary=True).contents[0]
    for kw in info_kws:
        game_json[kw] = soup.find(kw).contents[0]
        game_json['description'] = soup.find('description').contents[0].replace('<br/>', ' ').strip()
        try:
            game_json['img_url'] = soup.find('thumbnail').contents[0]
        except IndexError:
            game_json['img_url'] = 'N/A'
        game_json['user_suggested_age'] = 0
        game_json['user_suggested_players'] = []

    for poll in soup.find_all('poll'):

        if poll.get('name') == "suggested_playerage":
            total_votes = float(poll.get('totalvotes'))
            if total_votes > 0:
                for elm in poll.find_all('result'):
                    game_json['user_suggested_age'] += float(elm.get('value').split(' ')[0])*float(elm.get('numvotes'))
                game_json['user_suggested_age'] /= total_votes
        elif poll.get('name') == 'suggested_numplayers':
            for results in poll.find_all('results'):
                suggested_num_dict = {'player_num' : results.get('numplayers')}
                for elm in results.find_all('result'):
                    suggested_num_dict[elm.get('value')] = elm.get('numvotes')
                game_json['user_suggested_players'].append(suggested_num_dict)

    stats = soup.find('ratings')
    game_json['stats'] = {}
    for kw in stats_kws:
        game_json['stats'][kw] = float(stats.find(kw).contents[0])
    num_comments = min(game_json['stats']['numcomments'],200)
    game_json['comments'] = []

    j = 1

    while (num_comments) > 0:
        response = requests.get(f'https://www.boardgamegeek.com/xmlapi/boardgame/{id}?comments=j')

        # Parse HTML and save to BeautifulSoup object¶
        soup = BeautifulSoup(response.text, "html.parser")


        for elm in soup.find_all('comment'):
            try:
                comment_dict = {}
                comment_dict['rating'] = elm.get('rating')
                comment_dict['username'] = elm.get('username')
                comment_dict['comment'] = elm.contents[0]
                game_json['comments'].append(comment_dict)
            except IndexError:
                pass
        j += 1
        num_comments -=50

    with open(f'bbg_json/{id}.json', 'w') as f:
        json.dump(game_json, f)

if __name__ == "__main__":
    id_file = 'game_ids.csv'
    if not os.path.exists(id_file):
        get_game_ids(id_file)
    with open(id_file, 'r') as f:
        ids = [id.strip() for id in f.readlines()]
    for id in tqdm(ids):
        if not os.path.exists(f'bbg_json/{id}.json'):
            get_game_info(id)

    json_list = os.listdir('bbg_json/')
    thumb_list = set([ x.split('.')[0] for x in os.listdir('thumbs/') ])

    json_list = list(filter(lambda x: x.split('.')[0] not in thumb_list, json_list))
    for fname in tqdm(json_list):
        with open(os.path.join('bbg_json',fname), 'r') as f:

            game_info = json.load(f)
            try:
                urllib.request.urlretrieve(game_info['img_url'], f"thumbs/{fname.split('.')[0]}.jpg")
            except ValueError:
                pass
