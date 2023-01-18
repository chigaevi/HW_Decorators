import requests
from HW_1 import logger

def get_all_superhero_list (url='https://akabab.github.io/superhero-api/api/all.json'):
    superhero_list = requests.get(url)
    return superhero_list.json()

@logger
def smartes_superhero(list_heros):
    all_superheros = get_all_superhero_list()
    max_intelligence = 0
    smartest_hero = []
    for name in list_heros:
        for superhero in all_superheros:
            if superhero['name'] == name:
                intelligence = superhero['powerstats']['intelligence']
                if intelligence > max_intelligence:
                    max_intelligence = intelligence
                    smartest_hero = [name]
                elif intelligence == max_intelligence:
                    max_intelligence = intelligence
                    smartest_hero.append(name)
    return print(smartest_hero)

# def get_name_intelligence_list():
#     all_superheros = get_all_superhero_list()
#     for superhero in all_superheros:
#         print(superhero['name'],'-',superhero['powerstats']['intelligence'])

if __name__ == '__main__':
    superheros = ['Hulk', 'Captain America', 'Thanos', 'Watcher', 'Vision']
    smartes_superhero(superheros)
    # get_name_intelligence_list()