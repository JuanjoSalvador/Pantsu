import requests

BASE_URL = "https://nyaa.pantsu.cat/api"

class Torrents():

    def search(self, keyword, limit):
        request = requests.get("{}/search?q={}&limit={}".format(BASE_URL, keyword, limit))

        return request.json()

    def view(self, item_id):
        request = requests.get("/view/{}".format(BASE_URL, item_id))

        return request.json()