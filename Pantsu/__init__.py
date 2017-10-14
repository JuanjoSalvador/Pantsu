
__version__   = '1.0.0'
__author__    = 'Juanjo Salvador'
__email__     = 'juanjosalvador@netc.eu'
__url__       = 'http://juanjosalvador.me'
__copyright__ = '2017 Juanjo Salvador'
__license__   = 'MIT license'

import requests

BASE_URL = "https://nyaa.pantsu.cat/api"

def search(keyword, limit):
    request = requests.get("{}/search?q={}&limit={}".format(BASE_URL, keyword, limit))

    return request.json()

def view(item_id):
    request = requests.get("/view/{}".format(BASE_URL, item_id))

    return request.json()

def login(username, password):
    login = requests.post("{}/login/".format(BASE_URL), data={'username': username, 'password': password})

    return login.json()

def profile(user_id):
    profile = requests.post("{}/profile/".format(BASE_URL), data={'id': user_id})

    return profile.json()