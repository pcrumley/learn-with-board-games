import os
import matplotlib.pyplot as plt
from tqdm import tqdm
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time
import heapq
import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from pprint import pprint
from PIL import Image
import io
import base64

data = {}

# Games is the JSON we are going to save and load with the
# front end
json_list = os.listdir('bbg_json/')

# First we load in all of the jsons
for fname in tqdm(json_list):
    filter_set = set([])
    with open(os.path.join('bbg_json',fname), 'r') as f:
        data[fname.split('.')[0]] = json.load(f)
        data[fname.split('.')[0]]['game_id'] = fname.split('.')[0]
        comments_cpy = [comment for comment in data[fname.split('.')[0]]['comments']]
        data[fname.split('.')[0]]['comments'] = []
        for comment in comments_cpy:
            if comment['comment'] in filter_set:
                pass
            else:
                data[fname.split('.')[0]]['comments'].append(comment)
                filter_set.add(comment['comment'])
        #max_comments = max(len(data[fname.split('.')[0]]['comments']), max_comments)

#print([key for key in data['1'].keys()])
def for_kids(game):
    ''' The first filter. Based solely off of manufactured
    recommended age. I think this is a place that can be improved.
    '''
    return int(game['age']) < 8 and int(game['age']) > 0

kids_games = list(filter(for_kids, data.values()))

complexity = [g['stats']['averageweight'] for g in data.values()]
age =  [np.log(2021-float(g['yearpublished'])) for g in data.values()]
X = np.array(list(zip(complexity,age)))
#X = np.array(complexity).reshape(-1,1)
y= np.array([g['stats']['average'] for g in data.values()]).reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train) #training the algorithm

def normed_score(game):
    ''' BBG ratings are biased towards complicated games and also
    against older games. Eventually I will use regression to correct for
    the bias.... but for now...'''

    return game['stats']['average']-regressor.predict([[game['stats']['averageweight'],np.log(2021-float(game['yearpublished']))]] )[0,0]

for game in data.values():
    game['overall_score'] = normed_score(game)

analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return score['compound']


def new_score(game, search_string, norm = 10.0,):
    rel_comments = filter(lambda x: search_string in x['comment'], game['comments'])
    if search_string ==' math':
        rel_comments = filter(lambda x: 'math trade' not in x['comment'], rel_comments)
    #rel_comments = list(map(lambda x: x['comment'], rel_comments))
    #scores = map(lambda x: (sentiment_analyzer_scores(x['comment']),x['comment']), rel_comments)

    n_comments = len(list(rel_comments))
    if search_string ==' coop':
        n_comments += len(list(filter(lambda x: ' co-op' in x['comment'], game['comments'])))
    sum = 0
    if n_comments > 2:
        #for elm in  map(sentiment_analyzer_scores, rel_comments):
            #if elm < 0.1:
            #    return -1000
            #else:
        return game['overall_score']# + sum/n_comments * norm)/2
    else:
        return -100000000
def return_n_best_comments(game, N, search_string):
    rel_comments = filter(lambda x: search_string in x['comment'], game['comments'])
    rel_comments = map(lambda x: (sentiment_analyzer_scores(x['comment']),x['comment']), rel_comments)
    #print(list(rel_comments))

    return heapq.nlargest(N, rel_comments)

def return_n_best(N, search_string):
    return filter(lambda x: x[0]>-10, heapq.nlargest(N, map(lambda g: (new_score(g, search_string), g['game_id']), kids_games)))

##### The individual mechanics score
scores_dict = {
    #'dexterity_score': 'dexterity',
    'logic_score': ' logic',
    'deductive_score': ' deduc',
    'pattern_score': ' pattern',
    'co-operative_score': ' coop',
    'math_score': ' math',
    'memorization_score': ' memory'
}
#best_games = heapq.nlargest(10, map(lambda g: (g['overall_score'], g['game_id']), kids_games))
best_games = []
games = {}

for k, v in scores_dict.items():
    games[f'{k}_games'] = [x[1] for x in return_n_best(15, v)]

    best_games.extend(games[f'{k}_games'])
    #print(k, return_n_best(10, v))
#best_games = sorted(list(set(x[1] for x in best_games)))
best_games = list(set(best_games))

for id in best_games:
    games[id] = data[id]
    game = games[id]
    game['best_comments'] = []
    for key, val in scores_dict.items():
        game[key] = new_score(game, val)
        game[f'{key}_comments'] = [x[1] for x in return_n_best_comments(game, 3 , val)]

        game['best_comments'].extend(game[f'{key}_comments'])
    roll_dice = np.random.choice(len(game['best_comments']), size=min(3,len(game['best_comments'])), replace=False)
    tmp_list = []
    for loc in roll_dice:
        tmp_list.append(game['best_comments'][loc])

    game['best_comments'] = tmp_list


    img = Image.open(f'./thumbs/{id}.jpg')

    img_io = io.BytesIO()
    img.save(img_io, format='png',compress_level = 1)#, quality=100)
    img_io.seek(0)
    games[id]['img'] = 'data:image/png;base64,' + base64.b64encode(img_io.getvalue()).decode('utf-8')
games['best_games'] = best_games

with open('data.json', 'w') as f:
    json.dump(games, f)
print([key for key in games.keys()])
#pprint(games)
