import requests
import json

class RIOTAPI:
    def __init__(self, apikey):
        self.key = apikey

    def request(self, endpoint):
        headers = {"X-Riot-Token": self.key}
        url = "https://na1.api.riotgames.com" + endpoint

        r = requests.get(url, headers=headers)
        return r.json()
