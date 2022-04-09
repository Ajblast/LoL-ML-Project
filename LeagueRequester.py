from RIOTAPI import RIOTAPI, Region

class LeagueRequester:
    def __init__(self, api : RIOTAPI):
        self.api = api

    def challengerPlayers(self, region : Region):
        endpoint = "/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5"
        return self.api.request(region, endpoint)

    def grandmasterPlayers(self, region : Region):
        endpoint = "/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5"
        return self.api.request(region, endpoint)

    def masterPlayers(self, region : Region):
        endpoint = "/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5"
        return self.api.request(region, endpoint)
