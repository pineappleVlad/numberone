import requests
import json

heroes_list = ['Hulk', 'Captain america', 'Thanos']

intelligence_dict = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}
url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'

for hero in heroes_list:
    hero_dict = json.loads(requests.get(url + hero).content)
    intelligence_dict[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])

if intelligence_dict["Hulk"] > intelligence_dict["Captain america"]:
    if intelligence_dict["Hulk"] > intelligence_dict["Thanos"]:
        print("Hulk most intelligence")
    elif intelligence_dict["Hulk"] < intelligence_dict["Thanos"] and intelligence_dict["Captain america"] < intelligence_dict["Thanos"]:
        print("Thanos most intelligence")
else:
    print("Captain america most intelligence")

