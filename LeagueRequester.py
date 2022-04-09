from RIOTAPI import RIOTAPI

class LeagueRequester:
    def __init__(self, api):
        self.api = api

    def challengerPlayers(self):
        endpoint = "/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5"
        return self.api.request(endpoint)

    def grandmasterPlayers(self):
        endpoint = "/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5"
        return self.api.request(endpoint)

    def masterPlayers(self):
        endpoint = "/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5"
        return self.api.request(endpoint)
