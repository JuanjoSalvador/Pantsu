import requests

BASE_URL = "https://nyaa.pantsu.cat/api"

class Users():

    def login(self, username, password):
        login = requests.post("{}/login/".format(BASE_URL), data={'username': username, 'password': password})

        return login

    def profile(self, user_id):
        profile = requests.post("{}/profile/".format(BASE_URL), data={'id': user_id})

        return profile