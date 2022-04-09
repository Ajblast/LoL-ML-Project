import requests

class RIOTAPI:
    def __init__(self, apikey):
        self.key = apikey

    def request(self, endpoint):
        headers = {"X-Riot-Token": self.key}
        url = "https://na1.api.riotgames.com" + endpoint

        r = requests.get(url, headers=headers)
        return r.json()


#api = RIOTAPI("KEY")
#retval = api.request("/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5")
#print(retval)