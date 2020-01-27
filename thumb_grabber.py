import os
from tqdm import tqdm
import pprint as pp
import json
import urllib.request
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
